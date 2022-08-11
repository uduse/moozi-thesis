start_training = False
trajectory_samples = []
parameter_server = make_parameter_server()
replay_buffer = make_replay_buffer()
training_worker = [make_train_worker() for i in range(num_train_workers)]
testing_worker = make_test_worker()
reanalyze_workers = [make_reanalyze_worker() for i in range(num_reanalyze_worker)]

for epoch in range(num_epochs):
    if not start_training:
        if start_training_condition_met():
            start_training = True

    # synchronize all workers parameters if conditions are met
    if (epoch % train_worker_update_period) == 0:
        for worker in training_worker:
            worker.set_parameters(parameter_server.get_parameters())

    if (epoch % reanalyze_worker_update_period) == 0:
        for worker in reanalyze_workers:
            worker.set_parameters(parameter_server.get_parameters())

    if (epoch % test_worker_eval_period) == 0:
        testing_worker.set_parameters(parameter_server.get_parameters())

    # process trajectories into training targets
    replay_buffer.process_trajectory_samples(trajectory_samples)

    # update parameters by sampling from replay buffer
    if start_training:
        for i in range(num_updates_per_epoch):
            batch = replay_buffer.sample_batch(batch_size)
            parameter_server.update(batch)

    # generate train targets with training  workers
    trajectory_samples.clear()
    for worker in training_worker:
        sample = worker.run()
        trajectory_samples.append(sample)

    # test with testing worker
    if (epoch % test_worker_eval_period) == 0:
        test_result = testing_worker.run()

    # update search statistics with reanalyze workers
    if start_training:
        for worker in reanalyze_workers:
            trajs_to_update = replay_buffer.get_trajectory_samples()
            worker.refill_trajectory(trajs_to_update)
            updated_trajs = worker.run()
            replay_buffer.add_trajs(updated_trajs)

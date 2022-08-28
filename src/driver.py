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
    for worker in training_worker + testing_worker + reanalyze_workers:
        if update_condition_met(worker):
            worker.set_parameters(parameter_server.get_parameters())

    replay_buffer.process_trajectory_samples(trajectory_samples)

    if start_training:
        for i in range(num_updates_per_epoch):
            batch = replay_buffer.sample_batch(batch_size)
            parameter_server.update(batch)

    trajectory_samples.clear()
    for worker in training_worker:
        sample = worker.run()
        trajectory_samples.append(sample)

    if testing_condition_met():
        test_result = testing_worker.run()

    if start_training:
        for worker in reanalyze_workers:
            trajectories_to_update = replay_buffer.get_trajectory_samples()
            worker.refill_trajectory(trajectories_to_update)
            updated_trajectories = worker.run()
            replay_buffer.add_trajs(updated_trajectories)

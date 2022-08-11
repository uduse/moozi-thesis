vectorized_environment = make_vectorized_environment(name, number_of_environments)
observation_stacker = make_obs_stacker(history_length)
planner = make_planner(mcts_config)
step_samples: list = []

def run_once(steps):
    for i in range(steps):
        env_result = vectorized_environment.step(action, env_result.is_last)
        stacked_observation = observation_stacker.process(env_result.observation)
        action, search_statistics = planner.process(stacked_observation)
        step_sample = (env_result, action, search_statistics)
        step_samples.append(step_sample)
        
    trajectory_samples = take_finished_trajectories(step_samples)
    return trajectory_samples
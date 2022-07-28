# interact with the environment with a policy indefinitely
def main_loop(env, policy):
    action = 0
    while True:
        result = step(env, action, result.is_last)
        action = policy(result.observation)
    
# episodic task stepping
def step(env, action, is_last):
    if is_last:
        return env.reset()
    else:
        return env.step(action)

# continuous task stepping
def step(env, action, is_last):
    return env.step(action)
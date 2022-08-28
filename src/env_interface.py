# interact with the environment with a policy indefinitely
def main_loop(env, policy):
    action = 0
    reset = True
    while True:
        result = step(env, action, reset)
        action = policy(result.observation)
        reset = result.is_last


def step(env, action, reset):
    if env.type == "episodic":
        if reset:
            return env.reset()
        else:
            return env.step(action)
    elif env.type == "continuous":
        return env.step(action)

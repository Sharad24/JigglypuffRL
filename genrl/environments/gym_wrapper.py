import gym

from genrl.environments import BaseWrapper


class GymWrapper(BaseWrapper, gym.Wrapper):
    """
    Wrapper class for all Gym Environments

    :param env: Gym environment name
    :param n_envs: Number of environments. None if not vectorised
    :param parallel: If vectorised, should environments be run through \
serially or parallelly
    :type env: string
    :type n_envs: None, int
    :type parallel: boolean
    """
    # TODO(zeus3101) Add functionality for VecEnvs
    def __init__(self, env):
        super(GymWrapper, self).__init__(env)
        self.env = env
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space

    def __getattr__(self, name):
        """
        All other calls would go to base env
        """
        env = super(GymWrapper, self).__getattribute__('env')
        return getattr(env, name)

    def render(self, mode="human"):
        """
        Renders all envs in a tiles format similar to baselines.

        :param mode: Can either be 'human' or 'rgb_array'. \
Displays tiled images in 'human' and returns tiled images in 'rgb_array'
        :type mode: string
        """
        self.env.render(mode=mode)

    def seed(self, seed=None):
        """
        Set environment seed

        :param seed: Value of seed
        :type seed: int
        """
        self.env.seed(seed)

    def step(self, action):
        """
        Steps the env through given action

        :param action: Action taken by agent
        :type action: NumPy array
        """
        return self.env.step(action)

    def reset(self):
        """
        Resets environment

        :returns: Initial state
        """
        return self.env.reset()

    def close(self):
        """
        Closes environment
        """
        self.env.close()


def GymEnv(env_id):
    """
    Function to apply wrappers for all regular Gym envs by Trainer class

    :param env: Environment Name
    :type env: string
    """
    gym_env = gym.make(env_id)
    env = GymWrapper(gym_env)

    return env
import os

from obstacle_tower_env import ObstacleTowerEnv

env = ObstacleTowerEnv(os.environ['OBS_TOWER_PATH'], worker_id=0)

env.seed(72)
env.floor(12)
env.reset()
for action in [18, 18, 18, 18, 18, 18, 30, 24, 24, 21, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 24, 24, 6, 6, 6, 6, 6, 6, 6, 6, 30, 30, 30, 30, 30, 18, 24, 24, 24, 6, 6, 6, 6, 6, 6, 24, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 24, 24, 24, 18, 30, 18, 18, 30, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 30, 24, 24, 30, 30, 24, 24, 24, 30, 30, 30, 30, 30, 18, 18, 18, 18, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 18, 30, 18, 18, 18, 18, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 24, 24, 24, 24, 24, 24, 24, 24, 18, 30, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 24, 21, 18, 24, 24, 24, 24, 18, 18, 18, 24, 18, 18, 18, 18, 30, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 18, 18, 30, 30, 30, 30, 30, 30, 12, 12, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 30, 24, 24, 30, 30, 30, 30, 21, 18, 24, 24, 24, 24, 24, 30, 30, 18, 18, 24, 21, 18, 18, 18, 30, 18, 24, 24, 30, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 6, 6, 6, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 18, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 30, 30, 18, 24, 18, 30, 18, 18, 24, 18, 18, 24, 30, 30, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 18, 24, 24, 24, 6, 6, 6, 6, 6, 6, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 18, 30, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 18, 24, 24, 24, 24, 24, 18, 18, 18, 18, 30, 18, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 30, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 24, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 30, 18, 24, 24, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 18, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 24, 24, 6, 6, 6, 6, 6, 6, 6, 30, 30, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 24, 6, 6, 6, 6, 6, 6, 6, 30, 30, 30, 30, 30, 24, 24, 24, 6, 6, 6, 6, 6, 24, 24, 24, 24, 18, 18, 18, 30, 30, 18, 18, 24, 30, 24, 12, 12, 30, 30, 30, 30, 18, 18, 24, 24, 6, 6, 6, 6, 6, 6, 6, 6, 30, 30, 6, 6, 6, 6, 30, 18, 18, 18, 18, 24, 18, 30, 30, 18, 6, 6, 6, 6, 6, 24, 30, 18, 24, 24, 6, 6, 6, 6, 24, 24, 30, 30, 30, 30, 24, 24, 6, 6, 6, 6, 6, 6, 24, 30, 30, 30, 18, 18, 24, 24, 6, 6, 6, 6, 6, 24, 24, 24, 24, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 18, 18, 18, 24, 24, 18, 18, 18, 18, 18, 30, 30, 30, 18, 18, 24, 24, 18, 6, 6, 18, 18, 18, 18, 18, 18, 18, 30, 30, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 18, 18, 18, 18, 30, 30, 30, 30, 30, 24, 24, 24, 18, 18, 24, 30, 30, 30, 18, 18, 18, 30, 30, 30, 30, 18, 18, 24, 18, 30, 30, 24, 24, 30, 30, 30, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 18, 18, 18, 18, 18, 30, 24, 24, 24, 6, 6, 6, 6, 6, 6, 24, 24, 24, 24, 30, 30, 24, 24, 30, 30, 24, 24, 24, 24, 24, 21, 30, 24, 24, 24, 24, 18, 18, 18, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 21, 21, 18, 18, 18, 24, 18, 18, 18, 18, 30, 18, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 24, 30, 30, 24, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 21, 24, 24, 24, 18, 18, 30, 24, 30, 24, 24, 24, 24, 24, 18, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 18, 30, 24, 24, 18, 18, 30, 30, 30, 30, 30, 30, 18, 18, 21, 18, 24, 30, 18, 18, 24, 24, 6, 6, 6, 24, 24, 24, 18, 24, 24, 24, 24, 21, 18, 30, 18, 18, 24, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 18, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 18, 18, 30, 18, 18, 18, 18, 30, 30, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 24, 21, 24, 24, 24, 24, 18, 18, 30, 30, 24, 24, 24, 18, 24, 24, 30, 30, 30, 24, 24, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 18, 24, 24, 18, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 18, 30, 30, 18, 24, 18, 18, 18, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 30, 30, 24, 24, 30, 30, 18, 18, 30, 30, 30, 18, 24, 24, 24, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 30, 18, 24, 18, 18, 18, 30, 24, 30, 30, 18, 30, 24, 24, 24, 24, 24, 18, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 21, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 30, 30, 24, 24, 21, 18, 18, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 18, 18, 18, 18, 18, 18, 18, 24, 24, 30, 30, 30, 24, 24, 30, 30, 18, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 30, 30, 24, 24, 30, 30, 30, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 24, 24, 18, 18, 30, 30, 18, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 30, 30, 18, 21, 21, 24, 24, 24, 24, 18, 30, 30, 18, 18, 30, 24, 24, 18, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 30, 24, 24, 24, 24, 24, 24, 24, 24, 21, 21, 24, 24, 24, 24, 24, 24, 18, 18, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 30, 30, 30, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 18, 24, 24, 24, 24, 18, 18, 18, 18, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 30, 30, 30, 24, 24, 18, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 30, 30, 18, 18, 24, 24, 24, 18, 18, 18, 18, 30, 30, 24, 24, 24, 24, 18, 18, 30, 30, 30, 30, 30, 30, 30, 18, 18, 18, 30, 30, 30, 30, 30, 30, 30, 30, 18, 24, 18, 24, 30, 30, 18, 18, 18, 24, 24, 18, 30, 30, 30, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 30, 30, 24, 18, 21, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 18, 18, 18, 18, 24, 30, 18, 24, 30, 24, 24, 24, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 18, 18, 21, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 18, 18]:
    env.step(action)

env.seed(58)
env.floor(10)
env.reset()
for action in [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 24, 30, 30, 30, 30, 30, 30, 30, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 24, 18, 18, 18, 18, 18, 24, 21, 18, 30, 30, 24, 18, 18, 18, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 24, 24, 24, 24, 18, 18, 18, 18, 18, 24, 18, 18, 24, 18, 18, 18, 18, 18, 18, 24, 18, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 6, 6, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 30, 18, 18, 18, 24, 30, 18, 18, 18, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 24, 18, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 30, 30, 18, 18, 24, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 18, 18, 18, 18, 18, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 21, 18, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 18, 30, 18, 18, 24, 24, 18, 18, 18, 18, 18, 30, 18, 6, 6, 6, 6, 6, 24, 24, 24, 24, 24, 24, 24, 21, 30, 18, 18, 18, 18, 30, 18, 18, 24, 24, 18, 18, 30, 30, 30, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 24, 24, 18, 18, 18, 18, 18, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 6, 6, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 24, 24, 30, 30, 30, 30, 18, 24, 24, 6, 6, 6, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 24, 24, 24, 18, 18, 18, 18, 30, 30, 24, 24, 18, 18, 18, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 21, 30, 30, 18, 18, 24, 18, 18, 30, 30, 30, 30, 30, 24, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 18, 18, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 30, 30, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 6, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 18, 18, 18, 18, 24, 18, 18, 18, 30, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 30, 30, 30, 30, 18, 18, 18, 18, 30, 30, 18, 18, 21, 21, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 21, 30, 18, 24, 18, 30, 18, 18, 18, 18, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 18, 30, 30, 24, 24, 24, 24, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 30, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 24, 30, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 24, 24, 24, 6, 6, 6, 6, 6, 6, 6, 6, 30, 30, 30, 30, 30, 30, 18, 24, 24, 6, 6, 6, 6, 6, 6, 6, 18, 18, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 6, 6, 6, 6, 24, 24, 24, 24, 30, 30, 30, 30, 30, 24, 24, 24, 6, 6, 6, 6, 6, 6, 24, 30, 30, 30, 30, 24, 24, 24, 6, 6, 6, 6, 6, 6, 24, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 18, 6, 6, 6, 6, 6, 6, 6, 6, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 6, 6, 24, 24, 24, 24, 24, 24, 30, 30, 30, 30, 18, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 18, 18, 24, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 24, 24, 24, 24, 24, 24, 18, 18, 18, 24, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 24, 24, 24, 6, 6, 6, 6, 6, 6, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 6, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 24, 18, 18, 18, 30, 18, 18, 18, 30, 18, 18, 30, 30, 21, 18, 18, 18, 18, 24, 18, 18, 21, 24, 24, 18, 18, 18, 24, 12, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 18, 30, 18, 21, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 30, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 18, 30, 30, 30, 18, 24, 24, 6, 6, 6, 6, 6, 6, 6, 6, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 6, 6, 6, 6, 6, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 24, 30, 30, 18, 18, 18, 24, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 18, 24, 24, 30, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 24, 18, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 21, 18, 18, 18, 18, 21, 21, 21, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 24, 18, 18, 18, 18, 30, 18, 18, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 24, 6, 18, 24, 24, 24, 24, 6, 6, 6, 6, 6, 24, 18, 18, 18, 18, 30, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 18, 18, 24, 24, 24, 6, 6, 6, 6, 6, 6, 6, 18, 18, 18, 18, 24, 24, 18, 18, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 30, 18, 18, 18, 30, 30, 30, 18, 18, 18, 18, 30, 18, 24, 24, 24, 24, 24, 18, 24, 30, 18, 18, 18, 18, 24, 30, 30, 30, 30, 30, 30, 30, 30, 24, 24, 24, 6, 6, 6, 6, 6, 24, 24, 18, 18, 18, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 18, 18, 18, 18, 30, 18, 24, 24, 18, 18, 30, 30, 18, 24, 24, 24, 30, 30, 30, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 18, 18, 18, 18, 24, 24, 18, 18, 30, 24, 6, 6, 6, 6, 6, 6, 24, 24, 24, 18, 18, 30, 30, 30, 18, 18, 24, 24, 24, 18, 18, 30, 30, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 24, 24, 21, 30, 12, 30, 18, 18, 18, 18, 30, 30, 18, 18, 18, 18, 24, 30, 30, 30, 30, 18, 18, 24, 24, 24, 24, 6, 6, 6]:
    env.step(action)

env.seed(37)
env.floor(11)

print('resetting (this will hang)...')
env.reset()
print('done reset')
env.close()
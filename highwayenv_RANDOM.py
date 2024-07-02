#AUTOMATIC/RANDOM
import gymnasium as gym
from matplotlib import pyplot as plt
import warnings
from random import choice
import time
warnings.filterwarnings("ignore")



env = gym.make('highway-v0', render_mode='rgb_array')

env.configure({
    "duration": 400,
    "lanes_count": 5,
    #"action": {
    #"type": "DiscreteMetaAction"
    #          },
    #"show_trajectories": True
})

env.reset()
start = time.time()

done = False
truncated = False
ACTIONS_ALL = {
        0: 'LANE_LEFT',
        1: 'IDLE',
        2: 'LANE_RIGHT',
        3: 'FASTER',
        4: 'SLOWER'
}
average_speed = 0
ticks_counted = 0
chosen_actions = [0,0,0,0,0]
while not done and not truncated:
    action = choice(env.get_available_actions())
    chosen_actions[action]+=1
    obs, reward, done, truncated, info = env.step(action)
    env.render()
    average_speed += info['speed']
    ticks_counted += 1
    #print(info)
end = time.time()
print("____________________")
print("FINISHED SIMULATION.")
print()
print()
print("Average speed:", round(average_speed / ticks_counted, 2))
print()
print("Actions:", chosen_actions)
print()
print("Time taken", round(end-start, 2))
print()
#plt.imshow(env.render())
#plt.show()

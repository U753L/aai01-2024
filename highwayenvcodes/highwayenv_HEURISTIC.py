#HEURISTIC/RULE-BASED
import gymnasium as gym
import warnings
from random import choice
import time
import numpy as np
warnings.filterwarnings("ignore")

#fout = open('test.txt', 'w')
env = gym.make('highway-v0', render_mode='rgb_array')

env.configure({
    "action": {
        "type": "DiscreteMetaAction",
    },
    "observation": {
        "type": "OccupancyGrid",
        "vehicles_count": 15,
        "features": ["presence", "x", "y", "vx", "vy", "cos_h", "sin_h"],
        "features_range": {
            "x": [-22.5, 22.5],
            "y": [-22.5, 22.5],
            "vx": [-20, 20],
            "vy": [-20, 20]
        },
        "grid_size": [[-45, 45], [-45, 45]],
        "grid_step": [2, 2],
        "absolute": False
    }, ##### our result from this is a 15x15 grid in each of the attributes
    "lanes_count": 4,
    "vehicles_count": 50,
    "duration": 100,  # [s]
    "initial_spacing": 2,
    "simulation_frequency": 15,  # [Hz] # CHANGE BACK TO 15
    "policy_frequency": 0.25,  # [Hz]
    "render_agent": True,
})

obs, other = env.reset()
#for a in obs[0]:
#    for b in a:
#        fout.write(str(b) + ' ')
#    fout.write('\n')
#fout.close()
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
speed=100


def getAction(env, obs, speed):
    available = env.get_available_actions()
    car_left = any(obs[0][20][19:30]) or 0 not in available # cant go to left lane
    car_right = any(obs[0][24][19:30]) or 2 not in available # cant go to right lane
    car_ahead = any(obs[0][22][23:35])
    slow_car_ahead = car_ahead and any([obs[3][22][i]<i for i in range(23,35)])
    #print(car_left, car_ahead, car_right)
    if not slow_car_ahead:
        if speed <= 21:
            return 3
        return 1
    if car_left:
        if car_right:
            return 4
        return 2
    if car_right:
        return 0
    return 2
total_reward = 0
while not done and not truncated:
    
    action = getAction(env, obs, speed)
    chosen_actions[action]+=1
    obs, reward, done, truncated, info = env.step(action)
    total_reward += reward
    speed = info['speed']
    env.render()
    if not done and not truncated:
        average_speed += info['speed']
        ticks_counted += 1
    
    
    
    
end = time.time()


# print lines

print("____________________")
print("FINISHED SIMULATION.")
print()
print()
print("Average speed:", round(average_speed / ticks_counted, 2))
print()
print("Actions:", chosen_actions)
print()
print("Time taken:", round(end-start, 2))
print()
print("Total Reward:", round(total_reward, 2))

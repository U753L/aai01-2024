#MANUAL
import gymnasium as gym
from matplotlib import pyplot as plt
import warnings
from random import choice
import time
import pygame
from pygame.locals import *


warnings.filterwarnings("ignore")



env = gym.make('highway-v0', render_mode='rgb_array')

env.configure({
    "policy_frequency": 1.5,
    "duration": 115,
    "lanes_count": 5,
    "manual_control": True,
    #"action": {
    #"type": "DiscreteMetaAction"
    #          },
})
## PYGAME THINGS
pygame.init()
screen = pygame.display.set_mode( (640,480) )
pygame.display.set_caption('Python numbers')
screen.fill((159, 182, 205))

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
############ LL, I, LR, F, S
while not done and not truncated:
    action_taken = 1
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        action_taken = 0
    elif keys[K_DOWN]:
        action_taken = 2
    elif keys[K_RIGHT]:
        action_taken = 3
    elif keys[K_LEFT]:
        action_taken = 4
    chosen_actions[action_taken]+=1
    obs, reward, done, truncated, info = env.step(1)
    env.render()
    average_speed += info['speed']
    ticks_counted += 1
    #print(chosen_actions, action_taken)
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

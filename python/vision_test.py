import numpy as np
from unityagents import UnityEnvironment

# Unity Parameters

GAME_FILE = "Unity_Vision_Test.exe"

BRAIN = "Brain"

IMG_LENGTH = 32 

# Training Parameters

MAX_STEPS = 10

# Logic
ENV = UnityEnvironment(file_name=GAME_FILE)
ENV.reset(False, config=None)

# action = [rot_x, rot_y, rot_z, mov_x, mov_y]
ACTION = {BRAIN : [1.0, 2.0, 0.0, 0.0, 0.0]}

for i in range(MAX_STEPS):
    info = ENV.step(ACTION, memory=None, value=None)[BRAIN]
    state = info.states[0]
    # np.reshape(state, {length, length})
    
    print("step = {}".format(i))
    print(state)

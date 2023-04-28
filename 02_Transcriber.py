from videogrep import transcribe
import os
import time
import customPaths

path = customPaths.path


then = time.time()
for file in os.listdir(path):
    layer_1 = path+'/'+file
    for file in os.listdir(layer_1):
        filename = os.fsdecode(layer_1+'/'+file)
        print(file)
        if (filename.endswith((".mp4", ".mov", ".ogv", ".avi"))):
            transcribe.transcribe(filename)
now = time.time()
print(now)
prtime = now-then
print(f'it took {prtime} seconds or {prtime/60} minutes')
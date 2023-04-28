import pandas as pd
import os
import shutil
import customPaths
from pprint import pprint
pd.options.display.show_dimensions = True
d = {
    'vPath':[], 
    'tPath':[],
    'transcribed':[]
    }

df = pd.DataFrame(data=d)

path = customPaths.path
videos = customPaths.videos
tscripts = customPaths.tscripts
masterjs = customPaths.masterjs

if os.path.isdir(tscripts) == False:
    os.mkdir(tscripts)

if os.path.isdir(videos) == False:
    os.mkdir(videos)

for file in os.listdir(path):
    layer_1 = path+'/'+file
    for file in os.listdir(layer_1):
        filename = os.fsdecode(layer_1+'/'+file)
        if (filename.endswith((".mp4", ".mov", ".ogv", ".avi"))) and os.path.isfile(videos + '/' +file) == False:
            shutil.copy(filename, videos)
            print(f'copiing video: {filename}')
        if (filename.endswith((".json"))) and os.path.isfile(tscripts + '/' +file) == False:
            shutil.copy(filename, tscripts)
            print(f'copiing json: {filename}')

for file in os.listdir(videos):
    videofiles = videos + '/' + file
    tsfiles = tscripts + '/' + file[0:-4] + '.json'
    if os.path.isfile(tsfiles):
        tr = True
    else:
        tr = False
    df2 = pd.DataFrame(data={
            'vPath':[file],
            'tPath':[tsfiles],
            'transcribed':[tr]
    })
    df = pd.concat([df,df2], ignore_index=True)

# print(df)

words = pd.DataFrame({
             'word':[],
             'start':[],
             'end':[],
             'vpath':[]
         })

for ind in (df.index):
    vpath = df['vPath'][ind]
    tpath = df['tPath'][ind]
    if df['transcribed'][ind]:
        ts = pd.read_json(tpath)
        ts = ts[['words']]
        for ind in (ts.index):
            tmp = ts['words'][ind]
            tmpwords = pd.DataFrame(data={
                'word':[tmp[0]['word']],
                'start':[tmp[0]['start']],
                'end':[tmp[0]['end']],
                'vpath':[vpath]
            })
            words = pd.concat([words, tmpwords], ignore_index=True)
print(words)    
words.to_json(masterjs)




import internetarchive
from internetarchive import *
import time
import os
import customPaths


path = customPaths.path

#'title:(Katy) AND mediatype:(movies)'
search = internetarchive.search_items('mediatype:(movies) AND language:"en" OR language:"En" OR language:"EN" AND NOT title:(nasa) AND NOT category:(nasa) AND NOT creator:(nasa) AND NOT creator:(NASA)')
absthen = time.time()
count = 0
for i in search:
    count = count + 1
    f = get_item(i['identifier'])
    if os.path.isdir(path + f.metadata['identifier']) != True:
        print(f" \033[94m {count}/{len(search)} \033[0m \n \033[92m \033[1m {f.metadata['title']} language: {f.metadata['language']}  \033[0m \n ID:   {i['identifier']}")
        then = time.time()
        try:
            f.download(destdir=path, ignore_existing=True, dry_run=False)
            # f.download(destdir=path, ignore_existing=True, dry_run=False, glob_pattern='*.mp4')
            # f.download(destdir=path, ignore_existing=True, dry_run=False, glob_pattern='*.mov')
            # f.download(destdir=path, ignore_existing=True, dry_run=False, glob_pattern='*.avi')
            # f.download(destdir=path, ignore_existing=True, dry_run=False, glob_pattern='*.ogv')
            # f.download(destdir=path, ignore_existing=True, dry_run=False, glob_pattern='*.jpg')
            # f.download(destdir=path, ignore_existing=True, dry_run=False, glob_pattern='*.xml')
        except:
            pass
        now = time.time()
        prtime = now-then
        print(f'-----------------------------------------------------------  it took {round(prtime/60, ndigits=2)} minutes Time: {time.strftime("%H:%M:", time.gmtime())}')

absnow = time.time()
absprtime = absnow-absthen
print(f'downloading took {round(absprtime/60, ndigits=2)} minutes') 
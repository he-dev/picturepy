
import os
import time
import itertools
import shutil
from pprint import pprint

PICTURES_PATH = "C:\\temp\\picturepy\\pictures\\"
GALLERIES_PATH = "C:\\temp\\picturepy\\galleries\\"

# Moves pictures from the main directory to subdirectories by modified date.

def format_filemtime(path):
    filemtime = os.path.getmtime(path)
    return time.strftime('%Y-%m-%d', time.gmtime(filemtime))

def group_pictures(keep_original=False):    

    start = time.perf_counter()

    picture_names = os.listdir(PICTURES_PATH)

    print(f"picture count: {len(picture_names)}")
    
    pictures_by_mtime = itertools.groupby(picture_names, lambda name: format_filemtime(os.path.join(PICTURES_PATH,name)))

    for (dir, picture_names) in pictures_by_mtime:
        path_dir = os.path.join(GALLERIES_PATH, dir)
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
            print(f"'{dir}' created.")
        else:
            print(f"'{dir}' already exists.")        

        do, verb = (shutil.copyfile, "copied") if keep_original else (shutil.move, "moved")
        
        for file in picture_names:
            do(
                src=os.path.join(PICTURES_PATH, file), 
                dst=os.path.join(path_dir, file))                
            print(f"\t'{file}' {verb}.")

    end = time.perf_counter()
    elapsed = round(end - start,2)
    print(f"elapsed: {elapsed} sec")

# --- --- ---

def main():
    group_pictures(keep_original=False)
    #group_pictures()

if __name__ == '__main__':
    main()


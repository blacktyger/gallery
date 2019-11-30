import os, time
import json
import random
from PIL import Image
import shutil
import pickle
from datetime import datetime
from stat import *


# files formats
def img_format():
    return '.JPG', '.jpg', '.jpeg', '.JPEG', '.BMP', '.bmp', '.PNG', '.png'


# all files paths
def file_path():
    location = 'E:\gallery\django_project\\blog\static\Zdjecia'
    files_path = []
    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in f:
            if item.endswith(img_format()):
                files_path.append(os.path.join(r, item))
    return files_path


# get file info (date, time)
def file_info(file):
    stats = datetime.fromtimestamp(os.stat(file)[ST_MTIME])
    ctx = {
        'path': file,
        'year': stats.strftime("%Y"),
        'month': [stats.strftime("%B"), stats.strftime("%m")],
        'day': [stats.strftime("%A"), stats.strftime("%d")],
        'time': stats.strftime("%H:%M"),
    }
    return ctx


# save everything to JSON file
def files_to_json():
    img_files = [img for img in file_path() if img.endswith(img_format())]
    print(f"Images: {len(img_files)}")
    with open('all_files.txt', 'w') as f:
        photos = [file_info(img) for img in img_files]
        json.dump({'photos': photos}, f, indent=4)


def display_info(file):
    dir = f"Info: " + file['path'].split('\\')[-2]
    date = f"Photo Date: {file['day'][0]}, {file['day'][1]} {file['month'][0]} {file['year']}"
    time = f"Photo Time: {file['time']}"
    return f"{dir} \n{date} \n{time} \n"


# TESTING AREA ---------------------------------------file------------------------------------------------
def test_random():
    with open('all_files.txt') as f:
        link_list = json.load(f)
        counter = 0
        while counter < 5:
            x = link_list['photos'][random.randint(0, 13946)]
            if x['year'] == '2018':
                print(display_info(x))
                # img = Image.open(x['path'])
                # img.show()
                counter += 1


#files_to_json()
test_random()

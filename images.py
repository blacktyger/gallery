import os
import json
import random
from PIL import Image
import shutil
import pickle


location = 'E:\gallery\django_project\\blog\static\Zdjecia\Szkocja'


# files formats
def img_format():
    return '.JPG', '.jpg', '.jpeg', '.JPEG', '.BMP', '.bmp', '.PNG', '.png'


# all files paths
def file_path():
    files_path = []
    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in f:
            if item.endswith(img_format()):
                files_path.append(os.path.join(r, item))
    return files_path


# get file info from title (date, time)
def file_info(file):
    title = str(file.split('\\')[-1])
    ctx = {
        'path': file,
        'year': str(title.split('_')[1][:4]),
        'month': str(title.split('_')[1][4:6]),
        'day': str(title.split('_')[1][-2:]),
        'time': f"{str(title.split('_')[2][:2])}:{str(title.split('_')[2][2:4])}",
    }
    return ctx


# make list of all files in folder
img_files = [img for img in file_path() if img.endswith(img_format())]
print(f"Images: {len(img_files)}")


# save everything to JSON file
def files_to_json():
    with open('all_files.txt', 'w') as f:
        photos = [file_info(img) for img in img_files if len(img.split('\\')[-1]) > 20]
        nonames = [img for img in img_files if len(img.split('\\')[-1]) < 15]
        json.dump({'photos': photos, 'nonames': nonames}, f, indent=4)

files_to_json()


# access files details from JSON file
with open('all_files.txt') as f:
    link_list = json.load(f)
    print(link_list['photos'][1])


# test
def test_random():
    files_to_json()  # map folder
    x = link_list['photos'][random.randint(10, 50)]
    print(x['month'], x['day'], x['time'])

    img = Image.open(x['path'])
    img.show()


test_random()

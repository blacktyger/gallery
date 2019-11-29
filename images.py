import os
import json
import random
from PIL import Image
import shutil
import pickle


# files formats
def img_format():
    return ('.JPG', '.jpg', '.jpeg', '.JPEG', '.BMP', '.bmp', '.PNG', '.png')


def vid_format():
    pass


# all files paths
def paths(folder_name='2016', main_path='E:\gallery\django_project\\blog\static\Zdjecia'):
    ctx = {
        'main_path': main_path,
        'folder_name': folder_name,
        'folder_path': main_path + '\\' + folder_name,
    }
    return ctx


# get file info from title (date, time)
def file_info(file):
    ctx = {
        'full_path': f"{paths()['folder_path']}\\{file}",
        'year': str(file.split('_')[1][:4]),
        'month': str(file.split('_')[1][4:6]),
        'day': str(file.split('_')[1][-2:]),
        'time': f"{str(file.split('_')[2][:2])}:{str(file.split('_')[2][2:4])}",
    }
    return ctx


# make list of all files in folder
img_files = [img for img in os.listdir(paths()['folder_path']) if img.endswith(img_format())]
print(f"All files in {paths()['folder_name']}: {len(os.listdir(paths()['folder_path']))}")
print(f"Images: {len(img_files)}")

files_info = paths()['folder_name'] + '.txt'


# save everything to JSON file
def files_to_json():
    with open(files_info, 'w') as f:
        photos = [file_info(img) for img in img_files if len(img) > 20]
        nonames = [img for img in img_files if len(img) < 15]
        json.dump({'photos': photos, 'nonames': nonames}, f, indent=4)


# access files details from JSON file
with open(files_info) as f:
    link_list = json.load(f)
    print(link_list['photos'][1])


# test
def test_random():
    files_to_json()  # map folder
    x = link_list['photos'][random.randint(10, 50)]
    print(x['month'], x['day'], x['time'])

    img = Image.open(x['full_path'])
    img.show()


test_random()

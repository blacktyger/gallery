import os
import random
from PIL import Image
import shutil
import pickle


def img_format():
    return ('.JPG', '.jpg', '.jpeg', '.JPEG', '.BMP', '.bmp', '.PNG', '.png')


def vid_format():
    pass


def paths(folder_name='2016', main_path='E:\gallery\django_project\\blog\static\Zdjecia'):
    main_path = main_path
    folder_name = folder_name
    folder_path = main_path + '\\' + folder_name
    return [main_path, folder_path, folder_name]


def file_info(file):
    year = str(file.split('_')[1][:4])
    month = str(file.split('_')[1][4:6])
    day = str(file.split('_')[1][-2:])
    time = f"{str(file.split('_')[2][:2])}:{str(file.split('_')[2][2:4])}"
    return [file, year, month, day, time]


# make list of all files in folder
img_files = [img for img in os.listdir(paths()[1]) if img.endswith(img_format())]
print(f"All files in {paths()[2]}: {len(os.listdir(paths()[1]))}")
print(f"Images: {len(img_files)}")


# list of img's to file
files_info = paths()[2] + '.txt'
with open(files_info, 'w') as f:
    for img in img_files:
        if len(img) > 20:
            f.write(str(file_info(img)) + "\n")
        else:
            f.write(str([img]) + "\n")

# access file and make link to image
with open(files_info, "r") as f:
    link_list = [paths()[1] + '\\' + str(line.strip().split("'")[1]) for line in f]



def test_random():
    x = random.choice(link_list)
    print(x)
    img = Image.open(x)
    img.show()

test_random()


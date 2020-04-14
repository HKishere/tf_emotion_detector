#!/usr/bin/python
import csv
import os
from PIL import Image
import numpy as np


datasets_path = r'./'
csv_file = os.path.join(datasets_path, 'fer2013.csv')

save_path= os.path.join(datasets_path, 'train')

if not os.path.exists(save_path):
    os.makedirs(save_path)

num = 1
with open(csv_file) as f:
    csvr = csv.reader(f)
    header = next(csvr)
    for emtion, pixel, usage in csvr:
        pixel = np.asarray([float(p) for p in pixel.split()]).reshape(48, 48)
        subfolder = os.path.join(save_path, emtion)
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        im = Image.fromarray(pixel).convert('L')
        image_name = os.path.join(subfolder, '{:05d}.jpg'.format(num))
        print(image_name)
        im.save(image_name)
        num = num + 1

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:33:40 2022

@author: UAB
"""
import os
import numpy as np
import keras
import tensorflow
from sklearn.model_selection import train_test_split
import nibabel as nib
import tensorflow as tf
from tensorflow.python.keras.utils.data_utils import Sequence
from keras.utils import np_utils
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from skimage import measure
from skimage.transform import resize
from keras_unet.metrics import dice_coef
from keras_unet.models import custom_unet
from keras_unet.losses import jaccard_distance
from sklearn.model_selection import train_test_split
from PIL import Image
from PIL import ImageOps
import fnmatch
import nibabel as nib
import shutil


def gather_set_and_path(data_path, phrase):
    set_of = []
    path = data_path + '\\'
    for f in os.listdir(data_path):
      if phrase in f:
        set_of.append(str(data_path+f))
      else:
        continue
    #set_of = np.array(set_of)

    indices = np.array(range(len(set_of))) # we will use this in the next step.

    return set_of

def gather_set(data_path, phrase):
    set_of = []
    path = data_path + '\\'
    for f in os.listdir(data_path):
      if phrase in f:
        set_of.append(f)
      else:
        continue
    #set_of = np.array(set_of)

    indices = np.array(range(len(set_of))) # we will use this in the next step.

    return set_of

#%%

data_path_1 = r"C:\Users\UAB\Kidney-Segmentation-Jupyter\data\\"
data_path_2 = r"C:\Users\UAB\data\Mayo\data\\"
data_path_3 = r"C:\Users\UAB\data\Emory\data\\"
data_path_4 = r"C:\Users\UAB\data\UAB\data\\"
 UABblaz
images_1 = gather_set_and_path(data_path_1, '_M')
images_2 = gather_set_and_path(data_path_2, '_M')
images_3 = gather_set_and_path(data_path_3, '_M')
images_4 = gather_set_and_path(data_path_4, '_M')


images = images_1+images_2+images_3+images_4

print(len(images))
#%%
labels_1 = gather_set_and_path(data_path_1, '_K')
labels_2 = gather_set_and_path(data_path_2, '_K')
labels_3 = gather_set_and_path(data_path_3, '_K')
labels_4 = gather_set_and_path(data_path_4, '_K')

labels = labels_1 + labels_2 + labels_3 + labels_4
print(len(labels))
#%%
d = {}
for i in images:
    if i not in d:
        d[i] = len(d)

labels_mapping = list(map(d.get, images))
#print(labels_mapping)

labels = {images[i]:labels_mapping[i] for i in range(len(images))}

#%%
id_list = []

train_sets = ["KU_","EM_", "UB_"]
val_sets = ["MA_"]

train_li = []
for i in range(len(images)):
    if any(phrase in images[i] for phrase in train_sets):
        train_li.append(images[i])

val_list = [] 
for i in range(len(images)):
    if any(phrase in images[i] for phrase in val_sets):
        val_list.append(images[i])
#training_list = [image for image in images if any(phrase in images for phrase in train_sets)]


#%%
files = gather_set(r"C:\Users\UAB\data\Mayo\data", '.npy')
    
for filename in (filename for filename in files if not filename.startswith('MA_')):
    print(filename)
    os.rename(filename, str('MA_'+filename))
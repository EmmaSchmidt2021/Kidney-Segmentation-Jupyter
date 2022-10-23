# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:32:24 2022

@author: UAB
"""

import os
raw_path = r'C:\Users\UAB\data\Mayo\Original\Issues'

patient_folders = []
pt_fnames = []


for root, dirs, files in os.walk(os.path.normpath(raw_path), topdown=True):
    for name in files:
        #print(os.path.join(root, name))
        pt_fnames.append(os.path.join(root, name))
print('\nPatient Folders have been identified\n')
    #sort through and get only the files with ROI in them
    #this eliminates the tiff and 3D files 
    #%%
    ROI_list = []
    for j in range(len(pt_fnames)):
        ROI_name = 'ROI'
        filename = os.path.basename(pt_fnames[j])
        if ROI_name in filename:
            ROI_list.append(pt_fnames[j])
    print('\nFilenames have been found and added\n')
    print('copied and moved '+ str(len(ROI_list))+' files')




#%%
import shutil
final_path = r"C:\Users\UAB\data\Mayo\Original\issues solved"
for i in range(len(ROI_list)):
    file = ROI_list[i]
    strPath = os.path.realpath(file)
    nmFolders = strPath.split( os.path.sep )
    name = nmFolders[-1]
    pt_num = nmFolders[-3][3:]
    folder = nmFolders[-2]
    if folder.endswith('a'):
        yr = str(0)
    elif folder.endswith('c'):
        yr = str(1)
    elif folder.endswith('g'):
        yr = str(2)
    elif folder.endswith('j'):
        yr = str(3)
    else:
        yr = 'NA'
    new_filename = str(pt_num +' ' + yr +' ' + name[49:])
    new_file = str(final_path + '\\'+new_filename)
    shutil.copy(file, new_file)
    #os.rename(file, os.path.join(final_path, new_filename))
    
#%%
raw_path = r'C:\Users\UAB\data\Mayo\Original\Issues\Pt 359308\Pt 359308\dciaca'
patient_folders = []
pt_fnames = []


for root, dirs, files in os.walk(os.path.normpath(raw_path), topdown=True):
    for name in files:
        #print(os.path.join(root, name))
        pt_fnames.append(os.path.join(root, name))
print('\nPatient Folders have been identified\n')

ROI_list = []
for j in range(len(pt_fnames)):
    ROI_name = 'ROI'
    filename = os.path.basename(pt_fnames[j])
    if ROI_name in filename:
        ROI_list.append(pt_fnames[j])
print('\nFilenames have been found and added\n')
print('copied and moved '+ str(len(ROI_list))+' files')
#%%
import shutil
final_path = r"C:\Users\UAB\data\Mayo\Original\Issues\Pt 359308\solved"
for i in range(len(ROI_list)):
    file = ROI_list[i]
    strPath = os.path.realpath(file)
    nmFolders = strPath.split( os.path.sep )
    name = nmFolders[-1]
    pt_num = nmFolders[-3][3:]
    folder = nmFolders[-2]
    if folder.endswith('a'):
        yr = str(0)
    elif folder.endswith('c'):
        yr = str(1)
    elif folder.endswith('g'):
        yr = str(2)
    elif folder.endswith('j'):
        yr = str(3)
    else:
        yr = 'NA'
    new_filename = str(pt_num +' ' + yr +' ' + name[49:])
    new_file = str(final_path + '\\'+new_filename)
    shutil.copy(file, new_file)
    #os.rename(file, os.path.join(final_path, new_filename))

#%%

strPath = os.path.realpath(file)
print( f"Full Path    :{strPath}" )
nmFolders = strPath.split( os.path.sep )
print( "List of Folders:", nmFolders )
print( f"Program Name :{nmFolders[-1]}" )
print( f"Folder Name  :{nmFolders[-2]}" )
print( f"Folder Parent:{nmFolders[-3]}" )

#%%
path = r'C:\Users\UAB\data\Mayo\Original\Issues\Pt 359308\Pt 359308\dciacj'
patient_folders = []
pt_fnames = []


for root, dirs, files in os.walk(os.path.normpath(path), topdown=True):
    for name in files:
        #print(os.path.join(root, name))
        pt_fnames.append(os.path.join(root, name))
print('\nPatient Folders have been identified\n')

ROI_list = []
for j in range(len(pt_fnames)):
    ROI_name = 'ROI'
    filename = os.path.basename(pt_fnames[j])
    if ROI_name in filename:
        ROI_list.append(pt_fnames[j])
print('\nFilenames have been found and added\n')
print('copied and moved '+ str(len(ROI_list))+' files')

#%%
import shutil
final_path = r"C:\Users\UAB\data\Mayo\Original\Issues\Pt 359308\solved"
for i in range(len(ROI_list)):
    file = ROI_list[i]
    strPath = os.path.realpath(file)
    nmFolders = strPath.split( os.path.sep )
    name = nmFolders[-1]
    pt_num = nmFolders[-3][3:]
    folder = nmFolders[-2]
    if folder.endswith('a'):
        yr = str(0)
    elif folder.endswith('c'):
        yr = str(1)
    elif folder.endswith('g'):
        yr = str(2)
    elif folder.endswith('j'):
        yr = str(3)
    else:
        yr = 'NA'
    new_filename = str(pt_num +' ' + yr +' ' + name[21:])
    new_file = str(final_path + '\\'+new_filename)
    shutil.copy(file, new_file)
    #os.rename(file, os.path.join(final_path, new_filename))
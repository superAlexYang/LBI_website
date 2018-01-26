import csv
import os
import glob
import options
import time

Group_1CSV = 'Group_1.csv'

def retrieveFieldNames(group_num):
    if group_num == 'Group_1':
        OPTS = options.GROUP_1
    fieldnames = list()
    fieldnames.append('image_name')
    for key in OPTS.keys():
        for value in OPTS[key]:
            name = key + "-" + value
            fieldnames.append(name)
    return fieldnames

def writeNewRow(data, group_num):
    if group_num == 'Group_1':
        CSVPATH = Group_1CSV
    file_exists = os.path.isfile(CSVPATH)
    with open(CSVPATH, 'a', newline='') as csvfile:
        dataWriter = csv.DictWriter(csvfile, fieldnames=retrieveFieldNames(group_num), restval=0, lineterminator='\n')
        if not file_exists:
            dataWriter.writeheader()  
        dataWriter.writerow(data)

def isFileLabelled(filename, CSVPATH):
    with open(CSVPATH, newline='') as csvfile:
        my_content = csv.reader(csvfile, delimiter=',')
        is_labelled = False

        for row in my_content:
            if filename == row[0]:
                is_labelled = True
                return True
        if not is_labelled:
            return False

def getImagesLabellingList(group_num):
    images_file_list = []
    if group_num == 'Group_1':
        CSVPATH = Group_1CSV
    path = 'static/Pics/'
    if os.path.isfile(CSVPATH):
        for filename in sorted(glob.glob(path+'*.jpg')): 
            if not isFileLabelled(filename, CSVPATH):
                images_file_list.append(filename)
    else:
        for filename in sorted(glob.glob(path+'*.jpg')): 
            images_file_list.append(filename)
    return images_file_list

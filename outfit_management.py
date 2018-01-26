import csv
import os
import glob
import options
import time
import file_management as fm
from collections import OrderedDict

READ_CSVPATH = 'read.csv'
WRITE_CSVPATH = 'write.csv'
IMAGEPATH = 'static/Pics/'


read_fieldnames=['image_name', 'gender-male','gender-female','gender-unknown', 'score']
new_fieldnames={'gender-unknown':'unknown'}


def writeNewRow(data, clothing_type):
    file_exists = os.path.isfile(WRITE_CSVPATH)
    with open(WRITE_CSVPATH, 'a', newline='') as csvfile:
        dataWriter = csv.DictWriter(csvfile, fieldnames=fm.retrieveFieldNames(clothing_type), restval=0, lineterminator='\n')
        if not file_exists:
            dataWriter.writeheader()
        dataWriter.writerow(data)

def retrieveImageData(filename, csvpath):
    with open(csvpath, newline='') as csvfile:
        my_content = csv.reader(csvfile, delimiter=',')
        for row in my_content:
            if filename == row[0]:
                data = dict()
                for i in range(len(row)):
                    if read_fieldnames[i] in new_fieldnames:
                        data[new_fieldnames[read_fieldnames[i]]] = row[i]
                    else:
                        data[read_fieldnames[i]] = row[i]
                print(data)
                return data
        return None

def isFileLabelled(filename, CSVPATH):
    if os.path.isfile(CSVPATH):
        with open(CSVPATH, newline='') as csvfile:
            my_content = csv.reader(csvfile, delimiter=',')
            is_labelled = False

            for row in my_content:
                if filename == row[0]:
                    is_labelled = True
                    return True
            if not is_labelled:
                return False
    else:
        return False

def getImagesLabellingList():
    images_data_list = []
    if os.path.isfile(READ_CSVPATH):
        for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): 
             basename = (os.path.basename(filename))
             if not isFileLabelled(basename, WRITE_CSVPATH):
                 print(basename)
                 image_data = retrieveImageData(basename, READ_CSVPATH)
                 if image_data:
                    images_data_list.append(image_data)
    else:
        if os.path.isfile(WRITE_CSVPATH):
            for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): 
                basename = (os.path.basename(filename))
                if not isFileLabelled(basename, WRITE_CSVPATH):
                    images_data_list.append({'image_name': basename})
        else:
            for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): 
                images_data_list.append({'image_name': os.path.basename(filename)})
    return images_data_list

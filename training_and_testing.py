import numpy as np
import tifffile as tiff
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import os
from numpy import *
from tqdm import tqdm
import cv2


#file path
FILE_2015 = './IAC_data/dataset/nmirror/'
FILE_2017 = './IAC_data/dataset/17nmirror/'
FILE_cadastral2015 = './IAC_data/dataset/tag_nmirror/'

imname = "quickbird2017_subset_"
imtag = "tag_cadastral2015_subset_"
# 0: g  1: r 2: b 3: ir

testing = "testing_"
training = "training_"

testing_savepath = "./data_building/testing/image_2/"
trainging_image_savepath = "./data_building/training/image_2/"
trainging_tag_savepath = "./data_building/training/gt_image_2/"

test_txt = open("./data_building/testing.txt","w+")
train_txt = open("./data_building/train3.txt","w+")
val_txt = open("./data_building/val3.txt","w+")
str_test_txt = ""
str_train_txt=""
str_val_txt = ""
saveimname = "um_"
saveimname2 = "um_building_"

type_of_image = ".png"
cout = 0
testnum = 0
lists = [listim for listim in os.listdir(FILE_2015)]

for num in tqdm(range(len(lists))):
    tmp = lists[num].split("_")
    i = tmp[2]
    j = tmp[3]
    if int(i) > 500 and int(i) < 4500 and int(j) > 4000 and int(j) < 12000:
        tp = './IAC_data/dataset/tag_nmirror/tag_cadastral2015_subset_'
        imtag = cv2.imread(tp + str(i) + "_" + str(j) + "_.png")
        imtag = imtag * 255
        if sum(sum(imtag)) > 50:
            im2015 = cv2.imread(FILE_2015 + lists[num])
            im2017 = cv2.imread(FILE_2017 + imname + str(i) + "_" + str(j) + "_.png")
            testing_file = np.hstack((im2015, im2017))
            if cout <= 2000:
                cv2.imwrite(trainging_image_savepath + saveimname + str(cout) + type_of_image, testing_file)
                str_train_txt = str_train_txt + trainging_image_savepath + saveimname + str(cout) + type_of_image + "\t"
                cv2.imwrite(trainging_tag_savepath + saveimname2 + str(cout) + type_of_image, imtag)
                str_train_txt = str_train_txt + trainging_tag_savepath + saveimname2 + str(cout) + type_of_image + "\n"
            if cout > 2000 and cout <= 3000:
                cv2.imwrite(testing_savepath + saveimname + str(cout) + type_of_image, testing_file)
                str_test_txt = str_test_txt + testing_savepath + saveimname + str(cout) + type_of_image + "\n"
            if cout > 3000:
                break
            cout = cout + 1

            # if cout > 4000 and cout <= 6000:
            #     cv2.imwrite(trainging_image_savepath + saveimname + str(cout) + type_of_image, testing_file)
            #     val_txt = val_txt + trainging_image_savepath + saveimname + str(cout) + type_of_image + "\t"
            #     cv2.imwrite(trainging_tag_savepath + saveimname2 + str(cout) + type_of_image, imtag)
            #     val_txt = val_txt + trainging_tag_savepath + saveimname2 + str(cout) + type_of_image + "\n"


test_txt.write(str_test_txt)
train_txt.write(str_train_txt)
# val_txt.write(str_val_txt)
test_txt.close()
train_txt.close()
print("Dataset create successfully!")



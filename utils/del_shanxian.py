import pandas as pd
import numpy as np
import cv2
import os, shutil
import matplotlib.pyplot as plt
import scipy.signal as ss
import utils.shanxian_utils as su

def del_shanxian(img):
    img = img*(np.mean(img)/np.mean(img,axis = 0))
    img = np.clip(img,0,255)
    img = np.uint8(img)
    img_fill = img.copy()
    shanxians = su.find_shanxian_row(img)[1]
    h,w = img.shape
    img_bool = np.zeros((h,w))
    for s in shanxians:
        img_bool[s-8:s+8] = 255
 
    img_bool = np.uint8(img_bool)
    img_fill = cv2.inpaint(img,img_bool,5,cv2.INPAINT_NS)
    #img_fill = img_fill*(np.mean(img_fill)/np.mean(img_fill,axis = 0))
    return img_fill
# -*- coding:utf-8 -*-
# 准备两个基础方法
import cv2
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from skimage import measure,color
from scipy.signal import argrelmax
import sys
sys.path.append('/home/inn/EL_temp')

import utils.grid_cut_utils as cut
import utils.shanxian_utils as su
from utils.del_shanxian import *

from matplotlib.pyplot import subplot as sb
from matplotlib.pyplot import imshow as sh


from utils.shanxian_utils import find_shanxian_row

from  collections import Counter
from scipy.spatial import distance as dist



    
def simple_cut( img_data):
    img = cv2.cvtColor(img_data, cv2.COLOR_BGR2GRAY)
    h,w = img.shape
    thres,img2 = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
    index = np.where(img2 == 255)
    ymin , xmin = np.min(index,axis = 1)
    ymax , xmax = np.max(index,axis = 1)
    r_sum = np.sum(img2,axis = 1)
    ymax_t = np.where(r_sum>.3*255*img.shape[1])[0]
    ymax_t = ymax_t[-1] if len(ymax_t)>0 else ymax
    newimg = img_data[ymin:ymax_t,xmin:xmax,:]
    return newimg

def index_big2small(zujian_img, row, col, xyxy_list):
    x1, y1, x2, y2 = xyxy_list
    h, w = zujian_img.shape
    cols, rows = cut.get_cut_line(zujian_img, num_hor_pieces = 12,num_ver_pieces = 6, auto_fix = 'jk_cengqian')
    rows = rows - rows[0]
    cols = cols - cols[0]
    left_bound = cols[col-1]
    top_bound = rows[row-1]
    right_bound = cols[col]
    down_bound = rows[row]
    xmin = max(0, x1 - left_bound)
    xmax = min(max(0, x2 - left_bound), w)
    ymin = max(0, y1 - top_bound)
    ymax = min(max(0, y2 - top_bound), h)
    
    return [xmin, ymin, xmax, ymax]



def getSubimgInfo(i,data):
    file = data.name[i] + '0x' +str( data.row[i] -1) + '_0x' +str( data.column[i]-1  ) + '.jpg'
    xmin,ymin,xmax,ymax = np.array(eval(data.coord[i])).astype(int)
    orgfile =  data.name[i] + '.jpg'
    orgimg = simple_cut(cv2.imread('./testset1/' + orgfile))
    subimg = cv2.imread('../img/testset/testset-newcut/' + file,0)
  
    orgimg = cv2.imread('./testset1/' + orgfile,0)
    xmin,ymin,xmax,ymax = np.array(eval(data.coord[i])).astype(int)
    xmin,ymin,xmax,ymax = index_big2small(orgimg,  data.row[i]  ,  data.column[i] , [xmin,ymin,xmax,ymax])
    
   
    return subimg,[xmin,ymin,xmax,ymax]


def get_coord(rps,label,option = 1):
    min_row, min_col, max_row, max_col = rps[label-1].bbox
    if option == 1:
        x1,y1 = min_col,min_row
        x2,y2 = max_col,max_row
    else:
        # 右上x1,y1，左下x2,y2
        x1,y1 = max_col,min_row
        x2,y2 = min_col,max_row
        
    return x1,y1,x2,y2


def relative_coord(x1,y1,x2,y2,w,h):
        # bbox 左上，右下
        return 'left' if x1/w < (1-x2/w) else 'right'

def rectContains(rect,pt):
     # bbox 左上，右下
    logic = rect[0] < pt[0] < rect[0]+rect[2] and rect[1] < pt[1] < rect[1]+rect[3]
    return logic

def getYinlieInfo(subimg,bx,verbose = True):
    del_img = del_shanxian(subimg)

    # get shanxian
    shanxian = del_img[ymin:ymax,xmin:xmax]
    #     print(shanxian.shape)

    size =int( 0.1* min(shanxian.shape[:2]) )
    w,h = shanxian.shape[:2]

    kernel1 = np.diag([1.0]*size) / size
    kernel2 = np.flip(kernel1,1)
    if w < h:

        kernel1 = cv2.resize(kernel1,(max(1,int(w * 1.0 *size/ h )),size))
        kernel2 = cv2.resize(kernel2,(max(1,int(w * 1.0 *size/ h )),size))

    else:
        kernel1 = cv2.resize(kernel1,(size,max(1,int(w * 1.0 *size/ h ))))
        kernel2 = cv2.resize(kernel2,(size,max(1,int(w * 1.0 *size/ h ))))      

    kernel1 = kernel1 / kernel1.sum()
    kernel2 = kernel2 / kernel2.sum()


    # get 2 blur
    blur1 = cv2.filter2D(shanxian,-1,kernel1)
    blur2 = cv2.filter2D(shanxian,-1,kernel2)


    if max( (w * 1.0 / h ) , (h * 1.0 / w )) > 1.75:
        shanxian_c = shanxian.copy()
        k  = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        #shanxian_c = cv2.morphologyEx(shanxian_c,cv2.MORPH_CLOSE,k)
        shanxian_c = cv2.dilate(shanxian_c,k)
        ret1 = ret2 =  255 -  cv2.adaptiveThreshold(shanxian_c, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 3)
    else:
        # get 2 binary image
        ret1  = 255 -  cv2.adaptiveThreshold(blur1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 3)
        ret2  = 255 -  cv2.adaptiveThreshold(blur2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 3)
    
    index_i = 0 
    labels1=measure.label(ret1,connectivity=2)
    labels2=measure.label(ret2,connectivity=2)
    labeldic1 = Counter(labels1.flatten())
    labeldic2 = Counter(labels2.flatten())
    maxArea1Dic = sorted(labeldic1.items() , key = lambda x:x[1])
    maxArea2Dic = sorted(labeldic2.items() , key = lambda x:x[1])
    rps = measure.regionprops(labels1, cache=False)
    min_row, min_col, max_row, max_col = rps[maxArea1Dic[-2][0]-1].bbox
    if maxArea1Dic[-2][1] > maxArea2Dic[-2][1] or labels1[min_row][min_col] != 0 :
    #if maxArea1Dic[-2][1] > maxArea2Dic[-2][1]:
        # choose first
        rps = measure.regionprops(labels1, cache=False)
        aa = [r.area for r in rps]
        #tuple 
        index = [maxArea1Dic[-i][0] for i in range(3,7) if maxArea1Dic[-i][1]/max(aa) >0.3]
        distance = 100000000
        max_x1,max_y1,max_x2,max_y2 = get_coord(rps,maxArea1Dic[-2][0])
        max_rel = relative_coord(max_x1,max_y1,max_x2,max_y2,h,w)
        if max_rel == 'left':
            for i in range(len(index)):
                x1,y1,x2,y2 = get_coord(rps,index[i])
                dists = dist.euclidean((max_x2,max_y2), (x1,y1))
                center_x,center_y = (x2+x1)/2,(y1+y2)/2
                #if dists < distance and x1 >= max_x2 and y1 >= max_y2:
                if dists < distance and center_x +10 >= max_x2 and center_y +10 >= max_y2:
                    distance = dists
                    index_i = index[i]

        elif max_rel == 'right':
            for i in range(len(index)):
                x1,y1,x2,y2 = get_coord(rps,index[i])
                dists = dist.euclidean((max_x1,max_y1), (x2,y2))
                center_x,center_y = (x2+x1)/2,(y1+y2)/2
                #if dists < distance and x2 <= max_x1 and y2 <= max_y1:
                if dists < distance and center_x -10 <= max_x1 and center_y -10 <= max_y1:
                    distance = dists
                    index_i = index[i]

        # draw the mask
        if index_i != 0:
            labels3 = ((labels1 == index_i)+ (labels1 == maxArea1Dic[-2][0]))
        else:
            labels3 = (labels1 == maxArea1Dic[-2][0])

    elif index_i == 0:
        # choose second
        rps = measure.regionprops(labels2, cache=False)
        aa = [r.area for r in rps]
        #tuple 
        index = [maxArea2Dic[-i][0] for i in range(3,7) if maxArea2Dic[-i][1]/max(aa) >0.3]
        distance = 100000000
        max_x1,max_y1,max_x2,max_y2 = get_coord(rps,maxArea2Dic[-2][0],2)
        max_rel = relative_coord(max_x1,max_y2,max_x2,max_y1,h,w)
        if max_rel == 'left':
            for i in range(len(index)):
                x1,y1,x2,y2 = get_coord(rps,index[i],2)
                dists = dist.euclidean((max_x1,max_y1), (x2,y2))
                center_x,center_y = (x2+x1)/2,(y1+y2)/2
                #if dists < distance and x2 >= max_x1 and y2 <= max_y1:
                if dists < distance and center_x +10 > max_x1 and center_y -10 < max_y1:
                    distance = dists
                    index_i = index[i]


        elif max_rel == 'right':
            for i in range(len(index)):
                x1,y1,x2,y2 = get_coord(rps,index[i],2)
                dists = dist.euclidean((max_x2,max_y2), (x1,y1))
                center_x,center_y = (x2+x1)/2,(y1+y2)/2
                #if dists < distance and x1 <= max_x2 and y1 >= max_y2:
                if dists < distance and center_x -10 <= max_x2 and center_y +10 >= max_y2:
                    distance = dists
                    index_i = index[i]

        # draw the mask
        if index_i != 0:
            labels3 = ((labels2 == index_i)+ (labels2 == maxArea2Dic[-2][0]))  
        else:
            labels3 = (labels2 == maxArea2Dic[-2][0])
            
    yinlieMask = np.zeros(shape = subimg.shape[:2])
    yinlieMask[ymin:ymax,xmin:xmax] = labels3
    
    if verbose == True:
        plt.imshow(del_img[ymin:ymax,xmin:xmax])
        plt.show()
        sb(1,2,1)
        sh(blur1)
        sb(1,2,2)
        sh(blur2)
        plt.show()
        sb(1,2,1)
        sh(ret1)
        sb(1,2,2)
        sh(ret2)
        plt.show()
        sh(labels3)
        plt.show()

            
    return yinlieMask, shanxian, labels3

def getHandianInfo(subimg,yinlieMask,verbose = True):
    # 生成栅线Mask
    shanxians = find_shanxian_row(subimg)[1]
    seg = [0,40,70,90,70,95,70 , 90 , 70 , 40] 
    seg = np.uint32(np.cumsum(seg) * subimg.shape[1] / 635)
    seg = seg[1:-1]
    
    shanxianmask_show = np.zeros(subimg.shape)
    totalCover = []
    for shanxian in shanxians:
        for interval in range(0,len(seg),2):
            shanxianmask_show[ shanxian - 5 : shanxian + 6 ,seg[interval] : seg[interval+1]] = 1
            shanxianmask = np.zeros(subimg.shape)
            shanxianmask[ shanxian - 5 : shanxian + 6 ,seg[interval] : seg[interval+1]] = 1
            pixels = (yinlieMask * shanxianmask > 0 ).sum()
            totalCover.append(pixels)

    if verbose == True:
        sb(1,3,1)
        plt.imshow(shanxianmask_show)
        sb(1,3,2)
        plt.imshow(yinlieMask)
        sb(1,3,3)
        shs = shanxianmask_show * 0.5 + yinlieMask
        plt.imshow(shs,'gray')
        plt.show()

    return shanxianmask_show, totalCover

def getEdgeInfo(subimg,yinlieMask,verbose = True):    
    # edgeMask
    edgeMask = np.zeros(subimg.shape)
    band = int(subimg.shape[0]*(20.0 / 630) )
    crossEdge = []
    edgeMask[:band,:] = 1
    crossEdge.append(np.sum((edgeMask * yinlieMask) > 0))

    edgeMask = np.zeros(subimg.shape)
    edgeMask[-band:,:] = 1
    crossEdge.append(np.sum((edgeMask * yinlieMask) > 0))

    edgeMask = np.zeros(subimg.shape)
    edgeMask[:,:band] = 1
    crossEdge.append(np.sum((edgeMask * yinlieMask) > 0))

    edgeMask = np.zeros(subimg.shape)
    edgeMask[:,-band:] = 1
    crossEdge.append(np.sum((edgeMask * yinlieMask) > 0))

    if verbose == True:
        plt.imshow(crossEdge)
        plt.show()

    return crossEdge
    
    
def getConvexDefectInfo(shanxian, subimg_mask, verbose=True):
    subimg_mask = subimg_mask.astype(np.int16)
#     # 根据长宽比旋转图片
#     transpose_tag = False
#     if subimg_mask.shape[0] / subimg_mask.shape[1] > 1:
#         transpose_tag = True
#         subimg_mask = subimg_mask.transpose()
#         shanxian = shanxian.transpose()
    
    # cv2方法
    yinlie = subimg_mask.copy()
    yinlie = np.uint8(yinlie)
    h, w = subimg_mask.shape
    yinlie = np.uint8(yinlie*255)
    img, contours, hierarchy = cv2.findContours(yinlie, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
    
    # 画出轮廓
    painter = np.uint8(np.ones((h, w))) 
    cv2.drawContours(painter,contours,-1,(0,0,255),1)
    
    # 画出凸包
    hull = cv2.convexHull(contours[0])
    cv2.drawContours(painter,[hull],-1,(0,255,0),1)
    
    # 计算凸包面积，轮廓面积，轮廓凸包面积比
    contour_area = cv2.contourArea(contours[0])
    hull_area = cv2.contourArea(hull)
    solidity = contour_area / hull_area    
     
    # 计算距离
    hull_on_contour = cv2.convexHull(contours[0], returnPoints = False)
    defects = cv2.convexityDefects(contours[0], hull_on_contour)
    depth = defects[:, 0, 3]
    
    # 计算旋转角度，确定隐裂走向
    (center_x, center_y), (w, h), angle = cv2.minAreaRect(contours[0])
    if w / h > 1:
        if -30 <= angle <= 0:
            trend = 'left_to_right'
        elif -60 <= angle < 30:
            trend = 'leftdown_to_rightup'
        else:
            trend = 'down_to_up'
    else:
        if -30 <= angle <= 0:
            trend = 'down_to_up'
        elif -60 <= angle < 30:
            trend = 'leftup_to_rightdown'
        else:
            trend = 'left_to_right'  
        
    # 距离变换
    dt = cv2.distanceTransform(subimg_mask.astype(np.uint8), 1, 5)

    # 提取骨架skeleton坐标
    row, col = argrelmax(dt)
    loc = np.array(list(zip(row, col)))
    
    # 拟合直线
    [vx, vy, x, y] = cv2.fitLine(np.float32(contours[0]), cv2.DIST_L2, 0, 0.01, 0.01)
    
    # 计算骨架偏离直线的平均距离
    try:
        average_diviation_l1 = np.sum(np.abs(vx*(loc[:, 0]-y)-vy*(loc[:, 1]-x)))/len(loc)
        average_diviation_l2 = np.sum(np.power(vx*(loc[:, 0]-y)-vy*(loc[:, 1]-x), 2))/len(loc)     
    except:
        average_diviation_l1 = 0
        average_diviation_l2 = 0
    
    # 显示
    if verbose:
        print('contour area: {}, hull area: {}, solidity: {}'.format(contour_area, hull_area, solidity))
        print('depth: {}'.format(depth))
        print('rotate angle: {}, trend: {}'.format(angle, trend))
        print("vx: {}; vy: {}; x: {}; y: {}".format(vx, vy, x, y))
        rows,cols = shanxian.shape[:2]
        lefty=int(-(x*vy/vx)+y)
        righty=int(((cols-x)*vy/vx)+y)
        print('righty: {}, lefty: {}'.format(righty, lefty))
        print('average diviation: {}'.format(average_diviation))
        skeleton_with_line = np.uint8(np.ones(dt.shape))
        skeleton_with_line[loc[:, 0], loc[:, 1]] = 255
        img = cv2.line(skeleton_with_line,(cols-1,righty),(0,lefty),(255,255,255),1)
        sb(2,2,1)
        sh(shanxian)
        sb(2,2,2)
        sh(painter)
        sb(2,2,3)
        sh(dt)
        sb(2,2,4)
        sh(img)
        plt.show()
    
    return depth, contour_area, hull_area, solidity, angle, trend, average_diviation_l1, average_diviation_l2




def getSkeletonInfo(labels3):
    dis = cv2.distanceTransform(labels3.astype(np.uint8),1,5)
    # 加随机扰动
    dis += 0.001 * np.random.rand(dis.shape[0] * dis.shape[1]).reshape(dis.shape)
    dis *= labels3
    # 对每行做argregmax
    argm = argrelmax(dis,order = 5)
    dis_d = np.zeros(shape = dis.shape)
    dis_d[list(argm[0]),list(argm[1])] = 1

    beckbone = (dis_d * dis) > 0 
    beckbone_dis = dis_d * dis
    return beckbone ,beckbone_dis ,dis
    


def getCuxiInfo(labels3):
    beckbone ,beckbone_dis ,dis = getSkeletonInfo(labels3)      
    estimate_10 = np.percentile(beckbone_dis[beckbone_dis!=0],15)
    estimate_25 = np.percentile(beckbone_dis[beckbone_dis!=0],25)
    estimate_50 = np.percentile(beckbone_dis[beckbone_dis!=0],50)
    estimate_75 = np.percentile(beckbone_dis[beckbone_dis!=0],75)
    estimate_90 = np.percentile(beckbone_dis[beckbone_dis!=0],90)
    estimate_10_ratio = estimate_10 / max(labels3.shape)
    estimate_25_ratio = estimate_25 / max(labels3.shape)
    estimate_50_ratio = estimate_50 / max(labels3.shape)
    estimate_75_ratio = estimate_75 / max(labels3.shape)
    estimate_90_ratio = estimate_90 / max(labels3.shape)
    return [estimate_10,estimate_25,estimate_50,estimate_75,estimate_90,\
            estimate_10_ratio,estimate_25_ratio,estimate_50_ratio,estimate_75_ratio,estimate_90_ratio]

def getColorFeature(yinlieMask,sub_del_img,labels3):
    """
    计算图片深度信息。返回一个字典
    """
    
    # 计算骨架
    w , h = labels3.shape[:2]
    beckbone = cv2.distanceTransform(labels3.astype(np.uint8),1,5)
    beckbone_c = np.zeros(shape = (beckbone.shape))
    # 行大于列 ， 统计每行上的最大值的位置
    if w > h :
        for row in range(np.argwhere((labels3.sum(1)>0) == 1).min(),np.argwhere((labels3.sum(1)>0) == 1).max()):
            plc = np.argmax(beckbone[row,:])
            beckbone_c[row,plc] = 1
    else:
        for col in range(np.argwhere((labels3.sum(0)>0) == 1).min(),np.argwhere((labels3.sum(0)>0) == 1).max()):
            plc = np.argmax(beckbone[:,col])
            beckbone_c[plc,col] = 1
    
    # 写入信息    
    colorFeature = {}
    
    
    # 乘上labels3
    yinlie_pixl = sub_del_img * labels3
    yinlie_pixl_not_zero = yinlie_pixl[yinlie_pixl > 0]
    colorFeature["mean"] = np.mean(yinlie_pixl)
    colorFeature["std"] = np.std(yinlie_pixl_not_zero)
    colorFeature["skew"] = pd.Series(yinlie_pixl_not_zero.flatten()).skew()
    colorFeature["kurt"] = pd.Series(yinlie_pixl_not_zero.flatten()).kurt()
    colorFeature["15_per"] = np.percentile(yinlie_pixl_not_zero, q = 15)
    colorFeature["25_per"] = np.percentile(yinlie_pixl_not_zero, q = 25)
    colorFeature["50_per"] = np.percentile(yinlie_pixl_not_zero, q = 50)
    colorFeature["75_per"] = np.percentile(yinlie_pixl_not_zero, q = 75)
    colorFeature["85_per"] = np.percentile(yinlie_pixl_not_zero, q = 85)
    colorFeature["95_per"] = np.percentile(yinlie_pixl_not_zero, q = 95)
    
    # 乘上skeleton
    yinlie_skeleton = sub_del_img * beckbone_c
    yinlie_skeleton_not_zero = yinlie_skeleton[yinlie_skeleton > 0]
    
    colorFeature["ske_mean"] = np.mean(yinlie_skeleton)
    colorFeature["ske_std"] = np.std(yinlie_skeleton_not_zero)
    colorFeature["ske_skew"] = pd.Series(yinlie_skeleton_not_zero.flatten()).skew()
    colorFeature["ske_kurt"] = pd.Series(yinlie_skeleton_not_zero.flatten()).kurt()
    colorFeature["ske_15_per"] = np.percentile(yinlie_skeleton_not_zero, q = 15)
    colorFeature["ske_25_per"] = np.percentile(yinlie_skeleton_not_zero, q = 25)
    colorFeature["ske_50_per"] = np.percentile(yinlie_skeleton_not_zero, q = 50)
    colorFeature["ske_75_per"] = np.percentile(yinlie_skeleton_not_zero, q = 75)
    colorFeature["ske_85_per"] = np.percentile(yinlie_skeleton_not_zero, q = 85)
    colorFeature["ske_95_per"] = np.percentile(yinlie_skeleton_not_zero, q = 95)
    
    # 对背景的处理
    sub_del_img_flat = sub_del_img.flatten()
    colorFeature["subimg_mean"] = np.mean(sub_del_img_flat)
    colorFeature["subimg_tmean"] = stats.trim_mean(sub_del_img_flat, proportiontocut= 0.15)
    colorFeature["subimg_std"] = np.std(sub_del_img_flat)
    colorFeature["subimg_tstd"] = stats.tstd(sub_del_img_flat, 
                                            limits = (np.percentile(sub_del_img_flat, q = 15), np.percentile(sub_del_img_flat, q = 85)))
    colorFeature["subimg_15_per"] = np.percentile(sub_del_img_flat, q = 15)
    colorFeature["subimg_25_per"] = np.percentile(sub_del_img_flat, q = 25)
    colorFeature["subimg_50_per"] = np.percentile(sub_del_img_flat, q = 50)
    colorFeature["subimg_75_per"] = np.percentile(sub_del_img_flat, q = 75)
    colorFeature["subimg_85_per"] = np.percentile(sub_del_img_flat, q = 85)
    
    # 去掉mask部分的小背景部分的处理
    backgroud = (labels3 == False)
    bg_flat = (sub_del_img * backgroud).flatten()
    
    colorFeature["bg_mean"] = np.mean(bg_flat)
    colorFeature["bg_tmean"] = stats.trim_mean(bg_flat, proportiontocut= 0.15)
    colorFeature["bg_std"] = np.std(bg_flat)
    colorFeature["bg_tstd"] = stats.tstd(bg_flat, 
                                            limits = (np.percentile(bg_flat, q = 15), np.percentile(bg_flat, q = 85)))
    colorFeature["bg_15_per"] = np.percentile(bg_flat, q = 15)
    colorFeature["bg_25_per"] = np.percentile(bg_flat, q = 25)
    colorFeature["bg_50_per"] = np.percentile(bg_flat, q = 50)
    colorFeature["bg_75_per"] = np.percentile(bg_flat, q = 75)
    colorFeature["bg_85_per"] = np.percentile(bg_flat, q = 85)
    
    
    return colorFeature



#res = []
#from tqdm import tqdm
#testset = data_falseyinlie
#for  i in range(testset.shape[0]):
#    file = data.name[i] + '0x' +str( data.row[i] -1) + '_0x' +str( #data.column[i]-1  ) + '.jpg'
#    subimg , bx = getSubimgInfo(i,testset)
#    a, b , c = getYinlie(subimg,bx,verbose = False)
##     print(i,file,c)
#    res.append((file,c))
#    if sum(c) == 0:
#        print(i ,file ,c)
#import pickle
#with open('res_n.pkl','wb') as f:
#    pickle.dump(res,f) 
#pd.DataFrame([ (i[0],sum(i[1])>0) for i in res])[1].value_counts()


#data = pd.read_csv('./1w1-result-1015.csv')

#thres = 0.9
#data = data[data.prob > thres]

#ans = pd.read_csv('./answer.csv')
#ans = ans[ans.type == 'yinlie']

#data.loc[:,'imginfo'] = data.name + data.row.astype(str) + #data.column.astype(str)
#ans.loc[:,'imginfo'] = ans.name + ans.row.astype(str) + #ans.column.astype(str)

#data_trueyinlie = #data[data.imginfo.isin(np.unique(ans.imginfo))].reset_index()
#data_falseyinlie = data[~data.imginfo.isin(np.unique(ans.imginfo))].reset_index()


#ans.loc[:,'filename'] = ans.name+ '0x' + (ans.row -1).astype(str) + '_0x' + (ans.column-1  ).astype(str) + '.jpg'
#data_trueyinlie.loc[:,'filename'] = data_trueyinlie.name+ '0x' +(data_trueyinlie.row -1).astype(str) + '_0x' +( data_trueyinlie.column -1  ).astype(str) + '.jpg'
#data_falseyinlie.loc[:,'filename'] =data_falseyinlie.name+ '0x' +(data_falseyinlie.row-1).astype(str) + '_0x' +( data_falseyinlie.column -1  ).astype(str) + '.jpg'
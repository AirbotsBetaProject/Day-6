
import urllib

import cv2

import numpy as np

import os

def store_raw_images():
    pos_gun_images_link ='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03470629'
    #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n06616216'
    try :
        pos_gun_image_urls = urllib.urlopen(pos_gun_images_link).read().decode()# openinf the url,reading and #
    except Exception as e:
        print e

    if not os.path.exists('pos_gun'):
        os.makedirs('pos_gun')

    pic_num = 125

    for i in pos_gun_image_urls.split('\n'):# split the url into line
        try:# lot of them goint to fail except such exception
            print(i)
            urllib.urlretrieve(i, "pos_gun/" +str(pic_num)+'.jpg')# store raw into directory
            img = cv2.imread("pos_gun/" +str(pic_num)+'.jpg',
                             cv2.IMREAD_GRAYSCALE)# read and convert into grey scale
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("pos_gun/" +str(pic_num)+'.jpg', resized_image)# save the resized image
            pic_num += 1

        except Exception as e:
            print(str(e))


def find_uglies():
    for file_type in ['pos_gun']:
        for img in os .listdir(file_type):
            for ugly in os.listdir('uglies'):# iterating through all the image
             try:
                 
                current_image_path = str(file_type)+'/'+str(img)# current image
                ugly = cv2.imread('uglies/' +str(ugly))# load ugly image
                question = cv2.imread(current_image_path)
            
                if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                  print('ugly_image')# if image are of same shape and are identical image
                  print(current_image_path)
                  os.remove(current_image_path)# remove current ugly image


             except Exception as e:
                print(str(e))


find_uglies()
#store_raw_images()

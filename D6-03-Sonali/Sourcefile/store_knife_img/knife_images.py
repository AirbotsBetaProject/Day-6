 
import urllib

import cv2

import numpy as np

import os

def store_raw_images():
    pos_knife_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03327691'#open url
    pos_knife_image_urls = urllib.urlopen(pos_knife_images_link).read().decode()#open and read the url
    
    if not os.path.exists('pos_knife'):#create a new directory if not present
        os.makedirs('pos_knife')

    pic_num = 1

    for i in pos_knife_image_urls.split('\n'):#split the url into line
        try:#lot of them goint to fail except such exception
            print(i)
            urllib.urlretrieve(i, "pos_gun/" +str(pic_num)+'.jpg')#store raw into directory
            img = cv2.imread("pos_gun/" +str(pic_num)+'.jpg',
                             cv2.IMREAD_GRAYSCALE)#read and convert into grey scale
            resized_image = cv2.resize(img, (100,100))#resize
            cv2.imwrite("pos_gun/" +str(pic_num)+'.jpg', resized_image)#save the resized image
            pic_num += 1

        except Exception as e:
            print(str(e))


def find_uglies():
    for file_type in ['pos_knife']:
        for img in os .listdir(file_type):#iterating through all the image
            for ugly in os.listdir('uglies'):
             try:
                 
                current_image_path = str(file_type)+'/'+str(img)#current image
                ugly = cv2.imread('uglies/' +str(ugly))#load ugly image
                question = cv2.imread(current_image_path)#read current image path
            
                if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):#if image are of same shape and are identical image
                  print('ugly_image')
                  print(current_image_path)
                  os.remove(current_image_path)#remove current ugly image 


             except Exception as e:
                print(str(e))
            


find_uglies()
#store_raw_images()

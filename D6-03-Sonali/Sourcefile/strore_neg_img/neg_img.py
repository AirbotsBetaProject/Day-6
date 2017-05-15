import urllib

import cv2

import numpy as np

import os


def store_raw_images():  # defining store raw images
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n10678937'
    #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n10793799'
    #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09996481'
    #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n10678937' #assigning link
    neg_image_urls = urllib.urlopen(neg_images_link).read(
    ).decode()  # openinf the url,reading and #

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 1

    for i in neg_image_urls.split('\n'):  # split the url into line
        try:  # lot of them goint to fail except such exception
            print(i)
            # store raw into directory
            urllib.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg',
                             cv2.IMREAD_GRAYSCALE)  # read and convert into grey scale
            resized_image = cv2.resize(img, (100, 100))
            # save the resized image
            cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))


def find_uglies():
    for file_type in ['neg']:
        for img in os .listdir(file_type):  # iterating through all the image
            for ugly in os.listdir('uglies'):
                try:

                    current_image_path = str(
                        file_type)+'/'+str(img)  # current image
                    ugly = cv2.imread('uglies/' + str(ugly))  # load ugly image
                    # read current image path
                    question = cv2.imread(current_image_path)

                    # if image are of same shape and are identical image
                    if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                        print('ugly_image')
                        print(current_image_path)
                        # remove current ugly image
                        os.remove(current_image_path)

                except Exception as e:
                    prit(str(e))



find_uglies()
# store_raw_images()

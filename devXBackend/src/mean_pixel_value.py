import cv2
from PIL import Image
import numpy
import os

# test_pic = Image.open('../winrar.png', 'r')
test_pic = cv2.imread('pictures/winrar.png')
#cv2.imshow('image', test_pic)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Input is gonna be an img, check if the img size is 32, 32, 3, return bgr right now.
def mean_pixel_value(img):

    if img.shape == (32, 32, 3): 

        avg_row_color = numpy.average(img, axis = 0)
        #print(avg_row_color)
        avg_color = numpy.average(avg_row_color, axis=0)
        #print(avg_color)
    else:
        print('Wrong img size')

    return avg_color

print (mean_pixel_value(test_pic))

# Input list of albums, return closest image
def closest_img(img, img_list):
    input_bgr = mean_pixel_value(img)
    closest = img_list[0]
    closest_bgr = 255
    for imgs in img_list:
        temp_bgr = mean_pixel_value(imgs)
        temp_distance = numpy.linalg.norm(input_bgr-temp_bgr)
        if temp_distance < closest_bgr:
            closest = imgs

    return closest

# Function for making list of all album files 
def make_album_list():
    album_list = []
    files = os.listdir('pictures')
    for fil in files:
        album_list.append(cv2.imread('pictures/' + fil))

    return album_list

# Values for testing functions
album_list = make_album_list()
closest_image = closest_img(test_pic, album_list)

cv2.imshow('image', closest_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(closest_img(test_pic, ))

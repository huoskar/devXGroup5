import cv2
from PIL import Image
import numpy
import os
from PIL import Image
from resizeimage import resizeimage

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

# input 512, 512, Taking 32, 32, 3 from input picture, returning list of these images.
'''
def input_to_list_of_fragments(input_img):
    iterations = input_img.shape[0] / 16
    list_of_fragments[16][16] = []
    next_pic = 0
    print(input_img)
    for y in range(0,input_img.shape[0]):
         if y % 32 == 0:
             next_pic_y =+ 1
        for x in range(0,input_img.shape[0]):
            if x % 32 == 0:
                next_pic_x =+ 1
            list_of_fragments[next_pic_x][next_pic_y] = input_img
'''
# Second try 
def input_to_list_of_fragments2(input_img):
    chunk = [32][32] * [3]
    chunks = [16][16] * chunk
    for i in range(0,16):
        for j in range(0,16):
            for x in range(0,32):
                for y in range(0,32):
                    chunk[x][y] = input_img.shape[x + i * 32][y + j * 32]
            chunks[i][j] = chunk[x][y]

    return chunks

# Main function, opacity
# Values for testing functions
album_list = make_album_list()
closest_image = closest_img(test_pic, album_list)

#cv2.imshow('image', closest_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
# print(closest_img(test_pic, ))

# Temporary old crop function
def crop_input_picture(img_name):
    with open(img_name, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [512, 512])
            #cover.save('test2-cover.jpeg', image.format)
    return cover

# Resize input file cv2 function
def resize_input_img(img):
    return cv2.resize(img, (512, 512))
# Resize album cover to 32, 32
def resize_album_img(img):
    return cv2.resize(img, (32, 32))

test_pic2 = cv2.imread('test2.jpg')
cropped_input = resize_input_img(test_pic2)
print(cropped_input)
input_to_list_of_fragments2(cropped_input)
#cv2.imshow('image', cropped_input)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

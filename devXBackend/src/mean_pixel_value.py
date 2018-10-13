import cv2
import random
import numpy as np
import os
import image_slicer
from PIL import Image

#### TODO
# Outprint a mean pixel value picture
# Fix main function when joining sliced image
# Divide input_picture to 4 or 8 smaler picture. Iterative over the joining
# Add error checks for easier development.


# Input is gonna be an img, check if the img size is 32, 32, 3, return bgr right now.
def mean_pixel_value(img):

    #if img.shape == (32, 32, 3):
    #if img is not None:
    avg_row_color = numpy.average(img, axis = 0)

    avg_color = numpy.average(avg_row_color, axis=0)
   # else:
   #    print('Wrong img size')

    return avg_color

# Input list of albums, return closest image
def closest_img(img, img_list):
    input_bgr = mean_pixel_value(img)
    closest = img_list[0]
    closest_distance = numpy.linalg.norm(input_bgr-mean_pixel_value(closest))
    for imgs in img_list:
        temp_bgr = mean_pixel_value(imgs)
        temp_distance = numpy.linalg.norm(input_bgr-temp_bgr)
        if temp_distance < closest_distance:
            closest = imgs
            closest_distance = temp_distance

    return closest

# Dict find cloesest colot
def closest_dict(dic_list, color):
    closest = dic_list[0]
    closest_distance = numpy.linalg.norm(color - closest)
    for dic_col in dic_list:
        temp_distance = numpy.linalg.norm(dic_col - color)
        if temp_distance < closest_distance:
            closest = dic_col
            closest_distance = temp_distance

    return closest

# Function for making list of all album files
def make_album_list():
    album_list = []
    files = os.listdir('chill')
    for fil in files:
        album_list.append(cv2.imread('chill/' + fil))
    return album_list

# Resize input file cv2 function, with a write, Maybe better with more pixels
def resize_input_img(img, w=512, h=512):
    resized_img = cv2.resize(img, (w, h))
    cv2.imwrite('resize_input_image.jpg',resized_img)
    return resized_img

# Resize album cover to 32, 32
def resize_album_img(img, w=32, h=32):
    return cv2.resize(img, (w, h))

# THIS FUNCTION IS NOT USED, for slicing
def input_to_fragments(img):
    os.chdir('fragments_of_inputs')
    info = image_slicer.slice(img, 256)
    print(info)

    return info
def main2():
    chill_dict = np.load('chill_dict.npy').item()
    resize_input_img(test_pic2)
    album_list = make_album_list()
    print(len(album_list)) # Number of albums availale
    big_tiles = image_slicer.slice('resize_input_image.jpg', 16)
    for big_tile in big_tiles:
        # resize_input_image.jpg
        tiles = image_slicer.slice(big_tile.filename, 8) #16 för 16,16 , annars dir 1024
        for tile in tiles:
            if tile.filename == 'resize_input_image_09_02.png': # Stop the opening
                break
            print(tile.filename)
            image = Image.open(tile.filename)
            #closest_image = closest_img(pic, album_list)
            color_pic = image.resize((1,1))
            color = np.round(np.array(color_pic)/32)
            color = tuple(color[0][0])
            if color in chill_dict.keys():
                closest_image_filenames = chill_dict[color]
                rand = random.randint(0,len(closest_image_filenames) - 1)
                closest_image_filename = closest_image_filenames[rand]
            closest_image = Image.open(closest_image_filename)
            closest_image.save(tile.filename)
            tile.image = Image.open(tile.filename) # Probably cant open more than ca 200 tiles
        final_pic = image_slicer.join(tiles)
        final_pic.save(big_tile.filename)
        big_tile.image = Image.open(big_tile.filename)
    final_ful_pic = image_slicer.join(big_tiles)
    final_ful_pic.save('result.png')

# Main function, opacity
def main():
    chill_dict = np.load('chill_dict.npy').item()
    resized_img = resize_input_img(test_pic2)
    album_list = make_album_list()
    print(len(album_list)) # Number of albums availale
    output_chunk_list = np.array((32,32))
    for x in range(0,32):
        for y in range(0,32):
            temp = resized_img[(0 + x*16):(16 + x*16),(0 + y*16):(16 + y*16)]
            color_pic = temp.resize((1,1))
            color = np.round(np.array(color_pic)/32)
            color = tuple(color[0][0])
            if color in chill_dict.keys():
                closest_image_filenames = chill_dict[color]
                rand = random.randint(0,len(closest_image_filenames) - 1)
                closest_image_filename = closest_image_filenames[rand]
            else:
               new_color = closest_dict(chill_dict.keys(), color)
               closest_image_filenames = chill_dict[new_color]
            output_chunk_list[x,y] = closest_image_filename
    #final_ful_pic.save('result.png')


# Values for testing functions
test_pic = cv2.imread('pictures/winrar.png')
test_pic2 = cv2.imread('test2.jpg')

print(os.getcwd())
main()


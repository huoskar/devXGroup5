import cv2
import numpy
import os
import image_slicer
from PIL import Image

#### TODO
# Outprint a mean pixel value picture
# Fix main function when joining sliced image
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

# Function for making list of all album files
def make_album_list():
    album_list = []
    files = os.listdir('featured')
    for fil in files:
        album_list.append(cv2.imread('featured/' + fil))
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

# Main function, opacity
def main():
    resize_input_img(test_pic2)
    album_list = make_album_list()
    print(len(album_list)) # Number of albums available
    tiles = image_slicer.slice('resize_input_image.jpg', 256) # wrong dir
    for tile in tiles:
        if tile.filename == 'resize_input_image_16_02.png': # Stop the opening
            break
        print(tile.filename)
        pic = cv2.imread(tile.filename)
        closest_image = closest_img(pic, album_list)
        cv2.imwrite(tile.filename, closest_image)
        tile.image = Image.open(tile.filename) # Probably cant open more than ca 200 tiles
    final_pic = image_slicer.join(tiles)
    final_pic.save('result.png')


# Values for testing functions
test_pic = cv2.imread('pictures/winrar.png')
test_pic2 = cv2.imread('test2.jpg')

print(os.getcwd())
main()


import cv2
from PIL import Image
import numpy
import os
import image_slicer
#from PIL import Image
#from resizeimage import resizeimage




# Input is gonna be an img, check if the img size is 32, 32, 3, return bgr right now.
def mean_pixel_value(img):

  #  if img.shape == (32, 32, 3): 
    #print(img)
    #print(type(img))
    if img is not None:
        avg_row_color = numpy.average(img, axis = 0)

        avg_color = numpy.average(avg_row_color, axis=0)
        #print(avg_color)
   # else:
   #    print('Wrong img size')

    return avg_color

# Input list of albums, return closest image
def closest_img(img, img_list):
    input_bgr = mean_pixel_value(img)
    closest = img_list[0]
    closest_bgr = 255123123
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

# Resize input file cv2 function, with a write
def resize_input_img(img):
    resized_img = cv2.resize(img, (512, 512))
    cv2.imwrite('resize_input_image.jpg',resized_img)
    return resized_img

# Resize album cover to 32, 32
def resize_album_img(img):
    return cv2.resize(img, (32, 32))

# input 512, 512, Taking 32, 32, 3 from input picture, returning list of these images.
def input_to_fragments(img):
    os.chdir('fragments_of_inputs')
    info = image_slicer.slice(img, 256)
    print(info)

    return info
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
'''

# Main function, opacity
def main():
    resize_input_img(test_pic2)
    album_list = make_album_list()
    #os.chdir('fragments_of_inputs')
    tiles = image_slicer.slice('resize_input_image.jpg', 256) # wrong dir
    #os.chdir('..')
    #pictures = os.listdir() # ändra till nuvarande.
    #print(pictures)
    #os.chdir('fragments_to_albums')
    for tile in tiles:

        #if pic.endswith('.png'):
        # Skickar in sträng, läs img
        #pic_name = pic
        if tile.filename == 'resize_input_image_16_02.png':
            break
        #if tile is not None:
        print(tile.filename)
        #print(type(tile.filename))
        pic = cv2.imread(tile.filename)
            #if tile.filename == 'resize_input_image_16_02.png':
            #print(pic)
        closest_image = closest_img(pic, album_list)
            #print(tile.filename, closest_image)
        cv2.imwrite(tile.filename, closest_image)
        tile.image = Image.open(tile.filename) # Probably cant open more than ca 200 tiles
        #tile.image.close()
    #os.chdir('..')
    final_pic = image_slicer.join(tiles)
    print(final_pic)
    #os.chdir('..')
    final_pic.save('result.png')
    #cv2.imwrite('result.png', final_pic)


# Values for testing functions
test_pic = cv2.imread('pictures/winrar.png')
test_pic2 = cv2.imread('test2.jpg')

#album_list = make_album_list()
#closest_image = closest_img(test_pic, album_list)
#cropped_input = resize_input_img(test_pic2)
print(os.getcwd())
main()

'''
print(os.getcwd())
os.chdir('fragments_of_inputs')
list_of_tiles = image_slicer.slice('../resize_input_image.jpg', 256)
pictures = os.listdir()
print(pictures)
info = image_slicer.join(list_of_tiles)
print(info)
#input_to_fragments(cropped_input)
'''

#cv2.imshow('image', closest_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

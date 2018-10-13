from PIL import Image

from resizeimage import resizeimage


with open('test2.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [512, 512])
        cover.save('test2-cover.jpeg', image.format)
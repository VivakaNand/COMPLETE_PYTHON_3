# installation of Pillow library
# change the image extension
# resize image files
# resize multiple images using for loop
# Sharpness
# Brightness
# Color
# Contrast
# Image blur, GaussianBlur

from PIL import Image, ImageEnhance, ImageFilter
import os
# img1 = Image.open('dog1.jpg')
# change extension
# img1.save('dog1.pdf')
# img1.show()

# resize image files
# 250
# MAX_SIZE = (250,250)
# img1 = Image.open('dog1.jpg')
# img1.thumbnail(MAX_SIZE)
# img1.save('dog1small.jpg')

# resize multiple images using for loop
# img1 = Image.open('dog1.jpg')
#for item in os.listdir():
#    if item.endswith('.jpg'):
#        img1 = Image.open(item)
#        img1.thumbnail(MAX_SIZE)
#        filename,extension = os.path.splitext(item)
#        img1.save(f'{filename}.png')

# Sharpness
# 0 : blurry
# 1 : original image
# 2 : image with increase sharpness
# 3 : more increase shapness
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(0).save('dog1edited.jpg')


# Brightness
# 0 : Black image
# 1 : original image
# 2 : image with increase brightness
# 3 : more increase brightness
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1).save('dog1edited.jpg')

# Color
# 0 : black and white
# 1 : original image
# 2 : image with change color
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(1).save('dog1edited.jpg')


# Contrast
# 0 : black
# 1 : original image
# 2 : image with increase contrast
# 3 : more increase contrast
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1).save('dog1edited.jpg')

# Image blur, GaussianBlur
img1 = Image.open('dog1.jpg')
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1edited.jpg')

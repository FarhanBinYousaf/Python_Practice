from email.mime import image
from PIL import Image, ImageEnhance
import os

    # ------- Sharpness ------ 
# img1 = Image.open('dogy1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).save('increased_Sharpness_5.jpg')

    #  --------- changing color ------
# img2 = Image.open('dogy1.jpg')
# change_color = ImageEnhance.Color(img2)
# change_color.enhance(5).save('black_5_white.jpg')

    #  ----------- Brightness ---------
img3 = Image.open('dogy1.jpg')
change_brightness = ImageEnhance.Brightness(img3)
change_brightness.enhance(2).save('increased_2_brightness.jpg')

         #  ----------- Contrast ---------
img3 = Image.open('dogy1.jpg')
change_brightness = ImageEnhance.Contrast(img3)
change_brightness.enhance(2).save('increased_2_contrast.jpg')
# 0 : Blurry
# 1 : Original Image
# 2 : Image with Increased Sharpness


# from fileinput import filename
from PIL import Image
import os
# img1 = Image.open('images/img.jfif')
# img1.save('images/img2.png')   # changing the extention of image
# img1.show()
# Change the size of image
# max_size = (100,120)
# img1.thumbnail(max_size)
# img1.save('images/dogy2.jpg')
# print(os.getcwd())
for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        filename,extention = os.path.splitext(item)
        # max_size = (650,720)
        # img1.thumbnail(max_size)
        img1.save(f"{filename}.png")
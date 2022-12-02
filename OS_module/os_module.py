import imp


import os
# print(os.getcwd())
# os.mkdir('movies')
old_path = os.path.join(r'D:\python\movies')
new_path = os.path.join(r'D:\python\EditImgWithPython')
os.rename(old_path,new_path)

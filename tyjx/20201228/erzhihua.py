# -*- coding:utf-8 -*-
# python 3.6

from os import listdir
from PIL import Image
import Img      # 自定义的包

def two_value():
    """将训练集所有原始图进行二值化"""

    file_list = listdir('source_image/')
    for each in file_list:
        image = Image.open('source_image/%s' % each)
        image = Img.twoValueImage(image, 200)
        image.save('two_value_image/%s' % each)

if __name__ == '__main__':
    two_value()

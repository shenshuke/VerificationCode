from imp import reload

from selenium import webdriver
import time
import sys, os
from PIL import Image, ImageDraw
import re
import time
from PIL import ImageGrab
from pytesser3 import *



# getPixel为去噪算法
def getPixel(image, x, y, G, N):
    L = image.getpixel((x, y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x, y - 1))
    else:
        return None

    # 降噪


# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# G: Integer 图像二值化阀值
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败
def clearNoise(image, G, N, Z):
    draw = ImageDraw.Draw(image)

    for i in xrange(0, Z):
        for x in xrange(1, image.size[0] - 1):
            for y in xrange(1, image.size[1] - 1):
                color = getPixel(image, x, y, G, N)
                if color != None:
                    draw.point((x, y), color)

                # 测试代码



    os.chdir(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\Scripts")
    time.sleep(2)
    # 截图，获取需要识别的区域
    # 坐标根据自己的分辨率自行调整
    x = 912
    y = 395
    m = 1012
    n = 436
    i = 1
    box = (x, y, m, n)
    img = ImageGrab.grab(box)
    # 保存截取的验证码图片
    img.save(r'D:\DOWNLOAD\pictures.png')
    # 截图完毕后，开始图像识别
    # 判断识别出的验证码是否为四位数，因为pytesser对有干扰的图片识别率较低，故采用多次截图并识别
    im = Image.open(r'D:\DOWNLOAD\pictures.png')
    text = image_to_string(im)
    text = text.replace(' ', '')
    text = re.findall(r"\d+\.?\d*", text)
    b = len(str(text))
    while (b != 8):
        print
        i
        # b为验证码数组长度，b=8说明识别成功，否则点击网页验证码图片刷新验证码再次截图并识别
        button = browser.find_element_by_id('CaptchaImg')
        button.click()
        img = ImageGrab.grab(box)
        i = 2
        # 截图保存路径
        src = 'D:/home/lyt/yzm2/' + bytes(i) + '.jpg'
        # 转灰度并去噪后保存路径
        src1 = 'D:/home/lyt/yzm3/' + bytes(i) + '.jpg'
        img.save(src)
        image = Image.open(src)
        # 将图片转换成灰度图片
        image = image.convert("L")
        # 去噪,G = 50,N = 1,Z = 1
        # N，Z可根据自己需要更改，目前识别成功率在1/3左右
        clearNoise(image, 1, 1, 1)
        # 保存图片
        image.save(src1)
        # 截图处理完毕后，开始图像识别
        im = Image.open(src1)
        text = image_to_string(im)
        text = text.replace(' ', '')
        text = re.findall(r"\d+\.?\d*", text)
        b = len(str(text))
        print(text[0])
    return text[0]
# # 以下为selenium对浏览器的操作
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get('http://29.149.128.186:8850/#/login')
# input_username = browser.find_element_by_name('username')
# input_username.send_keys("admin")
# input_pwd = browser.find_element_by_name('password')
# input_pwd.send_keys("888888")
#
# # 开始验证码识别
# a = imagetext()
# print(a)
# input_verify = browser.find_element_by_name('code')
# input_verify.send_keys(a)
# button = browser.find_element_by_xpath('//*[@id="app"]/div/form/button')
# button.click()

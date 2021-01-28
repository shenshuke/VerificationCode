from selenium import webdriver
import time
from PIL import Image

import pytesseract

driver = webdriver.Chrome()
driver.get('http://29.149.128.186:8850/#/login')
time.sleep(3)
driver.maximize_window()
time.sleep(2)

# 1.登录页面截图并保存在C:/test.png
driver.save_screenshot(r"D:\DOWNLOAD\downpng\test0.png")
im = Image.open(r"D:\DOWNLOAD\downpng\test0.png")
# 2.获取图片验证码坐标和尺寸
code_element = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/div[2]/img')
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
print(left,top,right,height)
# 3.截取图片验证码
img = im.crop((left, top, right, height))
# 4.截取的验证码图片保存为新的文件
img.save(r"D:\DOWNLOAD\downpng\test1.png")
driver.close()
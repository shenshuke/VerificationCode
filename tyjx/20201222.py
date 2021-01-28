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
driver.save_screenshot(r"D:\DOWNLOAD\test.png")
# 2.获取图片验证码坐标和尺寸
code_element = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/div[2]/img')
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open(r"D:\DOWNLOAD\test.png")
# 3.截取图片验证码
img = im.crop((left, top, right, height))
# 4.截取的验证码图片保存为新的文件
img.save(r"D:\DOWNLOAD\test1.png")
driver.close()
im = Image.open(r'D:\DOWNLOAD\test1.png')
gray = im.convert('L')
gray.show()
gray.save(r'D:\DOWNLOAD\test2.png')
threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
# out.show()
out.save(r'D:\DOWNLOAD\test3.png')
th = Image.open(r'D:\DOWNLOAD\test3.png')
for i in range(3, 14):
    str1 = '--psm ' + str(i) + '--oem 3 -c tessedit_char_whitelist=0123456789'
    print(pytesseract.image_to_string(th, config=str1))

import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿

driver = webdriver.Chrome()
driver.get('http://29.149.128.186:8850/#/login')  # 打开登陆页面
time.sleep(3)
driver.maximize_window()
driver.save_screenshot(r'D:\DOWNLOAD\pictures.png')  # 全屏截图
page_snap_obj = Image.open(r'D:\DOWNLOAD\pictures.png')
img = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/div[2]/img')  # 验证码元素位置
time.sleep(1)
location = img.location
size = img.size  # 获取验证码的大小参数
left = location['x']
top = location['y']
right = left + size['width']
bottom = top + size['height']
print(left, top, right, bottom)

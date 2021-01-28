
import time
from selenium import webdriver
from PIL import Image
import pytesseract
# driver_path = "D:\DOWNLOAD\chromewebdriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()
driver.get('http://sso.hq.cpic.com/login')
time.sleep(1)
driver.maximize_window()
time.sleep(1)

# 截图定位验证码
driver.save_screenshot('D:\DOWNLOAD\P13-01.PNG')
code_element = driver.find_element_by_xpath('//*[@id="imgObj"]')
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open(r'D:\DOWNLOAD\P13-01.png')
# 3.截取图片验证码
img = im.crop((left, top, right, height))
# 4.截取的验证码图片保存为新的文件
img.save(r"D:\DOWNLOAD\P13test1.png")
driver.close()
im = Image.open(r'D:\DOWNLOAD\P13test1.png')
gray = im.convert('L')
gray.save(r'D:\DOWNLOAD\test2.png')
threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
out.save(r'D:\DOWNLOAD\P13test2.png')
img = Image.open(r'D:\DOWNLOAD\P13test2.png')
img.show()
text = pytesseract.image_to_string(img)
print(text)

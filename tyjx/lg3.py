import pytesser3
import time
import selenium
from selenium import webdriver
from PIL import Image

# driver_path = "D:\DOWNLOAD\chromewebdriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()
driver.get('http://sso.hq.cpic.com/login')
time.sleep(5)
driver.maximize_window()
time.sleep(1)

# 截图定位验证码
driver.save_screenshot('D:\DOWNLOAD\2.PNG')
image = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/div[2]/img')
imgry = image.convert('L')
imgry.show()
print(pytesser3.image_to_string(image))

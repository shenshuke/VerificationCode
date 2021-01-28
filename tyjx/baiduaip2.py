from aip import AipOcr
from selenium import webdriver
import time
from PIL import Image

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
url = 'http://29.149.128.186:8850/#/login'
driver.get(url)
driver.save_screenshot('D:/DOWNLOAD/save_screenshot.png')

code_ele = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/div[2]/img')
print("验证码的坐标为：", code_ele.location)
print("验证码的大小为：", code_ele.size)
# 验证码的坐标为： {'x': 1723, 'y': 581}
# 验证码的大小为： {'height': 48, 'width': 96}

# (4)图片4个点的坐标位置
left = code_ele.location['x']  # x点的坐标
top = code_ele.location['y']  # y点的坐标
right = code_ele.size['width'] + left  # 上面右边点的坐标
down = code_ele.size['height'] + top  # 下面右边点的坐标
image = Image.open(r'D:/DOWNLOAD/save_screenshot.png')
code_image = image.crop((left, top, right, down))
code_image.save(r'D:/DOWNLOAD//code_image.png')

APP_ID = '23194923'  # 应用的appid
API_KEY = 'Y41GVuN8MdX0NFbCTfvbFt9t'  # 应用的appkey
SECRET_KEY = 'uTth0sVfMzOFpFpjTCz5RFmd3wy0mpuL'  # 应用的secretkey
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content(r'D:/DOWNLOAD//code_image.png')

# 调用通用文字识别（高精度版） """
code_ocr_original_result = client.basicAccurate(image)
print('code ocr original result:')
print(code_ocr_original_result)
print('final code result:')
for text in code_ocr_original_result.get('words_result'):
    code_ocr_final_result = text.get('words')
    print(text.get('words'))
code_ocr_final_result_with_out = code_ocr_final_result.replace(' ', '')
# account = driver.find_element_by_id('account')
# account.send_keys('')
#
# password = driver.find_element_by_id('password')
# password.send_keys('')
#
# code_input = driver.find_element_by_id('rancode')
# code_input.send_keys(code_ocr_final_result_with_out)
#
# code_input.submit()
# time.sleep(10)
# end = input('press any key to go out')

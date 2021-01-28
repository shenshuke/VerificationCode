from PIL import Image
import pytesseract
code_element = Image.open(r"D:\DOWNLOAD\downpng\test1.png")
x = 16
y = 6
h_avg = 20
w_avg = 14
h = y + h_avg
w = x + w_avg
img = code_element.crop((x, y, w, h))
img.save(r"D:\DOWNLOAD\downpng\test01.png")
gray = img.convert('L')
imggray = gray.convert('L')
# imggray.show()
#设置阈值
threshold = 165
#加载像素点
pixdata = imggray.load()
#获取图片的宽高
width, height = imggray.size
for y in range(height):
    for x in range(width):
        if pixdata[x, y] < threshold:
            pixdata[x, y] = 0
        else:
            pixdata[x, y] = 255
#查看图片
binImg  = imggray
# binImg .show()
#加载像素点
pixdata = binImg.load()
#获取图片宽高
width, height = binImg.size
for y in range(1, height- 1):
    for x in range(1, width- 1):
        count = 0
        # 上
        if pixdata[x, y - 1] > 245:
            count = count + 1
        # 下
        if pixdata[x, y + 1] > 245:
            count = count + 1
        # 左
        if pixdata[x - 1, y] > 245:
            count = count + 1
        # 右
        if pixdata[x + 1, y] > 245:
            count = count + 1
        # 左上
        if pixdata[x - 1, y - 1] > 245:
            count = count + 1
        # 左下
        if pixdata[x - 1, y + 1] > 245:
            count = count + 1
        # 右上
        if pixdata[x + 1, y - 1] > 245:
            count = count + 1
        # 右下
        if pixdata[x + 1, y + 1] > 245:
            count = count + 1
        #消除噪点
        if count > 100:
            pixdata[x, y] = 255
#查看图片
nrImg = binImg
nrImg.save(r"D:\DOWNLOAD\downpng\test02.png")
img = Image.open(r"D:\DOWNLOAD\downpng\test02.png")
text = pytesseract.image_to_string(img)
print(text)
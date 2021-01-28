from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random
import string


# 随机数字
def rndchar():
    # print(chr(65))
    return chr(random.randint(65, 90))


# 随机数字+字母
def getrandl(num, many):  # num 位数   many个数
    for x in range(many):
        s = ''
        for i in range(num):
            n = random.randint(1, 2)  # 1 生成数字 2 生成字母
            if n == 1:
                numb = random.randint(0, 9)
                s += str(numb)
            else:
                s += str(random.choice(string.ascii_letters))
    return s


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# a = rndchar()
# b = rndchar()
# c = rndchar()
# d = rndchar()
# print(a,b,c,d)

width = 60 * 4
height = 60
# 设置画布大小、颜色
img = Image.new('RGB', (width, height), (0, 0, 0))  # 0, 0,0  黑色
# img.show()
# 设置字体
font = ImageFont.truetype('msyh.ttc', 36)
draw = ImageDraw.Draw(img)
# 填充像素点
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):
    # draw.text((60*x,10),rndchar(),font =font,file =(255,255,255))#  60 横坐标、60+10=70位置继续、10 纵坐标
    draw.text((60 * t, 10), getrandl(1, 4), font=font, fill=rndColor())  # 60 横坐标、60+10=70位置继续、10 纵坐标
img = img.filter(ImageFilter.BLUR)
img.save(r'D:\DOWNLOAD\TEST1.PNG')
img.show()

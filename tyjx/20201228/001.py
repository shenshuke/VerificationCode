import  pytesser3
from PIL import Image
import  pytesseract

# 新建Image对象
image = Image.open(r"D:\STUDY\VerificationCode\3.png")
# 调用tesserocr的image_to_text()方法，传入image对象完成识别
Img =image.convert('L')
# result = pytesser3.image_to_string(image)
# print(result)
#二值化
threshold = 90      #我们自己定义的阈值
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# 图片二值化
photo = Img.point(table, '1')
photo.save("test.jpg")  #得到二值化处理后图片test.jpg
image =Image.open("test.jpg")  #显示二值化处理后的图片\
image.show()
# result = pytesseract.image_to_string(image).strip()
# print(result)
import pytesseract

from PIL import Image

im =Image.open(r'D:\DOWNLOAD\P13test2.png')
im.
text = pytesseract.image_to_string(im)

print(text)
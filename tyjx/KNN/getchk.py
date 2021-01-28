import urllib3,urllib,os
import requests
def savepng(index):
    if not  os.path.exists(pngsource):
        os.mkdir(pngsource)
for i in range(500):
    u=urllib('http://29.149.128.186:8850/invest/api/kaptcha/image')
    data =u.read()
    png_path ='pngsource/%d.png'%(i + int(index) )
    with open(pngsource,'wb') as f:
        f.write(data)

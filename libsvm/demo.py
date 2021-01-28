import  libsvm
import requests
from PIL import  Image
#下载验证码
def downloads_pic(**kwargs):
    pic_name = kwargs.get('pic_name', None)
    pic_path = 'D:\DOWNLOAD\source_png'
    url = 'http://29.149.128.186:8850/invest/api/kaptcha/image'
    res = requests.get(url, stream=True)
    with open(pic_path + pic_name+'.png', 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

        f.close()

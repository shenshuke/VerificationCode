# coding:utf8
import requests


def downimage(i):
    # 构建session
    sess = requests.Session()
    # 建立请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Connection": "keep-alive"}
    # 这个url是联合航空公司验证码，根据访问时间戳返回图片
    url = "http://29.149.128.186:8850/invest/api/kaptcha/image"
    # 获取响应图片内容
    image = sess.get(url, headers=headers).content
    # 保存到本地
    with open(str(i) + "image.png", "wb") as f:
        f.write(image)


if __name__ == "__main__":
    # 获取10张图片
    for i in range(10):
        downimage(i)
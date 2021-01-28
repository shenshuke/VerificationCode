def download_image():
    """download captcha image"""
    url = 'http://www.szcredit.org.cn/web/WebPages/Member/CheckCode.aspx'
    headers = {'user-agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) "
                              "AppleWebKit/536.3 (KHTML, like Gecko) "
                              "Chrome/19.0.1063.0 Safari/536.3")}
    for i in range(0, 500):
        image = Img.download_image(url=url, headers=headers)
        with open('source_image/%s.png' % str(i), 'wb') as f:
            f.write(image)
            f.close()
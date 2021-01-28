# coding=utf_8
import requests
import json
import unittest, time, re


class APIGetAdlis(unittest.TestCase):
    def test_call(self):
        github_url = 'http://29.149.128.186:8850/invest/api/kaptcha/image'
        data = json.dumps({'keyword': '测试'})
        resp = requests.post(github_url, data)
        print(resp.json)
        # if (data['errno']!=''):
        #  self.assertEqual(0, data['errno'])
        #  print"接口 deal/list-------------OK!"
        # else:
        #  print"接口 deal/list-------------Failure!"
        #  self.assertEqual(0, data['errno'])
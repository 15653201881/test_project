# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @File : test_home_page.py
# @Project: 云平台接口测试用例

import unittest
import os
import sys

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from test_project.common.http_requests import HttpRequests

class Test_microservice(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.url = 'http://10.10.100.224:10001'
        cls.http = HttpRequests(cls.url)

    def test_001_query_able(self):
        data = {}
        response = Test_microservice.http.post('/api/publicServiceZuul/architectureChart/findAll',data = data)
        self.assertEqual(200,response.status_code,'返回非200')
    def test_002_update_able(self):
        data = {"userId": "<userId>",
      "id": "<id>",
      "blockType": "<blockType>",
      "blockName": "<blockName>",
      "parentId": "<parentId>"}
        response = Test_microservice.http.post('/api/publicServiceZuul/architectureChart/saveAC',data = data)
        self.assertEqual(200,response.status_code,'返回非200')
    def test_003_delete_able(self):
        data = {"userId": "<userId>",
      "id": "<id>"}
        response = Test_microservice.http.post('/api/publicServiceZuul/architectureChart/deleteAC',data = data)
        self.assertEqual(200,response.status_code,'返回非200')
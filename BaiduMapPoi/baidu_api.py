# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlencode
import json

class BaiduApi():

    output = 'json'
    ak = 'juUHBugfdfVlthxjY5zyKlpNQA4IM8UM'

    def __init__(self, address):
        self.address = address
        location = self.getLocation(self.address)
        self.lat = location.get('result').get('location').get('lat')
        self.lng = location.get('result').get('location').get('lng')

    def getJson(self, url):
        response = urlopen(url)
        content = response.read()
        return json.loads(content.decode('utf-8'))

    def getLocation(self, address):
        dict = {'address': self.address,
            'output': self.output,
            'ak': self.ak}
        param = urlencode(dict)
        url = "http://api.map.baidu.com/geocoder/v2/?%s" % param
        return self.getJson(url)

    def getInfo(self, type, radius):
        dict = {'query': type,
            "location": repr(self.lat) + ',' + repr(self.lng),
            "radius": radius,
            "scope": 2,
            "page_size": 20,
            "page_num": 0,
            "output": self.output,
            "ak": self.ak,}
        param = urlencode(dict)
        url = "http://api.map.baidu.com/place/v2/search?%s" % param
        data = self.getJson(url)
        total = data.get('total')
        result = data.get('results')
        page_size = int(total/20-1) if total%20==0 else int(total/20)
        if page_size > 0:
            for x in range(1,page_size+1):
                dict['page_num'] = x
                new_param = urlencode(dict)
                new_url = "http://api.map.baidu.com/place/v2/search?%s" % new_param
                new_data = self.getJson(new_url)
                new_result = new_data.get('results')
                result = result + new_result
        return result

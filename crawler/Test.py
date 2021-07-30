# -*- coding:utf-8 -*-
from importlib import reload
import urllib3

import requests
import json
from pyquery import PyQuery as pq
import time

import sys

reload(sys)

fw = open('/Users/lipengfei/Documents/WebCrawler/offershow6.txt', 'w+')
urllib3.disable_warnings()


def fun(id):
    url = 'http://www.ioffershow.com/ offerdetail/%d/' % (id)
    r = requests.get(url)
    d = pq(r.text)
    values = []
    values.append(str(i))
    for option in d('div.ui-block-b'):
        value = d(option).text()
        values.append(value)
    print(','.join(values))


def fun1(i):
    url = 'https://www.ioffershow.com/webapi/v2/offer_detail'

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx67fbba6cd94591e4/40/page-frame.html'}
    data = {
        'access_token': '$ytkzhLIvv5+sYwytrpIDkg26d4HQpxjr6pCoffershowzju1qaz.1607933254395.e39a698a2cec127b37ac3c3e06fcb588',
        'id': i}
    time.sleep(1)
    r = requests.post(url, headers=headers, data=data, verify=False)
    j = json.loads(r.text)
    j = j['info']

    lines = []
    lines.append(str(j['id']))
    lines.append(j['ip'])
    lines.append(j['company'])
    lines.append(j['position'])
    lines.append(j['xueli'])
    lines.append(j['city'])
    lines.append(j['hangye'])
    lines.append(j['salary'])
    lines.append(str(j['number']))
    lines.append(str(j['score']))
    lines.append(j['remark'].replace('\n', '\\\\n'))
    lines.append(j['time'])
    line = '\t'.join(lines)

    fw.write(line + '\n')
    print(line)


if __name__ == '__main__':
    for i in range(39881, 56176):
        # for i in range(33174, 39880):
        # for i in range(27719, 33173):
        # for i in range(14300, 27719):
        # for i in range(4568, 10701):
        try:
            fun1(i)
        except Exception as err:
            print(i)
            print(err)
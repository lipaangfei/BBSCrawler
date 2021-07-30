#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
获取所有的面试、综合经验链接

"""
import datetime
import requests
from bs4 import BeautifulSoup
import time


class Crawler:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Host': 'bbs.yingjiesheng.com',
            # 'Referer': 'https://bbs.yingjiesheng.com/forum-349-1.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'cookie': '__yjs_duid=1_fde4a61c65cd33a5b7c87fbc56d9784a1619584133734; 2Inh_4553_saltkey=jzsRRGRS; 2Inh_4553_lastvisit=1619580533; Hm_lvt_b15730ce74e116ff0df97e207706fa4a=1619584134; CookieUuid=6a440db5e435583e050c5cb42dda6148; YSSN=a84o7dqj3vl1ai6dtdqb219mep7aosrj; jspaceuser=%D2%B9%B2%D7%D4%C2; wespaceuser=RkROR1NKV1Z9Q2pYCBZDRkcBQglTQBcHXw5AE08RUEVbBEEWV1pbQRIVEQ; uchomeyjs_reward_log=daylogin%2C9786940; uchomeyjs_auth=71aaQwKVLQpjqcwzc882kkFpaT06XCOfLi5kkAXtQwqbZE3VhtNMtwaZAMlhEbhAThuMRZ6ezfubAkRp84ogloUbXIGzrA; uchomeyjs_loginuser=%D2%B9%B2%D7%D4%C2; 2Inh_4553_auth=e7e6SoBVieLww%2BGfkVAxJtQiJWSqSBnYm2p%2BLHVmTpcDk4HS1JLz8UwpuL3Zv2ty96dHTt8EZ%2FyY8jWjCpO8KMHsf9rDLQ; 2Inh_4553_connect_is_bind=0; 2Inh_4553_nofavfid=1; 2Inh_4553_smile=3D1; 2Inh_4553_atarget=1; 2Inh_4553_st_t=13906980%7C1619591782%7C8db21f1662de4d0fb3d158b16acc73c2; 2Inh_4553_forum_lastvisit=D_61_1619591708D_1352_1619591782; 2Inh_4553_freeaddon_daily_topic_finish=2320943_1314; PHPSESSID=6cc411c19f5fe7fd5119af70f431bb7a; 2Inh_4553_ulastactivity=58e3RkmsPfvim0SlsVbCrzHCf%2FVi4dC%2FkZCeqt5PQMI%2FgJb2a69g; 2Inh_4553_viewid=tid_2312987; __cfduid=d6c18aac2f918e816480b9d7b9cd93df81619768261; 2Inh_4553_sid=OmI3XR; 2Inh_4553_lip=123.118.105.120%2C1619766114; 2Inh_4553_st_p=13906980%7C1619768262%7C7093e789501254e7f3f876473ec7022a; 2Inh_4553_sendmail=1; Hm_lpvt_b15730ce74e116ff0df97e207706fa4a=1619768266; 2Inh_4553_secqaa=21339.6a68ff4f7cbfa3ee4f; 2Inh_4553_lastact=1619768268%09home.php%09spacecp; 2Inh_4553_checkpm=1'
        }
        self.parse_failed_count = 0
        self.start_datetime = datetime.datetime.strptime("2020-05-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        self.type, self.tag = 1, 1

    def request(self, url: str):
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            # time.sleep(random.randint(1, 3))
            time.sleep(1)
            print(url, response.status_code)
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            return None

    def parse_result(self, html: str) -> str:
        if not html:
            return None
        soup = BeautifulSoup(html, 'lxml')
        types = soup.find(id="thread_types")
        # print(types.find_all(name='li'))
        for type in types.find_all(name='li'):
            if type.text == "综合经验":
                # print(type.get('href'))
                a = type.find(name='a')
                print(a.get('href'))
                return a.get('href')


if __name__ == '__main__':
    crawler = Crawler()

    outfile = open('/Users/lipengfei/Documents/WebCrawler/parent_url_experience.txt', 'w')
    with open('/Users/lipengfei/Documents/WebCrawler/parent_url_all.txt', 'r') as urls:
        while True:
            parent_url = urls.readline()
            if not parent_url:
                break
            html = crawler.request(parent_url)

            parent_url = crawler.parse_result(html)
            if not parent_url:
                continue
            parent_url = parent_url + '&orderby=dateline'
            outfile.write(parent_url + '\n')
            outfile.flush()
    outfile.close()

#! /usr/bin/python3.6
# -*- coding: utf-8 -*-
import datetime
import re

import requests
from bs4 import BeautifulSoup
import time
import MySQLdb


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
        self.type, self.tag = 2, 1

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

    def parse_result(self, html: str, parent_url: str, db, cursor) -> str:
        if not html:
            return None
        # with open("/Users/lipengfei/Documents/WebCrawler/html_temp.txt", 'w') as temp:
        #     temp.write(html)
        def R(s: str) -> str:
            if not s:
                return s
            return s.replace("'", "\\\'").replace('"', '\\\"')

        soup = BeautifulSoup(html, 'lxml')
        pt = soup.find(id='pt')
        heads = pt.find_all('a')
        if len(heads) == 4:
            category = heads[2].string
            company = heads[3].string
        else:
            category = heads[1].string
            company = heads[2].string
        discuss_posts = soup.find_all(name='tbody',
                                      attrs={"id": re.compile(r"normalthread_(\s\w+)?|stickthread_(\s\w+)?")})
        # print(discuss_posts)
        is_outdated = False  # 剩余帖子是否过时
        for discuss_post in discuss_posts:
            try:
                post_info = discuss_post.find(class_='xst')
                author_info = discuss_post.find(class_="by")
                author, date_str = [x for x in author_info.text.split('\n') if x]
                # print(date_str)
                release_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                if release_time < self.start_datetime:
                    if 'stickthread_' not in str(discuss_post):  # 不是置顶帖
                        print("到达过期临界点, release_time = ", release_time)
                        is_outdated = True
                        break
                    else:
                        continue
                if 'title="精华' not in str(discuss_post):
                    continue
                title = post_info.string
                # url = post_info['href']
                url = post_info.get('href')
                content = self.get_content(url)
                sql = """INSERT INTO `bbs_interview_discuss` (parent_url, url, category, company, title, content, release_time, author, type, tag)
                VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')""" \
                    .format(R(parent_url), R(url), R(category), R(company), R(title), R(content), release_time, R(author),
                            self.type, self.tag)
                try:
                    cursor.execute(sql)
                    db.commit()
                    # print(sql)
                    pass
                except:
                    db.rollback()
                    print('insert failed')
                    print(parent_url, url, category, company, title, content, release_time, author, self.type, self.tag)
            except:
                crawler.parse_failed_count += 1
                print('parse discuss failed')
                print('post_info:', post_info)
                print('url:', post_info.get('href'))
                continue
        next_page = soup.find(class_='nxt')
        next_parent_url = next_page['href'] if next_page else None
        if is_outdated:
            print("next page out-dated", next_parent_url)
            return None  # 其他帖子过期了，没有下一页啦

        return next_parent_url

    # def insert(self, parent_url, url, category, company, title, content):

    def get_content(self, url):
        html = self.request(url)
        if not html:
            return ''
        try:
            # print(html)
            soup = BeautifulSoup(html, 'lxml')
            posts = soup.find_all(class_='t_f')
            contents = []
            for post in posts:
                contents.append(post.text)
            contents = [content for content in contents if content]
            # print('contents', contents)
            return ''.join(contents)
        except:
            crawler.parse_failed_count += 1
            print('parse content failed', url, posts)
        return ''


if __name__ == '__main__':
    while True:
        start_time = datetime.datetime.now()
        finished_urls = set()
        all_finished = True
        with open('/Users/lipengfei/Documents/WebCrawler/finished_parent_url.txt', 'r') as f:
            while True:
                url = f.readline()
                if not url:
                    break
                finished_urls.add(url)
        outfile_finished_url = open('/Users/lipengfei/Documents/WebCrawler/finished_parent_url.txt', 'a+')
        crawler = Crawler()
        db = MySQLdb.connect('d.nowcoder.com', 'nc_test', 'nc_test_2019', 'wenyibi_test', port=12340, charset='utf8')
        cursor = db.cursor()
        # cursor.execute("SELECT * FROM `user_basic_info` LIMIT 1")
        # data = cursor.fetchone()
        # print(data)
        with open('/Users/lipengfei/Documents/WebCrawler/parent_url.txt', 'r') as urls:
            while True:
                parent_url = urls.readline()
                if not parent_url:
                    break
                if parent_url in finished_urls:
                    continue
                outfile_finished_url.write(parent_url)
                outfile_finished_url.flush()
                all_finished = False
                crawler.parse_failed_count = 0
                crawler.parse_failed_count_limit = 10
                while parent_url:
                    parent_url = parent_url.replace('\n', '')
                    html = crawler.request(parent_url)
                    if html:
                        parent_url = crawler.parse_result(html, parent_url, db, cursor)
                    else:
                        break
                    if crawler.parse_failed_count > crawler.parse_failed_count_limit:
                        break
                if crawler.parse_failed_count > crawler.parse_failed_count_limit:
                    break

        db.close()
        outfile_finished_url.close()
        end_time = datetime.datetime.now()
        print("开始时间:", start_time, "结束时间:", end_time, "时长(秒):", end_time - start_time)
        if all_finished:
            break

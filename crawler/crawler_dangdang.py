import json
import re
import requests

class Crawler:
    def __init__(self):
        pass

    def request_dangdang(self, url: str):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            return None

    def parse_result(self, html: str):
        pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
        items = re.findall(pattern, html)
        for item in items:
            yield {
                """
                排名, 书名, 图片地址, 作者, 推荐指数, 五星评分次数, 价格
                """
                'rank': item[0],
                'image': item[1],
                'title': item[2],
                'recommend': item[3],
                'author': item[4],
                'times': item[5],
                'price': item[6]
            }

    def write_result(self, items):
        with open('/Users/lipengfei/Documents/WebCrawler/books.txt', 'a', encoding='UTF-8') as f:
            for item in items:
                print('开始写入数据 ====> ' + str(item))
                f.write(json.dumps(item, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    crawler = Crawler()
    for page in range(1, 21):
        url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{}'.format(page)
        html = crawler.request_dangdang(url)
        if html:
            items = crawler.parse_result(html)
            crawler.write_result(items)
import requests
from bs4 import BeautifulSoup
import xlwt

class Crawler:
    def __init__(self):
        self.r = 1

    def request(self, url: str, headers):
        # print(url)
        try:
            response = requests.get(url, headers=headers)
            # print(response.status_code)
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            return None

    def parse_result(self, html: str):
        if not html:
            return
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
        view = soup.find(class_='grid_view')
        if not view:
            return
        item_list = view.find_all('li')
        if not item_list:
            return
        for item in item_list:
            try:
                item_name = item.find(class_='title').string
                item_img = item.find('a').find('img').get('src')
                item_index = item.find(class_='').string
                item_score = item.find(class_='rating_num').string
                item_author = item.find('p').text
                item_intr = item.find(class_='inq').string
                sheet.write(self.r, 0, item_name)
                sheet.write(self.r, 1, item_img)
                sheet.write(self.r, 2, item_index)
                sheet.write(self.r, 3, item_score)
                sheet.write(self.r, 4, item_author)
                sheet.write(self.r, 5, item_intr)
                self.r += 1
                print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
            except:
                continue


if __name__ == '__main__':
    crawler = Crawler()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Host': 'movie.douban.com',
               'Referer': 'https://movie.douban.com/top250',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
               }

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '图片')
    sheet.write(0, 2, '排名')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '作者')
    sheet.write(0, 5, '简介')
    crawler.r = 1

    for page in range(20):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(page * 25)
        html = crawler.request(url, headers)
        if html:
            crawler.parse_result(html)
    book.save('/Users/lipengfei/Documents/WebCrawler/movies.xlsx')

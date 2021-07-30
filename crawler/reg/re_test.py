import re

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall('.*?(\d+)\s',content,re.S)
print(res)
content = re.sub('\d+', '250', content)
print(content)
res = re.search('.*?(\d+)\s', content, re.S)
print(res.group(1))

category_a_link = '<a href="https://bbs.yingjiesheng.com/forum.php?gid=844">消费品/化妆品/食品/餐饮/烟草类公司</a>'
print(re.findall(r'<a.*?>(.*?)[<\n]', category_a_link))

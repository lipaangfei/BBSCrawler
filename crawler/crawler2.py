import ssl
import requests
# r = requests.get('https://api.github.com/events')

r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8'  # 设置编码格式
# print(r.status_code)
# print(r.encoding)
# print(r.text)
# print(r.content)
# print(r.headers)
# print(r.json())
# print(r.raw)
# print(r.raw.read(10))

# 当你想要一个键里面添加多个值的时候
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)


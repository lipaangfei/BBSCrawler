import ssl
import urllib
from urllib import request, response, error, parse, robotparser
context = ssl._create_unverified_context()
url = 'https://oauth.51job.com/get_login.php?client_id=000001&redirect_uri=https%3A%2F%2Funion.yingjiesheng.com%2Fapi_login.php&from_domain=yjs_web&display=default&state=7c893ec1be7b355a91bdc3c474087add--368ba30db1d6217cc18f7dfe0bd27a79&partner='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
data = {
    'loginname_encrypt': '/Pjp1Ki1S3j65+QC2J2pkg==',
    'password_encrypt': 'hiqxe1qVXCoVuCrSwYM+eg=='
}
data = bytes(parse.urlencode(data), 'utf-8')
req = request.Request(url, data=data, headers=headers, method='POST')
res = request.urlopen(req, context=context)
print(res.read().decode('utf-8'))
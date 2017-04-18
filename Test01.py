# import re
import requests

request_header = {
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

url = "~/Desktop/Python/html_test.html"

z = requests.get(url,headers = request_header)

print z.status_code
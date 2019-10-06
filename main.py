import requests

import browser_cookie3

cj = browser_cookie3.chrome()
url = "https://api.clippings.io/api/UserFileUploads/"


headers = {
    'Host':'my.clippings.io',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://my.clippings.io/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,es-419;q=0.8,es;q=0.7'
}

payload = {
    'Accept':'application/json',
    'Cache-Control': 'no-cache',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJtIW4xjUhazQ7b4Y',
    'DNT': '1',
    'Origin':  'https://my.clippings.io',
	'Referer': 'https://my.clippings.io/',
	'Sec-Fetch-Mode': 'cors',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
	'X-Requested-With':' XMLHttpRequest'
}

r = requests.POST(
    url,
    headers=headers,
    payload=payload,
    cookies=cj
    )

print(r.content)

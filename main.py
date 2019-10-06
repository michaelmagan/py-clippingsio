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


Accept: application/json
	.	Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJc3N1ZXIiOiJodHRwOi8vd3d3LmNsaXBwaW5ncy5pbyIsIkF1ZGllbmNlIjoiaHR0cDovL3d3dy5jbGlwcGluZ3MuaW8iLCJDbGFpbXMiOlt7Iklzc3VlciI6IkxPQ0FMIEFVVEhPUklUWSIsIk9yaWdpbmFsSXNzdWVyIjoiTE9DQUwgQVVUSE9SSVRZIiwiUHJvcGVydGllcyI6e30sIlN1YmplY3QiOm51bGwsIlR5cGUiOiJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIiwiVmFsdWUiOiJtcm1hZ2FuIiwiVmFsdWVUeXBlIjoiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEjc3RyaW5nIn0seyJJc3N1ZXIiOiJMT0NBTCBBVVRIT1JJVFkiLCJPcmlnaW5hbElzc3VlciI6IkxPQ0FMIEFVVEhPUklUWSIsIlByb3BlcnRpZXMiOnt9LCJTdWJqZWN0IjpudWxsLCJUeXBlIjoiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiLCJWYWx1ZSI6IjE5MDc2MCIsIlZhbHVlVHlwZSI6Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hI3N0cmluZyJ9LHsiSXNzdWVyIjoiTE9DQUwgQVVUSE9SSVRZIiwiT3JpZ2luYWxJc3N1ZXIiOiJMT0NBTCBBVVRIT1JJVFkiLCJQcm9wZXJ0aWVzIjp7fSwiU3ViamVjdCI6bnVsbCwiVHlwZSI6Imh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2VtYWlsYWRkcmVzcyIsIlZhbHVlIjoibWljaGFlbC5tYWdhbjkyQGdtYWlsLmNvbSIsIlZhbHVlVHlwZSI6Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hI3N0cmluZyJ9XSwiZXhwIjoxNTcwMTQxODA2fQ.Bvn44Qyjbap8euY3Q44ln6dkTVYM1H3ZxHm22OdkBSU
	.	Cache-Control: no-cache
	.	Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJtIW4xjUhazQ7b4Y
	.	DNT: 1
	.	Origin: https://my.clippings.io
	.	Referer: https://my.clippings.io/
	.	Sec-Fetch-Mode: cors
	.	User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36
	.	X-Requested-With: XMLHttpRequest


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

import urllib.request
import ssl

context = ssl._create_unverified_context()
# get
# response = urllib.request.urlopen("http://www.google.com")
# print(response.read())

# post
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode())

# timeout
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
#     print(response.read().decode())
# except urllib.error.URLError as e:
#     print("time out!")

# response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
# print(response.status)
# print(response.getheaders())

# url = "https://www.douban.com"
# url = "http://httpbin.org/post"
# headers={
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
#               "Version/14.0.2 Safari/605.1.15"
# }
#
# data = bytes(urllib.parse.urlencode({"name":"eric"}), encoding = "utf-8")
# req = urllib.request.Request(url = url, data = data, headers = headers, method = "POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

url = "https://www.reed.edu"
headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
              "Version/14.0.2 Safari/605.1.15"
}
req = urllib.request.Request(url = url, headers = headers)
response = urllib.request.urlopen(req, context = context)
print(response.read().decode('utf-8'))
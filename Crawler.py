# coding = utf-8
# @author: Yifang Zhu
# @file: crawler.py
from bs4 import BeautifulSoup  # website, crawl data
import re
import urllib.request
import xlwt
import ssl  # to solve the SSL problem while crawling

context = ssl._create_unverified_context()


def main():
	baseurl = "https://www.reed.edu/"
	# 1. getData
	datalist = getData(baseurl)
	# 2. analyze data
	savepath = "reed.xls"
	# 3. save data
	saveData(datalist, savepath)

# get the content of a specific url
def askURL(url):
	# pretend to be a web browser
	head = {  # stimulate to be a head
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
		              "Version/14.0.2 Safari/605.1.15"
	}
	# try to request the url
	request = urllib.request.Request(url=url, headers=head)
	html = ""
	try:
		response = urllib.request.urlopen(request, context=context)
		html = response.read().decode()
	# print(html)
	except urllib.error.URLError as e:
		if hasattr(e, "code"):
			print(e.code)
		if hasattr(e, "reason"):
			print(e.reason)
	
	return html

# Crawl the website
def getData(baseurl):
	html = askURL(baseurl)
	soup = BeautifulSoup(html, "html.parser")
	a = soup.find_all('a')
	links = []
	for item in a:
		url = item.get('href')
		if (baseurl in url) and (url != baseurl) and (url not in links):
			links.append(url)
	print(links)



# save data
def saveData(datalist, savepath):
	pass


if __name__ == "__main__":
	main()
	print("Finish!")
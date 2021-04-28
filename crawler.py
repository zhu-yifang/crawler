# coding = utf-8
# @author: Yifang Zhu
# @file: crawler.py
from bs4 import BeautifulSoup	#website, crawl data
import re
import urllib.request
import xlwt
import ssl	# to solve the SSL problem while crawling
context = ssl._create_unverified_context()

def main():
	baseurl = "https://movie.douban.com/top250?start="
	# 1. getData
	datalist = getData(baseurl)
	# 2. analyze data
	savepath = ".\\doubanMovieTop250.xls"
	# 3. save data
	# saveData(savepath)

	# askURL("https://movie.douban.com/top250?start=")
# pattern to find links
findLink = re.compile('<a href="(.*)">')	# create a pattern
# Crawl the website
def getData(baseurl):
	datalist = []
	for i in range(0,1):
		url = baseurl + str(i*25)
		html = askURL(url)	# save the web source code

		# analyze each webpage
		soup = BeautifulSoup(html,"html.parser")
		for item in soup.find_all("div", class_="item"):
			# print(item)
			item = str(item)
			# get links
			links = re.findall(findLink, item)[0]
			print(links)
	return datalist

# get the content of a specific url
def askURL(url):
	# pretend to be a web browser
	head = {	# stimulate to be a head
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
					  "Version/14.0.2 Safari/605.1.15"
	}
	# try to request the url
	request = urllib.request.Request(url = url, headers = head)
	html = ""
	try:
		response = urllib.request.urlopen(request, context=context)
		html = response.read().decode()
		# print(html)
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e, code)
		if hasattr(e, "reason"):
			print(e.reason)

	return html

# save data
def saveData(savepath):
	pass

if __name__ == "__main__":
	main()
# coding = utf-8
# @author: Yifang Zhu
# @file: crawler.py
from bs4 import BeautifulSoup	#website, crawl data
import re
import urllib
import xlwt

def main():
	baseurl = "https://movie.douban.com/top250?start="
	# 1. getData
	datalist = getData(baseurl)
	# 2. analyze data
	savepath = ".\\doubanMovieTop250.xls"
	# 3. save data
	saveData(savepath)
	
# Crawl the website
def getData(baseurl):
	datalist = []
	return datalist
# save data
def saveData(savepath):
	pass

if __name__ == "__main__":
	main()
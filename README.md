# Crawler
A crawler as the term project of CSCI396 Computer Networks

Given a URL, your crawler should return a "map" of all the URLs linked from the first URL that are also on the same server and no higher in hierarchy (e.g., if I give you "reed.edu" it should return many websites including "reed.edu/computer-science/", but given "reed.edu/computer-science/" should not return reed.edu as part of the map). The "map" can be just a textfile with minor formatting indicating what's linked to what, or could be a data structure within your program (e.g., a tree :)) with at least a 'print' sort-of command for me to visualize. Basically, given an address, your crawler goes, retrieves the object (ideally first object is an HTML), parses the object, finds other URLs, checks that they're in the same path as the first object, fetches those objects, parses them, repeat. Makes sense?

# How to test it?
In crawler.py, in the main(), you can change the baseurl to the website you want to crawl. Then run the code, it will print all the URLs linked from the first URL that are also on the same server and no higher in hierarchy.

# Design decision
First of all, I found https://www.bilibili.com/video/BV12E411A7ZQ, which is a very helpful video tutorial. I made a crawler for https://movie.douban.com/top250 with this tutorial (in practice.py). It can crawl the content of the top 250 movies in Douban. And output the result into Douban.xls.

Packages used: BeautifulSoup, re, urllib, xlwt, ssl 

# Potential extensions
1. Parse robots.txt
2. Multithreading
3. Crawl pictures with a specific hashtag on twitter

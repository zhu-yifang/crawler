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
findLink = re.compile(r'<a href="(.*)">')	# create a pattern
# Img
findImgSrc = re.compile(r'<img alt=".*" class="" src="(.*)" width=".*"/>',re.S)	#re.s
# Title
findTitle = re.compile(r'<span class="title">(.*)</span>')
# Rating
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# Judge
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# Inq
findInq = re.compile(r'<span class="inq">(.*)</span>')
# Bd
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

# Crawl the website
def getData(baseurl):
    datalist = []
    for i in range(0,1):
        url = baseurl + str(i*25)
        html = askURL(url)	# save the web source code

        # analyze each webpage
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []   # save data of one movie
            item = str(item)
            # print(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            
            imgSrc = re.findall(findImgSrc, item)[0]
            # print(imgSrc)
            data.append(imgSrc)
            
            titles = re.findall(findTitle,item)  # there may be multiple titles
            # print(titles)
            if(len(titles) == 2):
                ctitle = titles[0]  # Chinese title
                #print(ctitle)
                data.append(ctitle)
                otitle = titles[1].replace("\xa0/\xa0","")  # other title
                #print(otitle)
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
                
            rating = re.findall(findRating, item)
            data.append(rating)
            
            judgeNum = re.findall(findJudge, item)
            data.append(judgeNum)
            
            Inq = re.findall(findInq, item)
            if len(Inq) !=0:
                Inq = Inq[0].replace('。','')
                data.append(Inq)
            else:
                data.append('')

            Bd = re.findall(findBd, item)[0]
            Bd = re.sub("<br(\s+)?/>(\s+)?"," ", Bd)    # remove <br/>
            Bd = re.sub("/"," ", Bd)
            # Bd = re.sub('\xa0', '', Bd)
            # Bd = re.sub('\n', '', Bd)
            data.append(Bd.strip())
            
            #print(data)
            datalist.append(data)
    # print(datalist)
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
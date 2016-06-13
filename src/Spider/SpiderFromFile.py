#coding=utf-8
'''
Created on 2014-8-3

@author: Sachiel
'''
import re,urllib2
def testRegex():
    f = open("page.html")
    page = f.read()
    myItems = re.findall('<a class="titlelnk" href="(.*?)" target="_blank">(.*?)</a>', page, re.S)
    items = []

    for item in myItems:
        pattern = re.compile('.*java|python.*?', re.I)
        search = pattern.search(item[1])
        if search:
            content = "link: " + item[0] + ", title: " + item[1]
            items.append(content)

    for item in items:
        print item

def GetPage(page):
        myUrl = "http://www.cnblogs.com/#p" + page
        req = urllib2.Request(myUrl)
        req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
        response = urllib2.urlopen(req)
        mypage = response.read()
        unicodePage = mypage.decode("utf-8")
        f = open("page.html", "wb")
        f.write(unicodePage)

#GetPage(str(1))
testRegex()
#coding=utf-8
'''
Created on 2014-8-3
spider on cnblog
@author: Sachiel
'''

import urllib2, re, thread, time
class Spider_Model:
    
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
        self.cookie
    
    def GetPage(self, page):
        myUrl = "http://www.cnblogs.com/#p" + page
        req = urllib2.Request(myUrl)
        req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
        print 'scraping......'
        response = urllib2.urlopen(req)
        mypage = response.read()
        unicodePage = mypage.decode("utf-8")
        f = open(page + ".html", "wb")
        f.write(unicodePage)
        print 'another page~'

        myItems = re.findall('<a class="titlelnk" href="(.*?)" target="_blank">(.*?)</a>', unicodePage, re.S)
        items = []
        for item in myItems:
            pattern = re.compile('.*java|python.*?', re.I)
            search = pattern.search(item[1])
            if search:
                content = "link: " + item[0] + ", title: " + item[1]
                items.append(content)
                print content
        return items
    
    def LoadPage(self):    
        while self.enable:      
            if len(self.pages) < 2:    
                try:
                    myPage = self.GetPage(str(self.page))    
                    self.page += 1    
                    self.pages.append(myPage)    
                except:    
                    print 'can\'t access to cnblog！'    
            else:    
                time.sleep(1)    
            
    def ShowPage(self,nowPage,page):
        print "press enter continue，press quit end"
        for items in nowPage:    
            print u'Page %d' % page , items  
            myInput = raw_input()    
            if myInput == "quit":    
                self.enable = False    
                break
    
    def Start(self):
        self.enable = True
        page = self.page
        
        thread.start_new_thread(self.LoadPage,()) 
        
        while self.enable:

            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1
                
print u'press enter: '    
raw_input('')    
myModel = Spider_Model()    
myModel.Start()   
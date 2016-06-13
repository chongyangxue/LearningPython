#coding=utf-8

import urllib2, re, thread, time
class Spider_Model:
    
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
    
    def GetPage(self, page):
        myUrl = "http://www.qiushibaike.com/hot/page/" + page
        req = urllib2.Request(myUrl)
        req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
        response = urllib2.urlopen(req)
        mypage = response.read()
        unicodePage = mypage.decode("utf-8")
        myItems = re.findall('<div class="content" title=".*?">(.*?)</div>', unicodePage, re.S)
        items = []
        for item in myItems:
            content = item.replace("\n", "")
            items.append(content)

        return items
    
    def LoadPage(self):    
        # 如果用户未输入quit则一直运行    
        while self.enable:    
            # 如果pages数组中的内容小于2个    
            if len(self.pages) < 2:    
                try:    
                    # 获取新的页面中的段子们    
                    myPage = self.GetPage(str(self.page))    
                    self.page += 1    
                    self.pages.append(myPage)    
                except:    
                    print '无法链接糗事百科！'    
            else:    
                time.sleep(1)    
            
    def ShowPage(self,nowPage,page):
        print "按回车键继续阅读，输入quit结束"
        for items in nowPage:    
            print u'第%d页' % page , items  
            myInput = raw_input()    
            if myInput == "quit":    
                self.enable = False    
                break
    
    def Start(self):
        self.enable = True
        page = self.page
        
        thread.start_new_thread(self.LoadPage,()) 
        
        while self.enable:
            # 如果self的page数组中存有元素  
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1
            #else:
                #print u"正在加载中。。。"
                #self.LoadPage()
                
print u'请按下回车浏览今日的糗百内容：'    
raw_input('')    
myModel = Spider_Model()    
myModel.Start()   
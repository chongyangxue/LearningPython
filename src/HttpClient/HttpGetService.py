'''
Created on 2014-7-28

@author: Sachiel
'''
from urllib2 import Request, urlopen, HTTPError, URLError
def httpGet(url):
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
    req.add_header('cliversion', '3.0.1.0012')

    try: 
        resp = urlopen(req)
    except HTTPError, e:
        print e.code
    except URLError, e:
        print e.reason
    else:
        print resp.info()
        print resp.geturl()
        print "----------------------------------------------------"
        return resp.read()
    
if __name__ == '__main__':

    htmlstr = httpGet('http://www.sohu.com')
    print htmlstr

    
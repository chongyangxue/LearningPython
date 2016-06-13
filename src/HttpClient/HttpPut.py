'''
Created on 2014-7-29

@author: Sachiel
'''
import urllib2
def putRequest(url, data=None):
    request = urllib2.Request(url, data=data)  
    request.get_method = lambda: 'PUT' # or 'DELETE'  
    response = urllib2.urlopen(request)
    return response.read()

if __name__ == '__main__':

    htmlstr=putRequest('http://www.sogou.com')

    print htmlstr
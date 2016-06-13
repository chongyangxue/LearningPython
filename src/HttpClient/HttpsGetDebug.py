'''
Created on 2014-7-29

@author: Sachiel
'''
import urllib2
from os.path import join

def httpsGet(url):
    httpHandler = urllib2.HTTPHandler(debuglevel=1)  
    #httpsHandler = urllib2.HTTPSHandler(debuglevel=1)  
    opener = urllib2.build_opener(httpHandler)  
    urllib2.install_opener(opener)  
    response = urllib2.urlopen(url)
    print response.info()
    return response.read()

def saveToFile(path, filename, content):
    with open(join(path, filename), 'wb') as f:
        f.write(content)

if __name__ == '__main__':

    htmlstr=httpsGet('https://www.github.com')
    print htmlstr

    #saveToFile('f:','page.html', htmlstr)
'''
Created on 2014-8-3

@author: Sachiel
'''
import re  

pattern = re.compile('world', re.I)  

search = pattern.search('hello world!')
   
if search:  
    print search.group()  
    
match = pattern.match('hello world!')
   
if match:  
    print match.group()
else:
    print "not match"
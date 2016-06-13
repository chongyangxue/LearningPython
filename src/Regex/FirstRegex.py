'''
Created on 2014-7-31

@author: Sachiel
'''
import re

pattern = re.compile(r'hello')

match1 = pattern.match("hello world")
match2 = pattern.match("helloo world")
match3 = pattern.match("helllo world")

if match1:
    print match1.group()
else:
    print "match1 failed"
    
if match2:
    print match2.group()
else:
    print "match2 failed"
    
if match3:
    print match3.group()
else:
    print "match3 failed"
    
    
a = re.compile(r"""\d +  # the integral part 
                   \.    # the decimal point 
                   \d *  # some fractional digits""", re.X)  
  
b = re.compile(r"\d+\.\d*")  
  
match11 = a.match('3.1415')  
match12 = a.match('33')  
match21 = b.match('3.1415')  
match22 = b.match('33')   
  
if match11:  
    print match11.group()  
else:  
    print u'match11 failed'  
      
if match12:  
    print match12.group()  
else:  
    print u'match12 failed'  
      
if match21:  
    print match21.group()  
else:  
    print u'match21 failed'  
  
if match22:  
    print match22.group()  
else:  
    print u'match22 failed'
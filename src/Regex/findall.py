'''
Created on 2014-8-3

@author: Sachiel
'''
import re

p=re.compile('\d+')

print p.findall('one1two2three3four4')
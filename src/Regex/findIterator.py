'''
Created on 2014-8-3

@author: Sachiel
'''
import re

p = re.compile('\d+')

for m in p.finditer('one1two2three3four4'):
    print m.group() 
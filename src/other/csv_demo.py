'''
Created on 2015-4-2

@author: chongyangxue
'''
#coding=utf-8
import csv

csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])
csvfile.close()
#coding=utf-8
'''
Created on 2014-8-6

@author: chongyangxue
'''
import socket
import urllib2
if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print 'socket false:%s' % e
    print 'socket...'
    
    try:
        print 'connect...'
        sock.connect(('127.0.0.1', 10001))
        print 'connected'
        sock.send('hello')
        resp = sock.recv(1024)
        if str(resp).endswith("ok"):
            try:
                print 'send request...'
                req = urllib2.Request("action.do")
                req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
                req.add_header('cliversion', '3.0.1.0012')
                req.add_header('token', '7328780ab09d8afdb9727eccbd35862c')
                req.add_header('action', 'apps')
                sock.send(str(req))
                resp = sock.recv(2048)
                print resp
            except socket.error, e:
                print 'send false'  
                sock.close()
    except socket.error, e:
        print 'connetc false:%s' % e
    
    
        
    

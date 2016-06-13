# encoding:utf8


import urllib
import urllib2
import datetime
import hashlib

SMS_URL = "http://sms.sohusce.com/smsaccess/send"
#SMS_URL = "http://sms.apps.sohuno.com/smsaccess/send"
SCE_APPID = '10001'
SECRET = '26402506030f3ad18148a3dda2d49425'
KEY = '20140221184851895SMSPLATACCESS071'
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


headers = {
    'code' : hashlib.md5('SCE_APPID=%sSECRET=%sTIMESTAMP=%s' % (SCE_APPID, SECRET.upper(), timestamp)).hexdigest(),
    'timestamp' : timestamp,
}

data = {
    'wl_appid' : 100173,
    'sce_appid' : SCE_APPID,
    'destnumber' : '13466666210',
    'content' : u'hello world!',
    'tailsp' : '',
    'timestamp' : timestamp,
    'linkid' : 0,
    'priority' : 3,
}

def sign(data):
    sign = '%(wl_appid)s%(destnumber)s%(content)s%(timestamp)s' % data + KEY
    return hashlib.md5(sign).hexdigest()

data['enc'] = sign(data)

req = urllib2.Request(SMS_URL, urllib.urlencode(data), headers=headers)

print urllib2.urlopen(req).read()

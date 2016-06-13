import urllib,urllib2
import cookielib

url = "http://cloudscape.sohu.com/user/login"
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

values = {"username":"", "password":"", "captcha":"0"}
data = urllib.urlencode(values)
resp = opener.open(url, data)

for item in cookie:
    if item.name == "csuserinfo" or item.name == "csuserdig":
        print item.name + "=" + item.value
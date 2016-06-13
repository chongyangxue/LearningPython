from urllib2 import Request, urlopen
import urllib

values = {}
values["username"] = ""
values["password"] = ""
values["captcha"] = "0"
req = Request("http://cloudscape.sohu.com/user/login")
data = urllib.urlencode(values)
resp = urlopen(req, data, 1);
info = resp.info()
print info



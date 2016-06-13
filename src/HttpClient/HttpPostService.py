from urllib2 import Request, urlopen, HTTPError, URLError
import urllib

values = {}
values["url"] = ""
values["password"] = ""

req = Request("http://test-autotest05.app.sohuce.com/check_redis")
data = urllib.urlencode(values)
try: 
    resp = urlopen(req, data)
except HTTPError, e:
    print e
except URLError, e:
    print e
else:
    print resp.info()
    print "----------------------------------------------------"
    print resp.read()
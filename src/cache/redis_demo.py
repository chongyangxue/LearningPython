import redis
import hashlib

r = redis.Redis(host='10.16.4.214', port=13001, password='7a1e13274a91bf68a7cca75360391287')
key = hashlib.md5("chongyangxue@sohu-inc.comtoken").hexdigest()
value = r.get(key)
print value 

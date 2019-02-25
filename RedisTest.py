import redis
pool = redis.ConnectionPool(host='192.168.4.128',port=6379,password='123456')
r = redis.Redis(connection_pool=pool)
r.set('name', 'xulin5')
print(r.get('name'))

import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379, password='root')
r.set('foo', 'hello')
r.rpush('mylist', 'one')
print(r.get('foo'))
print(r.rpop('mylist'))




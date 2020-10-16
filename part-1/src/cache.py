import redis
import fakeredis

redis = redis.Redis('172.17.0.2')

def insert_cache(hash_json):  
    redis.set(hash_json, hash_json, ex=600)

def check_if_in_cache(hash_json):
    if redis.exists(hash_json):
        return True
    else:
        insert_cache(hash_json)
        return False

"""Creating fake_redis for testing purposes"""

fake_redis = fakeredis.FakeStrictRedis()

def fake_redis_insert_cache(hash_json):
    fake_redis.set(hash_json, hash_json, ex=600)

def fake_redis_check_if_in_cache(hash_json):
    if fake_redis.exists(hash_json):
        return True
    else:
        return False

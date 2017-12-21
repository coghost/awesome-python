from huey import RedisHuey

redis_conf = {
    'host': 'localhost',
    'port': 6380,
    'password': '123456',
    'db': 0,
}
rd_huey = RedisHuey(result_store='task_abc', **redis_conf)

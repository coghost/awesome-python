broker_url = 'amqp://admin:admin@localhost/cc'
result_backend = 'rpc://admin:admin@localhost/cc'
enable_utc = True
timezone = 'Asia/Shanghai'
task_ignore_result = True

task_queues = {
    'simple_usage': {
        'exchange': 'cc',
        'routing_key': 'simple_usage',
    },
}
task_routes = {
    'tasks.add': {
        'queue': 'simple_usage',
        'routing_key': 'tasks.add',
    },
}

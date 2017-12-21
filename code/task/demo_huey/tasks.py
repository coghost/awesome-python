import os
import sys
import time

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

import cde
from huey import crontab

from task.demo_huey.config import rd_huey as huey


@huey.task()
def count_beans(num):
    res = '{}: -- {} beans --'.format(cde.now(), num)
    print(res)
    time.sleep(3)
    return res


@huey.task(retries=3, retry_delay=5)
def try_thrice():
    print('trying....')
    raise Exception('nope')


@huey.periodic_task(crontab(minute='*'))
def print_time():
    print(cde.now())

import os
import sys
import datetime

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-3])
sys.path.append(app_root)

# import cutil
import cde

# 这个实例是用来被 huey_consumer.py 来指向的
"""
使用: huey_consumer.py app.rd_huey -w 4
来运行 ``消费程序``
"""
from task.demo_huey.config import rd_huey

from task.demo_huey.tasks import count_beans, try_thrice, print_time


def run():
    # 建立5个立即执行的任务
    for i in range(5):
        r = count_beans(i)
        print('Enqueued {} beans'.format(i))
        print(r.get())

    # 建立1个10s后执行的任务
    count_beans.schedule(args=(100,), delay=10)

    # 建立一个 60s 后运行的任务
    count_beans.schedule(args=(100,),
                         eta=datetime.datetime.now() + datetime.timedelta(seconds=60))

    # 异常任务, 重试
    try_thrice()
    try_thrice.revoke()
    try_thrice.restore()

    # 定期任务
    print_time()

    print('all done@[{}]'.format(cde.now()))


if __name__ == '__main__':
    run()

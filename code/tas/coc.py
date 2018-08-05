# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '30/03/2018 11:53 AM'
__description__ = '''
无论在 consumer 还是 producer，都是发出消息给对方后，就把代码执行交到对方，等待对方执行结果。
参考: 
https://blog.csdn.net/u010161379/article/details/51645264
'''

import os
import sys
import time
import asyncio
import threading

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from izen import dec


class PrCs(object):
    """
        简单的 send/yield 测试
    """

    def __init__(self):
        self.test()

    def consumer(self):
        r = ''
        while True:
            n = yield r
            if not n:
                return
            print('[CS] cs {}...'.format(n))

            if n == 3:
                r = '404'
            else:
                r = '200 OK'

    def produce(self, c):
        c.send(None)
        n__ = 0
        while True:
            n__ += 1
            print('[PD] pd {}...'.format(n__))
            r = c.send(n__)
            print('[PD] cs res: {}'.format(r))
            if r == '404':
                break

        c.close()

    def test(self):
        c = self.consumer()
        self.produce(c)


class YieldFr(object):
    def __init__(self):
        self.th()

    @asyncio.coroutine
    def hello(self):
        print('Hello Async... {}'.format(threading.current_thread()))
        r = yield from asyncio.sleep(1)
        print('End Hello. {} {}'.format(r, threading.current_thread()))

    async def hell(self):
        print('Hello Async... {}'.format(threading.current_thread()))
        r = await asyncio.sleep(1)
        print('End Hello. {} {}'.format(r, threading.current_thread()))

    @asyncio.coroutine
    def fet(self, host):
        print('wget {}'.format(host))
        conn = asyncio.open_connection(host, 80)
        reader, writer = yield from conn
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        yield from writer.drain()
        while True:
            line = yield from reader.readline()
            if line == b'\r\n':
                break

            print('{} header > {}'.format(host, line.decode('utf-8').rstrip()))

        writer.close()

    def th(self):
        tasks = [self.hello() for x in range(3)]
        # tasks = [
        #     fet(x) for x in ['www.sina.com.cn', 'www.sohu.com', 't.tinyc.cn']
        # ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.wait(tasks)
        )
        loop.close()


class YFRead(object):
    def __init__(self):
        self.tread()

    def reader(self):
        for i in range(4):
            yield '<< {}'.format(i)

    def reader_wrap(self, g):
        # 1. 遍历
        # for v in g:
        #     yield v

        # 2. yield from
        yield from g

    def tread(self):
        wrp = self.reader_wrap(self.reader())
        for i in wrp:
            print(i)


class YFWr(object):
    def __init__(self):
        self.spawn()

    def spawn(self):
        w = self.writer()
        wr = self.writer_wrap(w)
        wr.send(None)
        for i in range(4):
            wr.send(i)

    def writer(self):
        while True:
            w = (yield)
            print('>> ', w)

    def writer_wrap1(self, coro1):
        coro1.send(None)  # 生成器准备好接收数据
        while True:
            try:
                x = (yield)  # x接收send传进的数据
                coro1.send(x)  # 然后将x在send给writer子生成器
            except StopIteration:  # 处理子生成器返回的异常
                pass

    def writer_wrap(self, cor):
        yield from cor


now = lambda: time.time()


async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))


async def do_it_ok(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))


class ATask(object):
    def __init__(self, idx=0):
        # self.run()
        self.idx = idx
        start = now()
        getattr(self, 'run_{}'.format(idx))()
        print('Total Cost is:', now() - start)

    async def do_it_0(self, x):
        print('Waiting:', x)
        return 'Done@ {}s'.format(x)

    async def do_it_1(self, x):
        print('Waiting: ', x)
        await asyncio.sleep(x)
        d = 'Done@ {}s'.format(x)
        print(d)
        return d

    def run_0(self):
        # co_ = self.do_it(2)
        co_ = getattr(self, 'do_it_{}'.format(self.idx))(2)

        loop_ = asyncio.get_event_loop()
        loop_.run_until_complete(co_)

    def run_1(self):
        tasks = [
            asyncio.ensure_future(
                getattr(self, 'do_it_{}'.format(self.idx))(x)
            )
            for x in range(3)
        ]

        loop_ = asyncio.get_event_loop()
        loop_.run_until_complete(asyncio.wait(tasks))

        [
            print(x.result()) for x in tasks
        ]
        loop_.close()

    async def gen_tasks(self):
        tasks = [
            asyncio.ensure_future(
                getattr(self, 'do_it_1'.format(self.idx))(x)
            )
            for x in range(5)
        ]
        return await asyncio.wait(tasks)

    def run_2(self):
        loop = asyncio.get_event_loop()
        done, pend = loop.run_until_complete(self.gen_tasks())

        for task in done:
            print(task.result())

        loop.close()

    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def run_3(self):
        new_loop = asyncio.new_event_loop()
        t = threading.Thread(target=self.start_loop, args=(new_loop,))
        t.start()
        task6 = self.do_it_1(6)
        task3 = self.do_it_1(3)

        asyncio.run_coroutine_threadsafe(task6, new_loop)
        asyncio.run_coroutine_threadsafe(task3, new_loop)
        print('all D')

    def run_4(self):
        start = now()
        new_loop = asyncio.new_event_loop()
        t = threading.Thread(target=self.start_loop, args=(new_loop,))
        t.start()
        print('TIME: {}'.format(time.time() - start))

        asyncio.run_coroutine_threadsafe(do_it_ok(3), new_loop)
        asyncio.run_coroutine_threadsafe(do_it_ok(4), new_loop)


def run():
    while True:
        print('Iam Reached!')
        time.sleep(1)


if __name__ == '__main__':
    # YFRead()
    # YFWr()
    # ATask(3)
    PrCs()
    # run()

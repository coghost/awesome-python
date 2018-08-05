# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/7/4 10:25 AM'
__description__ = '''
- [yield vs yield from](https://blog.csdn.net/u010161379/article/details/51645264)
- [yield/send到yield from再到async/await](https://blog.csdn.net/soonfly/article/details/78361819)
- [GIL](https://www.cnblogs.com/stubborn412/p/4033651.html)
'''

import os
import sys
import asyncio
import random

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from izen import dec


class SimpleYieldSend(object):
    """简单的协程实现
    `consumer` 函数是一个 `generator`, 将 `consumer` 传入 `produce` 后

    1. 首先调用 `c.send(None)`, 启动生成器
    2.
    """

    def consumer(self):
        r = ''
        while True:
            n = yield r
            if not n:
                return

            print('[CS] cs {}...'.format(n))
            r = '200 OK'

    def produce(self, c):
        c.send(None)
        n = 0
        while n < 5:
            n += 1
            print('[PD] pd {}...'.format(n))
            r = c.send(n)
            print('[PD] got from cs: {}'.format(r))

        c.close()

    def test(self):
        c = self.consumer()
        self.produce(c)


class FibYield(object):
    def fibo(self, m=15):
        """ 第0个是0, 1是1, 从第2个开始, 每个数都是前两个数之和

            0, 1, 1, 2, 3, 5, 8 ...

            a, b
            a = b
            b = a+ b

            :param m: 可迭代的最大的值
            :type m:
            :return:
            :rtype:
            """
        a, b = 0, 1
        while m >= b:
            yield b
            a, b = b, a + b
        return 'done'

    def fibo_wrapper(self, g):
        yield from g

    def fibo_dir(self):
        for x in self.fibo(10):
            print(x)

    def test(self):
        fw = self.fibo_wrapper(self.fibo(20))
        for x in fw:
            print(x)


class StackRW(object):
    def reader(self):
        for i in range(5):
            yield '<< {}'.format(i)

    def reader_wrap(self, g):
        for x in g:
            yield x

    def test_reader_wrap(self):
        wrp = self.reader_wrap(self.reader())
        for i in wrp:
            print(i)

    def writer(self):
        while True:
            w = yield
            print('>> {}'.format(w))

    def writer_wrap(self, coro):
        yield from coro
        # coro.send(None)
        # while True:
        #     x = yield
        #     coro.send(x)

    def test_writer_wrap(self):
        w = self.writer()
        wrap = self.writer_wrap(w)
        wrap.send(None)
        for i in range(4):
            wrap.send(i)


class AioCo(object):
    @asyncio.coroutine
    def smart_fib(self, n):
        a, b = 0, 1
        while n >= b:
            to = random.uniform(0, 0.2)
            yield from asyncio.sleep(to)
            print('Smart one think {:.2f} secs to get {}'.format(to, b))
            a, b = b, a + b

    @asyncio.coroutine
    def stupid_fib(self, n):
        a, b = 0, 1
        while n >= b:
            to = random.uniform(0, 0.5)
            yield from asyncio.sleep(to)
            print('Stupid one think {:.2f} secs to get {}'.format(to, b))
            a, b = b, a + b

    # @dec.prt(1)
    def test(self):
        loop = asyncio.get_event_loop()
        tasks = [
            self.smart_fib(20),
            self.stupid_fib(20)
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        print('All Done')
        loop.close()


class AsAw(object):
    async def empty_list(self, lst):
        while len(lst):
            print(lst.pop())
            await asyncio.sleep(random.uniform(0, 0.3))

    def test(self):
        a = ['aaa', 'bbb', 'ccc']
        b = [x for x in range(5)]
        b2 = [x for x in range(8)]
        b3 = [x for x in range(2)]
        c = self.empty_list(a)
        c1 = self.empty_list(b)
        c2 = self.empty_list(b2)
        c3 = self.empty_list(b3)
        tasks = [c, c1, c2, c3]

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        print('all Done')
        loop.close()


def run():
    pass
    # s = SimpleYieldSend()
    # s.test()
    # f = FibYield()
    # f.test()
    # f.fibo_dir()
    # sr = StackRW()
    # sr.test_reader_wrap()
    # sr.test_writer_wrap()
    # ac = AioCo()
    # ac.test()
    sw = AsAw()
    sw.test()


if __name__ == '__main__':
    run()

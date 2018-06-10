# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '30/03/2018 6:42 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from aiohttp import web, ClientSession
import aiohttp
import async_timeout
import asyncio

import requests
import random

from izen import helper

idx_ = 0

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3163.100 '
                  'Safari/537.36',
    'Referer': 'http://yxpjwnet1.com'
}


class WSvr(object):
    def __init__(self):
        pass

    async def handle(self, request):
        global idx_
        name = request.match_info.get('name', "Anonymous")
        # to = random.random() / random.randint(1, 100)
        idx_ += 1
        text = "Hello, {}{}".format(name, idx_)
        # await asyncio.sleep(to)
        print(text)
        return web.Response(text=text)

    def run(self):
        app = web.Application()
        app.add_routes([web.get('/', self.handle),
                        web.get('/{name}', self.handle)])

        web.run_app(app)


class WebGet(object):
    def __init__(self, url):
        self.run(url)

    def run(self, url):
        res = requests.get(url)
        print(res.text)


class AIOGet(object):
    def __init__(self, url):
        self.url = url if isinstance(url, list) else [url]
        self.run()

    async def aget(self, url_in):
        global idx_
        async with ClientSession() as sess:
            async with sess.get(url_in, headers=headers) as resp:
                res = await resp.read()
                print('DONE!', res[:20])
                idx_ += 1
                with open('{}.jpg'.format(idx_), 'wb') as f:
                    f.write(res)
                # print(helper.to_str(res.text))
                return res

    def run(self):
        tasks = [
            self.aget(x) for x in self.url
        ]
        l_ = asyncio.get_event_loop()
        l_.run_until_complete(asyncio.wait(tasks))


async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)


if __name__ == '__main__':
    # WSvr().run()
    url = ''
    urls = [
        url.format(x + 10) for x in range(8)
    ]
    # WebGet(url)
    AIOGet(urls)
    # runit()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

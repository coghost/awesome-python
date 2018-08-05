# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/7/1 11:06 AM'
__description__ = '''
参考
https://www.cnblogs.com/grandyang/p/4606334.html
'''

import os
import sys
from functools import wraps
import random

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)
import linecache

counter = 0
enable_trace = True

chaos_list = []


def singleton(cls_single):
    _instance = {}

    def _init(*args, **kwargs):
        if cls_single not in _instance:
            _instance[cls_single] = cls_single(*args, **kwargs)
        return _instance

    return _init


def trace(do=True, show_details=False):
    def glb_trace_fn(frame, event, arg):
        if event != 'call':
            return None
        return local_trace

    def local_trace(frame, event, arg):
        global counter
        if event == 'line':
            file_name = frame.f_code.co_filename
            line_no = frame.f_lineno
            bname = os.path.basename(file_name)

            if show_details:
                print("{}({} - {}): {}"
                      .format(bname,
                              counter,
                              line_no,
                              linecache.getline(file_name, line_no)), end='')
            counter += 1
        return local_trace

    if not hasattr(do, '__call__'):
        def dec(fn):
            @wraps(fn)
            def _wrap(*args, **kwargs):
                global counter
                if not do:
                    return fn(*args, **kwargs)

                sys.settrace(glb_trace_fn)
                counter = 0
                result = fn(*args, **kwargs)
                sys.settrace(None)
                if not show_details:
                    print('[{}] running {} times'.format(fn.__name__, counter))
                return result

            return _wrap

        return dec

    @wraps(do)
    def _wrap(*args, **kwargs):
        global counter

        sys.settrace(glb_trace_fn)
        counter = 0
        result = do(*args, **kwargs)
        sys.settrace(None)
        if not show_details:
            print('[{}] running {} times'.format(do.__name__, counter))
        return result

    return _wrap


def set_chaos_len(n=16, show=False):
    chaos_list = []
    for i in range(n):
        chaos_list.append(random.randint(1, 1000))
    if show:
        print(chaos_list)
    return chaos_list


def get_list(n=16, m=20):
    chaos_list = []
    for i in range(n):
        chaos_list.append(random.randint(0, m))
    return chaos_list


@trace(1, 1)
def t1():
    print('t1')
    print('t2')


@trace(1, 1)
def l1():
    for i in range(10):
        pass


if __name__ == '__main__':
    t1()
    # l1()

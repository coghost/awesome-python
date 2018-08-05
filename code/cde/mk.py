# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/29 11:37 AM'
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
from logzero import logger as log


def cpz1(plain='aaaabbbbbbccccaa'):
    """
    aaaabbbbbbcccaa => a4b6c3a2
    :param plain:
    :type plain:
    :return:
    :rtype:
    """
    arr = []
    dat = {}
    l = ''

    for s in plain:
        if l != s:
            dat.setdefault(s, 0)
            arr.append(dat)
            l = s
        else:
            dat[s] += 1

    print(dat)
    print(arr)


def cpz(plain='aaaabbbbbbccccaa'):
    arr = []
    sub_ar = {}
    l = ''
    for p in plain:
        if l != p:
            sub_ar = {p: 1}
            arr.append(sub_ar)
            l = p
        else:
            sub_ar[p] += 1

    s = ['{}{}'.format(list(a.keys())[0], list(a.values())[0]) for a in arr]
    s = ''.join(s)
    print(s)
    return s


def compress(chars='aaaabbbbbbccccaa'):
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return write


def run():
    pass
    # cpz()
    # c = compress()
    # print(c)
    log.info('iam ok', extra={'a': 'whoami'})


if __name__ == '__main__':
    run()

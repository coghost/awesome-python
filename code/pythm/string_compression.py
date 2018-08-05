# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/7/2 10:08 AM'
__description__ = '''
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)


class Solution(object):
    def __init__(self,
                 plain='{}{}{}{}'.format('a' * 3, 'b' * 20, 'c' * 5, 'a' * 2),
                 delim=''):
        self.plain = plain
        self.delim = delim
        self.zp = ''

    def compress(self):
        """use list as store
        """
        l = ''
        arr = []
        tmp = []
        for p in self.plain:
            if l != p:
                tmp = [p, 1]
                arr.append(tmp)
                l = p
            else:
                tmp[1] += 1
        self.zp = '{}'.format(self.delim).join(['{}{}'.format(x[0], x[1]) for x in arr])

    def compress1(self):
        """use l, c as store
        """
        # last index
        l, c = '', 0
        for _, p in enumerate(self.plain):
            if l != p:
                if l:
                    self.zp += '{}{}{}'.format(l, c, self.delim)
                l, c = p, 1
            else:
                c += 1
            if _ == len(self.plain) - 1:
                self.zp += '{}{}'.format(l, c)

    def compress2(self):
        chars = [x for x in self.plain]
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


def run():
    s = Solution(delim='')
    s.compress1()
    print(s.zp)
    print([x for x in s.zp])


if __name__ == '__main__':
    run()

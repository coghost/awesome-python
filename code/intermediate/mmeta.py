# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '04/23/2018 15:07'
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

from logzero import logger as log  # pylint: disable=import-error


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


class MyShinyClass_1(object):
    pass


def echo_bar(self):
    print(self.bar)

# the metaclass will automatically get passed the same argument
# that you usually pass to `type`


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
      Return a class object, with the list of its attribute turned
      into uppercase.
    """

    # pick up any attribute that doesn't start with '__' and uppercase it
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass(type):

    def __new__(mcs, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, mcs).__new__(mcs, clsname, bases, uppercase_attr)


class Foo(metaclass=upper_attr):  # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    bar = 'bip'  # pylint: disable=C0102


def run_1():
    my_class = choose_class('foo')
    print(my_class)
    MyShinyClass = type('MyShinyClass', (), {})
    print(MyShinyClass)
    print(MyShinyClass())

    Foo = type('Foo', (), {'bar': True})
    FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})


def run():
    print(hasattr(Foo, 'bar'))
    # Out: False
    print(hasattr(Foo, 'BAR'))
    # Out: True

    f = Foo()
    print(f.BAR)  # pylint: disable=E1101
    # Out: 'bip'


def make_hook(f):
    f.is_hook = 1
    return f


class MyType(type):
    def __new__(mcs, name, bases, attrs):
        if name.startswith('None'):
            return None

        newattrs = {}
        for attr_name, attr_val in attrs.items():
            if getattr(attr_val, 'is_hook', 0):
                newattrs['__{}__'.format(attr_name)] = attr_val
            else:
                newattrs[attr_name] = attr_val

        return super(MyType, mcs).__new__(mcs, name, bases, newattrs)

    def __init__(cls, name, bases, attrs):
        super(MyType, cls).__init__(name, bases, attrs)
        print('Would register class {} now.'.format(cls))

    def __add__(cls, other):
        class AutoClass(cls, other):
            pass
        return AutoClass

    def unregister(cls):
        print('Would unregister class {} now.'.format(cls))


class MyObject(metaclass=MyType):
    pass


class NoneSample(MyObject):
    pass


class Example(MyObject):
    def __init__(self, val):
        self.value = val

    @make_hook
    def add(self, other):
        return self.__class__(self.value + other.value)


class Sibling(MyObject):
    pass


def run_my_type():
    print('{}, {}'.format(type(NoneSample), repr(NoneSample)))
    Example.unregister()
    inst = Example(10)
    print(inst + inst)
    ExmSib = Example + Sibling
    print(ExmSib)
    print(ExmSib.__mro__)


if __name__ == '__main__':
    # run()
    run_my_type()

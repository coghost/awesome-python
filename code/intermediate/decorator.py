# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '04/20/2018 12:08'
__description__ = '''
this file is all about decorators.
作用: 装饰器可以让你在不对现有代码作改动的情况下, 影响原有函数运行情况. 
1. 在函数运行前/后做某些事. 
2. 修改函数运行, 而不需要对原函数做改变. 
i.e. 
- 防止函数异常 @dec.catch
- 将函数放置于线程运行 @dec.threads(True)
- 打印函数运行时间 @dec.prt
- ... 

Refer Links:
- https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators/1594484#1594484
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from logzero import logger as log  # pylint: disable=import-error
from izen import dec  # pylint: disable=no-name-in-module


def shout(word="yes"):
    """functions 在python中被当作对象来处理.
    """

    return word.capitalize() + '!'


def t_fir():
    scream = shout
    try:
        d = shout("hi vscode. ")
        print(d)
    except UnboundLocalError as _:
        pass
    print(scream())
    del shout
    # maybe work on py2, but here not worked throw UnboundLocalError
    print(scream())


def talk():
    def whisper(word="yes"):
        return word.lower() + '...'

    print(whisper())


'''
函数引用
- 可以指定给变量
- 可以在另一函数中定义
'''


def get_talk(kind="shout"):
    def shout(word="yes"):
        return word.capitalize()+"!"

    def whisper(word="yes"):
        return word.lower()+"..."

    if kind == "shout":
        return shout
    else:
        return whisper


'''
现在你知道了理解`decorator`所需要的所有知识. 可以看到, `decorator` 是封装`wrappers`
这让你可以在执行你的代码之前和之后做任何你想实现的事情, 而且并不需要你变动函数本身.

注意:
- decorator 会让函数调用变慢.
- 不能取消装饰, 如果函数被装饰, 那么函数所有代码均被装饰.
'''


def doSomethingBefore(func):
    print("I do something before then I call the function you gave me")
    print(func())


def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper


def sandwich(food="--ham--"):
    print(food)


def makebold(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<b>" + fn() + "</b>"
    return wrapper


def makeitalic(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<i>" + fn() + "</i>"
    return wrapper


@makebold
@makeitalic
def say():
    return "hello"


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am {0}, what did you think?".format(self.age + lie))


def decorator_maker():
    print("I make decorators! I am executed only once: "
          "when you make me create a decorator.")

    def my_decorator(func):
        print("I am a decorator! I am executed only when you decorate a function.")

        def wrapped():
            print("I am the wrapper around the decorated function. "
                  "I am called when you call the decorated function. "
                  "As the wrapper, I return the RESULT of the decorated function.")
            return func()
        print("As the decorator, I return the wrapped function.")
        return wrapped

    print("As a decorator maker, I return a decorator")
    return my_decorator


@decorator_maker()
def decorated_function():
    print("I am the decorated function.")


def run_():
    pass
    # t_fir()
    # talk()
    # t = get_talk()
    # print(t('IamG'))
    # doSomethingBefore(t)
    sandwich()  # pylint: disable=E0601
    # sandwich_ = bread(ingredients(sandwich))
    # sandwich_()
    # print(say())
    l = Lucy()
    # l.sayYourAge(-3)
    # nd = decorator_maker()
    # d_f = nd(decorated_function)
    # d_f()
    print('=' * 32)
    decorated_function()


if __name__ == '__main__':
    run_()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '05/23/2018 10:03'
__description__ = '''
https://www.zhihu.com/question/22311781
https://en.wikibooks.org/wiki/Computer_Science_Design_Patterns
'''

"""
https://www.wikihow.com/Make-Coffee
暂时驾驭不了

the client of make all kinds of coffee
store
store manager

employee
customer

coffeemaker

bean
water

milk
fresh cream
糖浆 syrup
chocolate

"""

import os
import sys
import random
import weakref

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from logzero import logger as log


class DesignPatterns(object):
    dps = ['creational_patterns', 'structural_patterns', 'behavioral_patterns']
    creational_patterns = ['abstract_factory',
                           'factory',
                           'builder',
                           'prototype',
                           'singleton', ]
    structural_patterns = ['adapter',
                           'bridge',
                           'composite',
                           'decorator',
                           'facade',
                           'flyweight',
                           'proxy', ]
    behavioral_patterns = ['interpreter',
                           'template',
                           'chain_of_responsibility',
                           'command',
                           'iterator',
                           'mediator',
                           'memento',
                           'observer',
                           'state',
                           'visitor', ]

    def __init__(self, only_done=True):
        '''
        self.creational_patterns = {
            'abstract_factory': True,
            'factory': True,
            'builder': True,
            'prototype': True,
            'singleton': True,
        }

        self.structural_patterns = {
            'adapter': True,
            'bridge': True,
            'composite': True,
            'decorator': True,
            'facade': True,
            'flyweight': globals().get('test_flyweight', False),
            'proxy': False,
        }
        self.behavioral_patterns = {
            'interpreter': False,
            'template': False,
            'chain_of_responsibility': False,
            'command': False,
            'iterator': False,
            'mediator': False,
            'memento': False,
            'observer': False,
            'state': False,
            'visitor': False,
        }

        '''
        for dp in DesignPatterns.dps:
            d1 = getattr(self, dp)
            m = dict(
                zip(
                    d1,
                    [_ != None for _ in [globals().get('test_' + x) for x in d1 if x]]
                )
            )
            # 重置
            setattr(self, dp, m)

        self.done(only_done)

    def done(self, only_done=True):
        print('- ' * 16)
        c = self.creational_patterns
        s = self.structural_patterns
        b = self.behavioral_patterns
        j = 0
        l = []
        for _ in [c, s, b]:
            [l.append('{:>24}:\t'.format(k)) for k, v in _.items() if not only_done or v]
        for i, v in enumerate(l):
            print('{:>2}'.format(i), v, 'done')
        print('- ' * 16)


class Store(object):
    """咖啡店
    """

    pass


class Manager(object):
    """单例模式, 在一个咖啡店中, 有且只有一个店长
    """
    pass


'''Builder模式'''


class CoffeeBuilder(object):
    """Builder模式
    为制作 Coffee 提供各个步骤的抽象接口

    - grind_powder
    - boil_water
    - brew_method
    - serve_coffee
    # - grind_and_pack
    # - extract
    """

    def grind_powder(self):
        raise NotImplementedError

    def boil_water(self):
        raise NotImplementedError

    def brew_method(self):
        raise NotImplementedError

    def serve_coffee(self):
        raise NotImplementedError


class EspressoBuilder(CoffeeBuilder):
    """为CoffeeBuilder的具体实现: EspressoBuilder
    """

    def grind_powder(self):
        self.powder = '30g'

    def boil_water(self):
        self.water = '100ml'

    def brew_method(self):
        self.brew = 'extract'

    def serve_coffee(self):
        self.coffee = 'espresso'


class AmericanoBuilder(CoffeeBuilder):
    """为CoffeeBuilder的具体实现: 美式咖啡
    """

    def grind_powder(self):
        self.powder = '30g'

    def boil_water(self):
        self.water = '400ml'

    def brew_method(self):
        self.brew = 'brew'

    def serve_coffee(self):
        self.coffee = 'amaricano'


class MakeCoffeeDirector(object):
    """Director: 构建一个使用CoffeeBuilder接口的对象, 定义了制作步骤
    """

    def __init__(self, builder):
        self.__builder = builder
        self.make_coffee()

    def make_coffee(self):
        self.__builder.grind_powder()
        self.__builder.boil_water()
        self.__builder.brew_method()
        self.__builder.serve_coffee()

    def __repr__(self):
        __c = '{0.coffee}: has powder {0.powder}, water {0.water}, made by {0.brew}'.format(
            self.__builder)
        return __c


def test_builder():
    esp = EspressoBuilder()
    ama = AmericanoBuilder()
    cup_esp = MakeCoffeeDirector(esp)
    cup_ama = MakeCoffeeDirector(ama)
    print(cup_esp)
    print(cup_ama)


"""Builder模式 End"""

'''Simple Factory Start'''


class Coffee(object):
    """简单工厂模式, 提供get_name接口来生成各种口味咖啡
    """

    def __init__(self):
        self.name = ''

    def get_name(self):
        return self.name

    def get_recipe(self):
        raise NotImplementedError

    def __repr__(self):
        return 'coffee is: {}'.format(self.name)


class Espresso(Coffee):
    def __init__(self):
        super().__init__()
        self.name = 'espresso'
        self.espresso = 1
        self.water = 0

    def get_recipe(self):
        return '{} is made with pure espresso'.format(self.name)


class Americano(Coffee):
    def __init__(self):
        super().__init__()
        self.name = 'Americano'
        self.espresso = 1
        self.water = 2

    def get_recipe(self):
        return '{} is made with esp/water @ {}/{}'.format(self.name, self.espresso, self.water)


class FlatWhite(Coffee):
    def __init__(self):
        super().__init__()
        self.name = 'FlatWhite'
        self.espresso = 1
        self.milk = 1.5

    def get_recipe(self):
        return '{} is made with esp/milk @ {}/{}'.format(self.name, self.espresso, self.milk)


def test_factory():
    kinds = ['Americano', 'Espresso', 'FlatWhite']
    for k in kinds:
        cf = globals().get(k, Espresso)()
        print(cf)


'''Simple Factory End'''

'''Abstract Factory Start'''


class CoffeeFactory(object):
    """抽象咖啡工场, 即使有新的咖啡出现, 也无需对该类进行修改
    """

    def __init__(self, coffee_factory=None):
        self._coffee = coffee_factory

    def gen_coffee(self):
        _coffee = self._coffee()
        print('Made:', _coffee.get_name())
        print('With:', _coffee.get_recipe())
        print('*' * 32)


def test_abstract_factory():
    """ client caller
    """

    _esp_coffee = CoffeeFactory(Espresso)
    _esp_coffee.gen_coffee()

    def rand_coffee():
        return random.choice([Espresso, Americano, FlatWhite])()

    _cof = CoffeeFactory(rand_coffee)
    for i in range(5):
        _cof.gen_coffee()


'''Abstract Factory End'''

'''
class AbstractStoreFactory(object):
    """每个咖啡店都有 employee, 都有 coffee
    """

    def get_employee(self):
        raise NotImplementedError

    def get_coffee(self):
        raise NotImplementedError


class Pacific(AbstractStoreFactory):
    def get_employee(self):
        return PacificEmp()

    def get_coffee(self):
        return PacificCoffee()


class Starbucks(AbstractStoreFactory):
    def get_employee(self):
        return StarbucksEmp()

    def get_coffee(self):
        return StarbucksCoffee()


class EmployeeFactory(object):
    pass


class PacificEmp(EmployeeFactory):
    pass


class StarbucksEmp(EmployeeFactory):
    pass


class CoffeeStoreFactory(object):
    pass


class PacificCoffee(CoffeeStoreFactory):
    pass


class StarbucksCoffee(CoffeeStoreFactory):
    pass


class Cashier(EmployeeFactory):
    pass


class Waiter(EmployeeFactory):
    pass


class Waitress(EmployeeFactory):
    pass
Abstract Factory Start'''

"""
Protoype 模式 Start
直接复制, 获取备份, 然后修改使用
不需要执行构造函数, 但是在python下用处不是太大
在 python中可以直接使用 copy.copy/deepcopy 来操作
"""


class CoffeePrototype(object):
    cup = 'middle'

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._obj = {}

    def get_object(self):
        return self._obj

    def register_obj(self, name, ob):
        self._obj[name] = ob

    def unregister_obj(self, name):
        del self._obj[name]


def test_prototype():
    dis = PrototypeDispatcher()
    mid_coffee = CoffeePrototype()

    mid_esp = mid_coffee.clone()
    lit_esp = mid_coffee.clone(cup='little')
    print(mid_esp.cup, lit_esp.cup)
    import copy

    _ext_cof = copy.copy(mid_esp)
    _ext_cof.cup = 'large'
    print(_ext_cof.cup)

    dis.register_obj('cup_esp_mid', mid_esp)
    dis.register_obj('cup_esp_lit', lit_esp)

    for n, p in dis.get_object().items():
        print(n, p.cup)


"""Protype 模式 End"""

"""3 Tier
data => logic => Ui
class 咖啡库存data
class 盘点库存logic
class 老板查看UI
"""
"""3 Tier End"""

""" Adapter 模式
在不改变原来的已定类的前提下, 提供一个适配类, 让已定类可以执行共同的操作
class Employee
Employee StoreManager
    manage_employee
Employee CoffeeMaker
    make_coffee
Employee Waiter
    serve_coffee
Employee Cashier
    in_cash

所有的employee 都有工作, 但是没有一个统一的显示工作内容方法

class JobAdapter
    show_job
"""


class StoreManager(object):
    def __init__(self):
        self.name = 'manager'

    def manage_employee(self):
        return 'manage all employees'


class CoffeeMaker(object):
    def __init__(self):
        self.name = 'coffee maker'

    def make_coffee(self):
        return 'make kinds of coffees'


class Waiter(object):
    def __init__(self):
        self.name = 'waiter'

    def serve_coffee(self):
        return 'serve coffee to customers'


class JobAdapter(object):
    def __init__(self, obj, **adapted_jobs):
        """为待控制对象的方法提供对外统一接口

        :type adapted_jobs: dict
        :param adapted_jobs:
            key: 为类对外提供访问 method 的统一接口
            method: 为不同对象适用于该接口的方法
        :return:
        :rtype:

        obj {[type]} -- [待操作对象]
        """

        self.obj = obj
        self.__dict__.update(adapted_jobs)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def test_adapter():
    jobs = []
    manager = StoreManager()
    print(manager.__dict__)
    jobs.append(JobAdapter(manager, do_job=manager.manage_employee))
    print(jobs[0].__dict__)
    print(jobs[0].original_dict())

    ecm = CoffeeMaker()
    jobs.append(JobAdapter(ecm, do_job=ecm.make_coffee))

    waiter_ = Waiter()
    jobs.append(JobAdapter(waiter_, do_job=waiter_.serve_coffee))

    for _job in jobs:
        # print(_job)
        print('A {} do {}'.format(_job.name, _job.do_job()))


""" Adapter 模式 End"""

""" Bridge 模式
在 clients 调用 providers 之间增加一个 Bridge类, 该Bridge类包含 provider
这样 clients 对 providers 就不再直接调用, 而是clients请求Bridge类,
然后Bridge类会将clients请求转发到providers.
这样 clients 或者 providers 之间的改变只需要在 Bridge类 进行适配即可

现在有 咖啡机类能制作标准中杯espresso/amaricano等, 有消费者类饮用咖啡
如果没有中间的 制作咖啡类, 那么如果消费者有新要求 大杯amaricano, 则需要给咖啡机增加新配件/功能, 来制作
而增加了 抽象制作咖啡类, 消费者有新要求, 只需要在制作的时候增加合适的水和咖啡粉即可
同样小杯, 只需要减少比例就成.
"""


class Coffees(object):
    def get_coffee(self, espresso, water, cup_size):
        raise NotImplementedError


class CoffeeEspresso(Coffees):
    def get_coffee(self, espresso, water, cup_size='middle'):
        print(
            'made a {} cup of espresso, with {} espresso and {} water'.format(
                cup_size,
                espresso,
                water))


class CoffeeAmericano(Coffees):
    def get_coffee(self, espresso, water, cup_size='middle'):
        print(
            'made a {} cup of amaricano, with {} espresso and {} water'.format(
                cup_size,
                espresso,
                water))


class AbstractMakeCoffeeBridge(object):
    """ 抽象类 可以处理/转发 client请求, 以合适的方法使用现有类来完成工作
    """

    def make_coffee(self):
        raise NotImplementedError

    def resize_cup_size(self, cup_size):
        raise NotImplementedError


class MakeCoffee(AbstractMakeCoffeeBridge):
    def __init__(self, espresso, water, cup_size, making_coffee):
        self.espresso = espresso
        self.water = water
        self.cup_size = cup_size
        self.making_coffee = making_coffee

    def make_coffee(self):
        self.making_coffee.get_coffee(self.espresso, self.water, self.cup_size)

    def resize_cup_size(self, cup_size):
        self.cup_size = cup_size


def test_bridge():
    coffees = [
        MakeCoffee(1, 0, 'middle', CoffeeEspresso()),
        MakeCoffee(1, 2, 'middle', CoffeeAmericano()),
    ]
    for cf in coffees:
        cups = random.choice(['middle', 'big', 'little'])
        cf.resize_cup_size(cups)
        cf.make_coffee()


""" Bridge 模式 End"""

"""Composite 模式
暂时未找到合适的实例, 使用文件夹/文件来实现
"""


class Node(object):
    def __init__(self):
        pass

    def show(self):
        raise NotImplementedError


class Leaf(Node):
    def __init__(self):
        super().__init__()
        self.name = random.randint(1, 1000)

    def show(self):
        print('leaf:', self.name)


class Composite(Node):
    def __init__(self):
        super().__init__()
        self.name = 'A{}'.format(random.randint(1, 20))
        self.children = []

    def append_child(self, child):
        # child.show()
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def show(self):
        print('Folder:', self.name)
        print('=' * 32)
        for c in self.children:
            c.show()


def test_composite():
    cs = Composite()
    for i in range(5):
        cs.append_child(Leaf())

    cs.show()
    cs2 = Composite()
    cs2.append_child(cs)
    cs2.show()


"""Composite 模式"""

"""装饰器模式
代价很高
创建高
维护难
移除困难

咖啡店Store类
门装饰类, 边框装饰类, 地板类
"""


class Store(object):
    def draw(self, decorations):
        decorations.append('rough store')

    def info(self):
        pass


class StoreDec(object):
    def __init__(self, store):
        self.store = store

    def draw(self, decorations):
        self.store.draw(decorations)

    def info(self):
        self.store.info()


class BorderDec(StoreDec):
    def draw(self, decorations):
        self.store.draw(decorations)
        decorations.append('add bright borders')


class FloorDec(StoreDec):
    def draw(self, decorations):
        self.store.draw(decorations)
        decorations.append('add nicely floors')


def test_decorator():
    st = FloorDec(BorderDec(Store()))
    decs = []
    st.draw(decs)
    decs = ['{}. {}'.format(i + 1, x) for i, x in enumerate(decs)]
    print('\n'.join(decs))


"""装饰器模式 End
"""

"""Facade 模式
facade 模式 为一组复杂的操作对外提供一个简单的接口来实现
为一个复杂的系统, 提供一个简单的统一接口
比如: 制作一杯Latte咖啡
1. Espressos 60/250
2. Milk 180/250
3. foam 10/250
4. MakeLatte
    - add_esp
    - add_milk
    - add_foam
    - make_latte
    
5. 最终如果要制作一杯 Latte, 只需要 make_latte 就可以了
"""


class Espre(object):
    def get_vol(self, vol):
        return 'add espresso {}ml'.format(vol)


class Milk(object):
    def get_vol(self, vol):
        return 'add milk {}ml'.format(vol)


class MilkFoam(object):
    def get_vol(self, vol):
        return 'add milk foam {}ml'.format(vol)


class MakeLatteFacade(object):
    def __init__(self):
        self.esp = Espre()
        self.milk = Milk()
        self.milk_foam = MilkFoam()

        self.rate = {
            'e': 6 / 25,
            'm': 18 / 25,
            'f': 1 / 25,
        }

    def make_latte(self, total_vol=250):
        rate = self.rate
        latte_ = {
            'e': self.esp.get_vol(total_vol * rate.get('e', 6 / 25)),
            'm': self.milk.get_vol(total_vol * rate.get('m', 18 / 25)),
            'f': self.milk_foam.get_vol(total_vol * rate.get('f', 1 / 25))}
        print('{0[e]}\n{0[m]}\n{0[f]}'.format(latte_))
        print('Made A {0}ml latte'.format(total_vol))


def test_facade():
    latte = MakeLatteFacade()
    latte.make_latte(250)


"""Facade 模式 End
facade 就是集合一堆现有类, 并按照一定的逻辑拼接起来, 只对外提供一个简单的接口的实现
代价: 很简单, 无额外代价
创建: 易于创建
维护: 易于维护
移除: 易于移除
"""

"""flyweight 模式
针对大量细粒度对象来使用
一般是由于应用程序使用了大量的对象, 造成了很大的存储开销
e.g. 纸牌 Card
clubs(梅花), diamonds(方块), hearts(红桃), spades(黑桃)
"""


class Card(object):
    _CardPool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit, None)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return '<Card: {}{}>'.format(self.value, self.suit)


def test_flyweight():
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2)
    print(id(c1), id(c2))


"""flyweight 模式
"""

if __name__ == '__main__':
    dp = DesignPatterns()
    # dp.done()
    # test_builder()
    # test_factory()
    # test_abstract_factory()
    # test_prototype()
    # test_adapter()
    # test_bridge()
    # test_composite()
    # test_decorator()
    # test_facade()
    test_flyweight()

#_*_coding:utf-8_*_

'''
工厂方法模式是简单工厂模式的衍生，解决了许多简单工厂模式的问题。
首先完全实现‘开－闭 原则’，实现了可扩展。其次更复杂的层次结构，可以应用于产品结果复杂的场合。 　　
工厂方法模式的对简单工厂模式进行了抽象。有一个抽象的Factory类（可以是抽象类和接口），这个类将不在负责具体的产品生产，而是只制定一些规范，具体的生产工作由其子类去完成。在这个模式中，工厂类和产品类往往可以依次对应。即一个抽象工厂对应一个抽象产品，一个具体工厂对应一个具体产品，这个具体的工厂就负责生产对应的产品。 　　
工厂方法模式(Factory Method pattern)是最典型的模板方法模式(Templete Method pattern)应用。


'''


class CreateOperation(object):
    def get_name(self):
        return self.Operation_name

class Addition(CreateOperation):
    def __init__(self):
        self.Operation_name = 'Addition'
    def count(self):
        print("加法计算")

class Subtraction(CreateOperation):
    def __init__(self):
        self.Operation_name = 'Subtraction'
    def count(self):
        print("减法计算")

class OperationInterfaceFactory(object):
    '''接口基类'''

    def create(self):
        '''把要创建的工厂对象装配进来'''
        raise NotImplementedError              #报错后产生的问题分类是NotImplementedError

class CreateAddition(OperationInterfaceFactory):
    def create(self):
        return Addition()

class CreateSubtraction(OperationInterfaceFactory):
    def create(self):
        return Subtraction()

shape_interface = CreateAddition()
obj = shape_interface.create()
obj.get_name()
obj.count()

shape_interface2 = CreateSubtraction()
obj2 = shape_interface2.create()
obj2.count()


工厂模式

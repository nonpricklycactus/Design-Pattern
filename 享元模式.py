class FlyweightBase(object):
    _instances = dict()
    def __init__(self,*args,**kwargs):
        #继承的子类必须初始化
        raise NotImplementedError

    def __new__(cls, *args, **kwargs):
        print(cls._instances,type(cls))
        return cls._instances.setdefault(
            (cls,args,tuple(kwargs.items())),

            super(FlyweightBase,cls).__new__(cls)
        )

    def test_data(self):
        pass
class Spam(FlyweightBase):
    '''精子类'''

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def test_data(self):
        print("精子准备好了",self.a,self.b)
class Egg(FlyweightBase):
    '''卵类'''
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def test_data(self):
        print("卵子准备好了",self.x,self.y)



spam1 = Spam(1,'abc')
spam2 = Spam(1,'abc')
spam3 = Spam(3,'DEF')

egg1 = Egg(1,'abc')
print(id(spam1),id(spam2),id(spam3))

#egg2 = Egg(4,'abc')
# assert spam1 is spam2
# assert egg1 is not spam1
# print(id(spam1),id(spam2))
# spam2.test_data()
# egg1.test_data()
# print(egg1._instances)
# print(egg1._instances.keys())
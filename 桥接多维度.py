class AbstractRoad(object):
    '''公路基类'''
    car = None

class AbstractCar(object):
    '''车辆基类'''

    def run(self):
        pass

class People(object):
    pass


class Street(AbstractRoad):
    '''市区街道'''

    def run(self):
        self.car.run()
        print("在市区街道上行驶")

class SpeedWay(AbstractRoad):
    '''高速公路'''

    def run(self):
        self.car.run()
        print("在高速公路上行驶")


class Car(AbstractCar):
    '''小汽车'''
    def run(self):
        print("小汽车在")

class Bus(AbstractCar):
    '''公共汽车'''
    road = None

    def run(self):
        print("公共汽车在")



#加上人
class Man(People):
    def drive(self):
        print("男人开着")
        self.road.run()
#加上人
class Woman(People):
    def drive(self):
        print("女人开着")
        self.road.run()
if __name__ == "__main__":
    #小汽车在高速上行驶
    road1 = SpeedWay()
    road1.car = Car()
    road1.run()

    #
    road2 = SpeedWay()
    road2.car = Bus()
    road2.run()


    #人开车
    road3 = Street()
    road3.car = Car()

    p1 = Man()
    p1.road = road3
    p1.drive()

    p2 = Woman()
    p2.road = road3
    p2.drive()
# 应用组合模式的会员卡消费
#
#     那么我们就根据我们会员卡的消费，来模拟一下组合模式的实现吧！let's go！
#
#     首先：
#
#            1.我们的部件有，总店，分店，加盟店！
#
#            2.我们的部件共有的行为是：刷会员卡
#
#            3.部件之间的层次关系，也就是店面的层次关系是，总店下有分店、分店下可以拥有加盟店。
#
# 有了我们这几个必要条件后，我的要求就是目前店面搞活动当我在总店刷卡后，就可以累积相当于在所有下级店面刷卡的积分总额，设计的代码如下



class Store(object):
    '''店面基类'''


    #添加店面
    def add(self,store):
        pass
    #删除店面
    def remove(self,store):
        pass
    def pay_by_card(self):
        pass

class BranchStore(Store):
    def __init__(self,name):
        self.name = name
        self.my_store_list = []

    def pay_by_card(self):
        print("店面[%s]的积分已累加进该会员卡" %self.name)
        for s in self.my_store_list:
            s.pay_by_card()

    #添加店面
    def add(self,store):
        self.my_store_list.append(store)
    #删除店面
    def remove(self,store):
        self.my_store_list.remove(store)

class JoinStore(Store):
    '''加盟店'''
    def __init__(self,name):
        self.name = name

    def pay_by_card(self):
        print("店面[%s]的积分已累加进该会员卡" %self.name)

    def add(self,store):
        print("无添加子店权限")
    def remove(self,store):
        print("无删除子店权限")



if __name__ == "__main__":
    store = BranchStore("朝阳总店")
    branch = BranchStore("海淀分店")
    join_branch = JoinStore("昌平加盟1店")
    join_branch2 = JoinStore("昌平加盟2店")

    branch.add(join_branch)
    branch.add(join_branch2)

    store.add(branch)


    store.pay_by_card()
    print(store.my_store_list)


# 这样在累积所有子店面积分的时候，就不需要去关心子店面的个数了，也不用关系是否是叶子节点还是组合节点了，也就是说不管是总店刷卡，还是加盟店刷卡，都可以正确有效的计算出活动积分。
#
# 什么情况下使用组合模式
#
# 引用大话设计模式的片段：“当发现需求中是体现部分与整体层次结构时，以及你希望用户可以忽略组合对象与单个对象的不同，统一地使用组合结构中的所有对象时，就应该考虑组合模式了。”
#
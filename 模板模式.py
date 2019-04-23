class Register(object):
    '''用户注册接口'''

    def register(self):
        pass
    def login(self):
        pass

    def auth(self):
        self.register()
        self.login()

class RegisterByQQ(Register):
    '''qq注册'''

    def register(self):
        print("---用qq注册-----")

    def login(self):
        print('----用qq登录-----')



class RegisterByWeiChat(Register):
    '''微信注册'''

    def register(self):
        print("---用微信注册-----")

    def login(self):
        print('----用微信登录-----')


if __name__ == "__main__":

    register1 = RegisterByQQ()
    register1.auth()

    register2 = RegisterByWeiChat()
    register2.auth()
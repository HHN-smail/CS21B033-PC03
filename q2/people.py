class People:
    options = [1,-1] # 1 is corperate, -1 is cheat
    def __init__(self,name):
        self.name = name
        self.coin = 0

class A(People):
    def __init__(self,name):
        super().__init__(name)
    
    def choose(self):
        return -1

class B(People):
    def __init__(self,name):
        super().__init__(name)
    
    def choose(self):
        return 1

class C(People):
    def __init__(self,name):
        super().__init__(name)
        self.enemy_response = [1]
        
    
    def save_enemy_response(self,response):
        self.enemy_response.append(response)

    def choose(self):
            return self.enemy_response[-1]

if __name__ =='__main__':
    a = A('a')
    b= type(a)('b')
    print(b)
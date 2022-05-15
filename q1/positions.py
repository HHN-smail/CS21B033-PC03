import random
class Position:
    @classmethod
    def set_universe(cls, universe):
        cls.universe = universe
        print('defining universe for all the positions')
        print('If we used CPP we could just refer to the universe, I am not sure how to reference in python')

    def __init__(self,x,y, move_schema):
        self.x = x
        self.y = y
        self.move_schema= move_schema

    def move(self, direction):
        oldPos = (self.x, self.y)

        if self.move_schema == 1: # 1 means that the player can move in NEWS direction
            if direction == "N":
                self.y += 1
            elif direction == "S":
                self.y -= 1
            elif direction == "W":
                self.x -= 1
            elif direction == "E":
                self.x += 1
            else:
                print("Error: Invalid direction")
                return False
            try:
                self.previous_pos.append((self.x, self.y))
            except:
                pass
            Position.universe.update_universe(self, oldPos)
            return True

    # def move_schema2(self, direction):
        elif self.move_schema == 2: # 2 means that the player can move in any direction
            x= self.x
            y=self.y
            if (len(direction) ==2 or len(direction) == 1):
                for i in direction:
                    if i == "N":
                        y += 1
                    elif i == "S":
                        y -= 1
                    elif i == "W":
                        x -= 1
                    elif i == "E":
                        x += 1
                    else:
                        print("Error: Invalid direction")
                        return False
            else:
                print("Error: Invalid direction")
                return False
            self.x = x  
            self.y = y
            # if we recieve NX as direction the moment is invalid, neither x or y changes
            return True
        
        else:
            #no move schema defined, for pond, food, etc
            return False





class Insect(Position): #organism named as insect
    def __init__(self,x,y,vision_distance, move_schema = 1 ):
        super().__init__(x,y, move_schema = 1)
        self.predator_list = [Spider]
        self.prey_list = [Grass, Water]
        self.vision_distance = vision_distance
        self.move_schema = move_schema
        Position.universe.update_universe(self)
        self.subuniverse = Position.universe.get_subuniverse_manhatten(self.x,self.y, vision_distance)
        self.previous_pos = [(self.x, self.y)]
    def update_subuniverse_manhatten(self,subuniverse):
        self.subuniverse = subuniverse
    
    def hunt(self):
        if(not self.subuniverse):
            print("Error: subuniverse not defined")
        preyFound = False
        for i in self.subuniverse:
            for j in i:
                if isinstance(j, tuple(self.prey_list)):
                    self.move_towards_manhatten(j)
                    preyFound = True
                    return
        if not preyFound:
            # print("No prey found")
            possible_moves = ["N","S","E","W"]
            if self.x == 0:
                possible_moves.pop(3)
            if self.y == 0:
                possible_moves.pop(1)
            if self.x == Position.universe.n-1:
                possible_moves.pop(2)
            if self.y == Position.universe.n-1:
                possible_moves.pop(0)
            self.move(possible_moves[random.randint(0,3)])
                


    def move_towards_manhatten(self,j):
        # j is Position class
        if self.x > j.x:
            self.move("W")  
        elif self.y > j.y:
            self.move("S")
        elif self.x < j.x:
            self.move("E")
        elif self.y < j.y:
            self.move("N")
        else:
            print("at the same position")

        self.update_subuniverse_manhatten(Position.universe.get_subuniverse_manhatten(self.x,self.y, self.vision_distance))
        # Position.universe.update_universe(Insect(self.x,self.y,self.vision_distance, self.move_schema))


    def move_towards_cartesian(self,j):
        # j is position class
        pass
    



class Spider(Position):  #predator named as spider
    def __init__(self,x,y, vision_distance, move_schema = 1):
        super().__init__(x,y, move_schema)
        self.predator_list = []
        self.prey_list = [Insect, Grass, Water]

class Grass(Position): #food named as grass
    def __init__(self,x,y, move_schema = 0):
        self.x = x
        self.y = y
        super().__init__(x,y, move_schema = 0)
        self.predator_list = [Insect, Spider]
        self.prey_list = []

class Water(Position): #pond/water named as water
    def __init__(self,x,y, move_schema = 0):
        super().__init__(x,y, move_schema)
        self.predator_list = [Insect, Spider]
        self.prey_list = []



class Empty(Position):
    def __init__(self,x,y, move_schema = 0):
        super().__init__(x,y, move_schema = 0)
        self.predator_list = []
        self.prey_list = [] 



if __name__ == '__main__':
    pass
import random
import positions
class Universe:
    def __init__(self, n , k ):
        self.n = n
        self.k = k

    def __str__(self):
        return_string = ""
        for i in self.universe:
            for j in i:
                if  isinstance(j, positions.Empty):
                    return_string += "0 "
                elif isinstance(j, positions.Grass):
                    return_string += "1 "
                elif isinstance(j, positions.Insect):
                    return_string += "2 "
            return_string += "\n"
        return return_string


    @classmethod
    def generate_random_universe(cls, n, k):
        universe = cls(n, k)
        universe.food = (tuple(zip(random.sample(range(n), k), random.sample(range(n), k))))
        print("""Using this randomisation technique we won't get 2points we same x cordinate or y cordinate.
        all points have unique x and unique y, we ignore this fact and can be patched later on if needed.""")
        return universe

    def populateFood(self, positions_of_food ):
        # positions_of_food === [(1,2), (3,4), (5,6)] and should have k tupples
        if len(positions_of_food) != self.k:
            print(f"Error: Number of food positions should be equal to {self.k}")
            return False

        for i in positions_of_food:
            if type(i) != tuple :
                print(f"Error: Food positions should be tuples")
                return False
            if len(i) != 2:
                print(f"Error: Food positions should be tuples with 2 integer elements <= {self.n}")
                return False
            for j in i:
                if type(j) != int:
                    print(f"Error: Food positions should be tuples with 2 integer elements <= {self.n}")
                    return False
                if j < 0 or j > self.n:
                    print(f"Error: Food positions should be tuples with 2 integer elements <= {self.n}")
                    return False
        
        self.food = positions_of_food
        for i in positions_of_food:
            self.update_universe(positions.Grass(i[0],i[1]))
        return True

    def update_universe(self,new_state,oldPos = False):
        if (not self.universe):
            self.render_universe()
        try:
            if type(self.universe[new_state.x][new_state.y]) == positions.Empty:
                self.universe[new_state.x][new_state.y] = new_state
            elif type(self.universe[new_state.x][new_state.y]) in new_state.prey_list:
                self.universe[new_state.x][new_state.y] = new_state
            else:
                self.universe[new_state.x][new_state.y] = new_state
            if oldPos:
                self.universe[oldPos[0]][oldPos[1]] = positions.Empty(oldPos[0],oldPos[1])
            else:
                pass
                # print('no old pos')
        except IndexError:
            # print("Error: Universe is too small")
            pass



    def render_universe(self):
        print(""" we store the entire universe in our memory as a matrix. I realise this may not be the best way to do it depending on the use case.
        If we only have a single iteration of the universe used by all the players (kind of like r/place) then it might be better to store the entire universe in memory. 
        But if players can create lobbies and join them, storing the entire universe on our server may not be the best approach, especially when n is large. """)


        self.universe = []
        for i in range(self.n):
            self.universe.append([])
            for j in range(self.n):
                self.universe[i].append(positions.Empty(x = i, y = j))
        # self.universe[x][y] represents the (x,y) cordinate


        
    
    def get_subuniverse_manhatten(self, x, y, radius):
        # should have created a subuniverse class and returned object instead of list
        subuniverse = []
        if ( not self.universe):
            self.render_universe()
            # |x1-x| + |y1-y| <= radius
        for i in range(0, radius+1):
            subuniverse.append([])
            for x1 in range(x-i, x+i+1):
                try:
                    subuniverse[i].append(self.universe[x1][y-i + abs(x1-x)])
                except Exception as e:
                    # print(e) #for testing, delete in final commit
                    pass
                try:
                    subuniverse[i].append(self.universe[x1][y+i - abs(x1-x)])
                except Exception as e:
                    # print(e) #for testing, delete in final commit
                    pass
        return subuniverse
        # first sublist of subuniverse has positions at distance 0 (the organism itself), second at distance 1, etc.







if __name__ == '__main__':
    universe = Universe.generate_random_universe(n=1000,k=500) #change the values of n and k as per your preference
    positions.Position.set_universe(universe) 
    universe.render_universe()
    universe.populateFood(universe.food)   
    org1 = positions.Insect(1,1,100) #change the values of x,y and view distance as per your preference
    file = open('./q1/universe.txt', 'w')
    for p in range(100): #change the number of iterations as per your preference
        # longer iterations is taking much longer to run, ~1 second per iteration 
        print(p)
        org1.hunt()
        file.write(universe.__str__())
        file.write('\n' * 10)

    file.write(repr(org1.previous_pos))
    file.close()




            

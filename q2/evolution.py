import tryouts
import people
import random

class Evolution:
    def __init__(self, typeA, typeB, typeC):
        self.typeA = [people.A(str(i)) for i in range(typeA)]
        self.typeB = [people.B(str(i)) for i in range(typeB)]
        self.typeC = [people.C(str(i)) for i in range(typeC)]
        self.all_people = sorted([self.typeA + self.typeB + self.typeC][0], key=lambda x : x.coin, reverse=True)

    def __str__(self):
        typeA = 0
        typeB = 0
        typeC = 0
        for i in self.all_people:
            if isinstance(i, people.A):
                typeA += 1
            elif isinstance(i, people.B):
                typeB += 1
            elif isinstance(i, people.C):
                typeC += 1
        return f"typeA : {typeA} \ntypeB : {typeB}  \ntypeC : {typeC} \n \n \n \n \n "

    def evolve(self):
        for i in range(len(self.all_people)):
            for j in range(i):
                tryouts.Tryout(self.all_people[i], self.all_people[j]).tourney(iterations = 10)
        self.all_people.sort(key=lambda x : x.coin, reverse=True)
        for i in range(5):
            # executing the failures
            self.all_people.pop(-1)
        for i in range(5):
            #  multiply at victors
            self.all_people.append(type(self.all_people[i])(self.all_people[i].name))
            # name of people does not matter
        self.iteration = self.iteration + 1

    def checkHomogeneity(self):
        for i in range(len(self.all_people)-1):
            if type(self.all_people[i]) != type(self.all_people[i +1]):
                return False
        return True


    def run(self):
        self.iteration = 0
        for i in range(20):
        # while(True):
            if(self.checkHomogeneity()):
                break
            self.evolve()
            print(str(self))


if __name__ == '__main__':
    file = open("./q2/evolution.txt", "w")
    for i in range(26):
        for j in range(26-i):
            ev = Evolution(i,j,25-i-j)
            ev.run()
            file.write(f"type A : {i} type B : {j} type C : {25-i-j} \n")
            file.write(str(ev))
            file.write("\n")
            file.write("\n")
            file.write("\n")

    file.close()
    # ev = Evolution(10,10,10) # enter values of A,B,C
    # ev.run()

    """
    if assume that for every new tourney C clears enemy's response (each tourney has 10 matches)
    106 matches where domination is seen, 6 for B, 39 for A, 61 for C
    """
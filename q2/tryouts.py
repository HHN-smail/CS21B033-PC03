import people
class Tryout:
    def __init__(self, person1, person2):
    # person1 and person2 are objects of class A, B or C
        self.person1 = person1
        self.person2 = person2

    def __str__(self):
        self.tourney()
        return f"{self.person1.name} has {self.person1.coin} coins and {self.person2.name} has {self.person2.coin} coins"

    def play(self):
        person1_response = self.person1.choose()
        person2_response = self.person2.choose()
        if isinstance(self.person1, people.C):
            self.person1.save_enemy_response(person2_response)
        elif isinstance(self.person2, people.C):
            self.person2.save_enemy_response(person1_response)
        else:
            pass    

        if person1_response == person2_response:
            if person1_response == 1:
                self.person1.coin += 2
                self.person2.coin += 2
        else:
            if person1_response == -1:
                # if person 1 cheats he gets 3 coins and person2 looses a coin
                self.person1.coin += 3
                self.person2.coin -= 1
            else:
                # if person 2 cheats he gets 3 coins
                self.person2.coin += 3
                self.person1.coin -= 1


    def tourney(self,iterations = 10):
        for i in range(10):
            self.play()
        if type(self.person1) == people.C:
            self.person1.enemy_response = [1]
        if type(self.person2) == people.C:
            self.person2.enemy_response = [1]

if __name__ == '__main__':
    allison = people.A("allison")
    brody = people.B("brody")
    cameron = people.C("cameron")

    tryout1 = Tryout(allison, brody)
    print(tryout1)
    tryout2 = Tryout(brody, cameron)
    print(tryout2)
    tryout3 = Tryout(cameron, allison)
    print(tryout3)

    # allison has 30 coins and brody has -10 coins
    # brody has 10 coins and cameron has 20 coins
    # cameron has 19 coins and allison has 33 coins
    # being nice always works out :)


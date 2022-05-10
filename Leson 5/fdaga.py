
class Hero:
    print("Hi")
    def __init__(self,name,age,race,height):
        self.name = name
        self.age = age
        self.race = race
        self.height = 180
    
    def show(self):
        print(self.name)
        print(self.age)
        print(self.race)
        print(self.height)

class elves(Hero):
    pass

class gnomes(Hero):
    pass

class magicians(Hero):
    pass 

nick = elves()
stas = gnomes()
kiril = magicians()

First = Hero(name=(input("Твоє Імя: ")),age=(input("Скільки тобі років: ")),Race=(input("Веди свою расу: ")))
First.show()
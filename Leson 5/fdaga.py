class Hero:
    print("Hi")
    amount_students = 0
    def __init__(self,name,age,power,Race):
        self.name = name
        self.age = age
        self.power = power
        self.Lvl = 1
        self.Race = Race

        print("i am alive!")
        Hero.amount_students += 1

    def show(self):
        print(self.name)
        print(self.age)
        print(self.Lvl)
        print(self.power)
        print(self.Race)

First = Hero(name=(input("Твоє Імя: ")),age=(input("Скільки тобі років: ")),power=(input("Веди свою силу: ")),Race=(input("Веди свою расу: ")))
First.show()

Second = Hero(name=(input("Твоє Імя: ")),age=(input("Скільки тобі років: ")),power=(input("Веди свою силу: ")),Race=(input("Веди свою расу: ")))
Second.show()

print(Hero.amount_students)
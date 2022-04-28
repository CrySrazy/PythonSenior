import random

class Student:
    
    def __init__(self,name,money):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 1000

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def to_hunter(self):
        print("I am cool, i am hunter")
        self.gladness += 1
        self.progress += 0.1

    def to_go_market(self):
        print("money its water")
        self.gladness += 2
        self.progress += 0.1
        self.money -= 3

    def to_eat(self):
        print("Nyam Nyam")
        self.gladness += 2
        self.progress += 0.1
    
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Student is Einsthein")
            self.alive = False

    def end_of_day(self):
        print(f"Gladnes = {self.gladness}")
        print(f"Progress = {round(self.progress)}")

    def live(self,day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live = random.randint(1,4)
        if live == 1:
            self.to_study()
        elif live == 2:
            self.to_sleep()
        elif live == 3:
            self.to_chill()
        elif live == 4:
            self.to_eat()
        self.end_of_day()
        self.is_alive()

first_student = Student(name = input("Name your student: "))

for day in range(365):
    if first_student.is_alive == False:
        break
    first_student.live(day)
    input("Prees Enter to contine...")
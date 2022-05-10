# class Human:
#     height = 180

# class Student(Human):
#     satiety = 10

# class Wolker(Human):
#     satiety = 10

# nick = Student()
# stas = Wolker()

# print(nick.satiety)
# print(stas.satiety)

# #------------------------------------------

# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60

# class Parent(Grandparent):
#     age = 40

# class Child(Parent):
#     height = 150
#     def __init__(self):
#         print(self.height)
#         print(self.age)
#         print(self.satiety)

# nick = Child()

# #--------------------------------------------

# class Hello:
#     def __init__ (self):
#         print("Hello!")

# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__
#         print("World")

# hi = Hello_World

#---------------------------------------------

class Coumputer:
   def __init__(self):
       super().__init__
       self.memory = 128

class Display:
    def __init__(self):
        super().__init__
        self.resolution = "4k"

class SmartPhone(Coumputer,Display):
    def show(self):
        print(self.memory)
        print(self.resolution)

phone = SmartPhone()
phone.show
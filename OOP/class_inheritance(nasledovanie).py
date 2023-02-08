# class Pet:
#     def __init__(self,name = None):
#         self.name = name
#
#
# class Dog(Pet):
#     def __init__(self,name = None, breed = None):
#         super().__init__(name)  # вызываем из родительского класса метод инициализации
#         self.breed = breed
#     def say(self):
#         return f"{self.name} ({self.breed}) say : 'wow wow!'"
#
# class Byrd(Pet):
#     def __init__(self,  weight, color, name =None):
#         super().__init__(name)
#         self.weight = weight
#         self.color = color
#
#     def __str__(self):
#         return f"{self.name} with {self.weight} kg, {self.color}"
#
# class Franky(Dog,Byrd):
#     def __init__(self,name,breed,weight,color):
#         super().__init__(name, breed)
#         Byrd.__init__(weight,color)
#
#         print(self.name,self.weight,self.breed,self.color)
# barbos = Dog('Barbos','chihuahua')
# print(barbos.say())
#
# chikchirik = Byrd('Chikrik',0.1,'red')
# print(chikchirik)
# frank = Franky('fr','chihuhu',123,'red')
#------------------------------------------------------------------------------
# Задача на грузовую и легковую машину с собственными атрибутами, наследуемых от общего родителя

class Car:
    def __init__(self,mark):
        self._mark = mark
    #
    def __str__(self):
        return self.__class__.__name__
    def show_mark(self):
        print('Mark:', self._mark, self)
    def ride(self):
        print('>>>In driving mode<<<')

    def stop(self):
        print('>>>Stop mode<<<')


class Cargo(Car):
    def __init__(self, mark, occupancy = 0):
        super().__init__(mark)
        self.occupancy = occupancy

    def load(self):
        print('>>>Loading<<<')

    def unload(self):
        print('>>>Unloading<<<')

class Passenger(Car):
    def __init__(self,mark,hpower):
        super().__init__(mark)
        self.power = hpower

    def jump(self):
        print('--JUUUUUUMMP--')

shelby = Car('chevrolet')

shelby.show_mark()
shelby.ride()
shelby.stop()

print('-------------------------------------------')
scania = Cargo('Scania',400)
scania.show_mark()
scania.ride()
scania.stop()
print('Occupancy:',scania.occupancy)
scania.load()
scania.unload()
print((scania.__dict__))

print('\n---------------------------------\n')

maybach = Passenger('Scania',400)
maybach.show_mark()
print('Hourse powers:',maybach.power)
maybach.jump()
print(maybach.__dict__)
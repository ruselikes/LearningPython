from random import randint
class Planet:

    count = 0
    def __init__(self,_name):
        self.name = _name
        Planet.count +=1
    '''Если print(<экземпляр класса>) - то теперь будет выводиться его поле-имя. 
    иначе: __main__.Planet'''
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"

solar_system = []
planets_names = ("Меркурий","Венера","Земля","Марс","Юпитер","Сатурн","Уран","Нептун")

for name in planets_names:
    planet = Planet(name)
    solar_system.append(planet)

print(Planet.count)

class House:
    '''Class for description of certain House iclude: Number, Counts of floors, Color, Having balcon'''
    def __init__(self, _floor_count, _color = None,_have_balcon = True, _number = None):

        self.number = randint(0,100) or _number
        self.floor_count = _floor_count
        self.have_balcon = _have_balcon
        self.color = _color or 'uncolor'
    def __repr__(self):
        return f"№: {self.number}F: {self.floor_count},C: {self.color},B: {self.have_balcon}\n"

    def __str__(self):
        return f"№: {self.number} Floors: {self.floor_count},Color: {self.color},Balcon: {self.have_balcon}\n"

    def increase_count_floors(self,incr_count):
        self.floor_count += incr_count



print(House.__doc__)
rus_h = House( 15,'синий',False)
dasd = House(321)
print('dasd',dasd)
dasd.increase_count_floors(45)
print('new dasd',dasd)


print(rus_h,'\n\n')
colors = ['синий','черный','красный','белый']
houses = []

for _ in range(5):
    hb = True
    house = House(randint(1,10),colors[randint(0,3)],hb)
    houses.append(house)

print(houses)


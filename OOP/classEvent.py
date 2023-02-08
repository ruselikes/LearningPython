import re
class Event:

    EventInstancesList = []
    def __init__(self,description,date):
        self._description = description
        self._date = date
        Event.EventInstancesList.append(self)

    def __repr__(self):
        # date_test = re.split(" - | . | /", self.date)
        date = self._date.split('-')
        d,m,y = date

        return f"Event's description: {self._description},\nDate:\nD: {d}, M: {m}, Y: {y}"

    description = property()
    @description.setter
    def description(self,description):
        self._description = description

    @description.getter
    def description(self):
        return self._description

    @description.deleter
    def description(self):
        del self._description

    @property
    def date(self):
        return self._date

    @classmethod
    def from_string(cls,string):
        data  = string.split(":")
        description, date = data
        return cls(description,date)


class SecondEvent(Event):
    pass


event1 = Event.from_string('day of birthday:11-02-2002')
print(event1,'\n', event1.__dict__)
event1.description = 'Try to redefine description of event1'
print(event1,'\n', event1.__dict__)

# print(SecondEvent.__mro__)#выводит иерархию классов. method resolution order


#
# a = event1.from_string('birthday:12-02-2202')
# print('a',a,'\n')
#
# ev2 = Event('test','13-01-2023')
# print('usual init\n',ev2, '\n')
#
# b = ev2.from_string('test:14-02-0222')
# print('b-ev2 after from string', b, '\n')
#
# print('ev2\n',ev2)
#
# print('\n\nList of instances')
# print(Event.EventInstancesList)
#
# del_instance = Event('aaa','10-32-2002')
# print('\n',del_instance)
# del del_instance.date
# print(del_instance.__dict__)

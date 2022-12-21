
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self, name):
        print(f'{name} Hello world')


class Emploee(Person):
    def say_by(self, name):
        print(f'{name} Hello world')

person = Person('Yurii', 54)
emploee = 



if __name__ == '__main__':
    print(person.say_hi('Vasy'))

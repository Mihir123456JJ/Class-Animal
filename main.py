from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class monkey(Animal):
    def move(self):
        print("I am a arboreal animal")
class rabbit(Animal):
    def move(self):
        print("I can run Fast!")
one=monkey()
one.move()                    
two=rabbit()
two.move()

class Fish:
    def swim(self):
        print("fish is swimming")
    def eat(self):
        print("fish is eating")

fish=Fish()
fish.swim()
fish.eat()


#constructor override

class Game:
    def __init__(self,name):
        self.name=name
    def start(self):
        print(self.name,"has started")
    def stop(self):
        print(self.name,"has stopped")

game=Game("Simcity")
game.start()
game.stop()       
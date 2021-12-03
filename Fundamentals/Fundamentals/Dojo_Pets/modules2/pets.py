class Pet():
    # implement __init__( name , type , tricks ):
    def __init__( self , name, type, tricks, energy = 100000, health = 100 ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
    # implement the following methods:
    def show_stats(self):
        print(f"Name: {self.name}\nType: {self.type}\nTricks: {self.tricks}\nEnergy: {self.energy}\nHealth: {self.health}\n")
        return self
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print (f"{self.name}: zZzZzZzZ...")
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print (f"{self.name}: Nom Nom Nom")
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.noise()
        self.show_stats()
    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name}: Woof Woof!!!")
        return self
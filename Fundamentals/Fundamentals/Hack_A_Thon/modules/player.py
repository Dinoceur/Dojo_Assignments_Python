
class Player:
    def __init__( self , name, strength = 25, speed = 3, health = 100 ):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats( self ):
            print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
            return self

    def heal(self):
        self.health += 10
        self.shout()
        self.show_stats()

    def shout(self):
            print("I'm a basic npc...blah")
            return self
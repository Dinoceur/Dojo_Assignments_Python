
class Ninja():
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__( self , first_name, last_name, pet, treats = 3, health = 100 ):
        self.first = first_name
        self.last = last_name
        self.pet = pet
        self.treats = treats
        self.health = health    	
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        self.pet.show_stats()
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        self.pet.show_stats()
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()


from modules.player import Player
from modules.ninja import Ninja, Sword_Ninja, NinjaStar_Ninja, Nunchaku_Ninja
from modules.pirate import Pirate, Sword_Pirate , Blunderbuss_Pirate, Axe_Pirate 
from random import randint, choice


class The_Showdown:
    def __init__(self, player1, player2):
        self.players = [ player1 , player2 ]
        self.win = False

    def attack(self, attacker, opponent):
        attack = randint(attacker.speed, attacker.strength)
        defend = randint(opponent.speed, opponent.strength)
        if attack < defend:
            attacker.grunt()
            opponent.heal()
        else:
            if attack == attacker.strength:
                attack += 10              
            opponent.health -= attack
            print(f"{attacker.name} did {attack} damage")

    def declare_victor(self, first, second):
        if first.health <= 0:
            second.show_stats().victory()
        else:
            first.show_stats().victory()


    def fight(self):
        first = choice(self.players)
        if first == self.players[0]:
            second = self.players[1]
        else:
            second = self.players[0]
        while self.win == False:
            if first.health <= 0 or second.health <= 0:
                self.win = True
                self.declare_victor(first,second)
                break
            self.attack(first, second)
            self.attack(second, first)


fighter1 = NinjaStar_Ninja(input("Enter Player 1 Name: "))
fighter2 = Blunderbuss_Pirate(input("Enter Player 2 Name: "))

war = The_Showdown(fighter1,fighter2)

war.fight()
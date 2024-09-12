# game_engine.py

from player import Player
from room import Room
from item import Item
from character import Character

class GameEngine:
    def __init__(self):
        self.player = None
        self.rooms = {}
        self.setup_game()

    def setup_game(self):
        # Create rooms
        street = Room("You are on a busy street. You see a casino to the east.")
        alley = Room("You are in a dark alley. There might be something valuable here.")
        casino = Room("You enter the casino. The dealer is ready for you.")
        back_room = Room("You find a secret back room. There might be hidden chips here.")

        # Connect rooms
        street.connect("east", casino)
        street.connect("north", alley)
        alley.connect("south", street)
        casino.connect("west", street)
        casino.connect("north", back_room)
        back_room.connect("south", casino)

        # Create characters
        dealer = Character("Dealer", "Welcome to the blackjack table. Win $200 to leave with the prize!")

        # Add characters to rooms
        casino.add_character(dealer)

        # Create items (chips)
        chip_10 = Item("10-dollar chip", "A small chip worth $10.", 10)
        chip_50 = Item("50-dollar chip", "A valuable chip worth $50.", 50)
        chip_100 = Item("100-dollar chip", "A highly valuable chip worth $100.", 100)

        # Add items to rooms
        alley.add_item(chip_10)
        back_room.add_item(chip_50)
        back_room.add_item(chip_100)

        # Store rooms
        self.rooms["street"] = street
        self.rooms["alley"] = alley
        self.rooms["casino"] = casino
        self.rooms["back_room"] = back_room

        # Set player's starting room
        self.player = Player(input("Enter your name, gambler: "))
        self.player.current_room = street

    def play(self):
        while True:
            self.player.current_room.describe()
            option_map = self.player.current_room.list_options()

            choice = input("> ")

            if choice in option_map:
                action, target = option_map[choice]

                if action == "move":
                    self.player.move(target)
                elif action == "talk":
                    # Here we call interact on the character in the current room
                    if target in self.player.current_room.characters:
                        self.player.current_room.characters[target].interact(self.player)
                    else:
                        print(f"There is no one named {target} here.")
                elif action == "take":
                    if target in self.player.current_room.items:
                        item = self.player.current_room.items.pop(target)
                        self.player.pick_item(item)
                    else:
                        print(f"There is no {target} here.")
                elif action == "show_inventory":
                    self.player.show_inventory()
                elif action == "quit":
                    print("Thanks for playing!")
                    break
            else:
                print("Invalid choice, please try again.")

            if self.player.check_win():
                print("Congratulations! You've won $200! You win the game!")
                break

if __name__ == "__main__":
    game = GameEngine()
    game.play()

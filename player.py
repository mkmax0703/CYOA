# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.money = 0
        self.current_room = None
        self.bet = 0  # Store the current bet amount

    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way.")

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}.")
        self.money += item.value
        print(f"You now have ${self.money}.")

    def show_inventory(self):
        if self.inventory:
            print("You have the following items:")
            for item in self.inventory:
                print(f"- {item.name} (${item.value})")
        else:
            print("Your inventory is empty.")

    def gamble(self, bet):
        self.bet = bet  # Store the current bet

    def check_money(self):
        return self.money

    def check_win(self):
        return self.money >= 200

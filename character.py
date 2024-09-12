# character.py

import random

class Character:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def interact(self, player):
        print(f"{self.name} says: '{self.dialogue}'")
        if self.name == "Dealer":
            self.blackjack(player)

    def blackjack(self, player):
        print("Starting blackjack...")

        # Ensure the player places a bet before drawing hands
        while True:
            try:
                bet = int(input(f"You have ${player.money}. How much would you like to bet? "))
                if bet > player.check_money():
                    print("You don't have enough money to place this bet.")
                elif bet <= 0:
                    print("Please enter a valid bet amount.")
                else:
                    player.gamble(bet)  # Set the bet for the round
                    break
            except ValueError:
                print("Invalid bet amount. Please enter a valid number.")

        # Simple deck of cards with values (ignore suits for simplicity)
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

        def deal_card():
            return deck.pop(random.randint(0, len(deck) - 1))

        def hand_value(hand):
            value = sum(hand)
            # Convert Ace from 11 to 1 if hand is over 21
            aces = hand.count(11)
            while value > 21 and aces:
                value -= 10
                aces -= 1
            return value

        # Deal initial hands
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        print(f"Your cards: {player_hand}, total: {hand_value(player_hand)}")
        print(f"Dealer's showing: {dealer_hand[0]}")

        # Player turn
        while True:
            action = input("Would you like to Hit or Stand? (hit/stand): ").lower()
            if action == "hit":
                player_hand.append(deal_card())
                print(f"Your cards: {player_hand}, total: {hand_value(player_hand)}")
                if hand_value(player_hand) > 21:
                    print("You busted!")
                    player.money -= player.bet  # Player loses bet
                    print(f"You now have ${player.money}.")
                    return
            elif action == "stand":
                break
            else:
                print("Invalid action. Please type 'hit' or 'stand'.")

        # Dealer turn
        print(f"Dealer's cards: {dealer_hand}, total: {hand_value(dealer_hand)}")
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card())
            print(f"Dealer hits. Dealer's cards: {dealer_hand}, total: {hand_value(dealer_hand)}")

        # Determine outcome
        player_total = hand_value(player_hand)
        dealer_total = hand_value(dealer_hand)

        if dealer_total > 21:
            print("Dealer busted! You win!")
            player.money += player.bet  # Player wins bet
        elif player_total > dealer_total:
            print(f"You win with {player_total} against dealer's {dealer_total}!")
            player.money += player.bet  # Player wins bet
        elif player_total < dealer_total:
            print(f"Dealer wins with {dealer_total} against your {player_total}.")
            player.money -= player.bet  # Player loses bet
        else:
            print(f"It's a tie with {player_total}. No money lost or won.")

        print(f"You now have ${player.money}.")

        if player.money <= 0:
            print("You're out of money. Maybe you should go find more chips.")

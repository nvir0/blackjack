import random
print("Blackjack")

"""This program will let you play blackjack"""

# Dealer cards
# Player cards
# Deal the cards
# Sum dealer's cards
# Sum player's cards
# Compare dealer's hand to player's hand
    # case 0: if the sum is greater than 21 = BUST
    # case 1: if P card sum is less than 21: option Hit or option Stay
    # case 2: if P Hit add deal another card
    # case 3: if P Stay compare sum of D vs sum P
    # case 4: if P sum < 21 && P > D then P wins
    # case 4.5: if P sum == 21 then P wins
    # case 5: if P sum < D then P loses

deck = []
dealer = []
player = []

def fill_the_deck():
     #number_of_decks = int(input("How many decks? "))
    number_of_decks = 1
    for i in range(1, 4*number_of_decks+1):
        for j in range(2,14):
            if j > 11:
                deck.append(10)
            else:
                deck.append(j)

    random.shuffle(deck)

def deal_dealer():
    dealer.append(deck[0])
    deck.pop(0)

def deal_player():
    player.append(deck[0])
    deck.pop(0)

def player_cards():
    print("You have a total of " + str(sum(player)) + " from these cards: " + str(player).strip('[]'))

def dealer_cards():
    print("Dealer has a total of " + str(sum(dealer)) + " from these cards: " + str(dealer).strip('[]'))

def dealer_forced():
    if sum(dealer) <= 16:
        deal_dealer()
    

fill_the_deck()
while len(dealer) != 2:
    deal_player()
    deal_dealer()
print("Dealer has X, " + str(dealer[1]))
player_cards()

if sum(player) == 21:
    print("You have a blackjack! You win!")
elif sum(player) > 21:
    print("You have busted!")
elif sum(dealer) == 21:
    print("Dealer has 21 and wins")
elif sum(dealer) > 21:
    print("Dealer has busted!")

while sum(player) < 21:
    action_taken = str(input("Do you want to hit or stay? H/S: "))
    if sum(dealer) == 21:
        dealer_cards()
        print("Dealer has a blackjack and wins!")
        break
    elif sum(dealer) > 21:
        dealer_cards()
        print("Dealer has busted!")
        break
    else:
        if action_taken == "H" or action_taken == "h":
            deal_player()
            player_cards()
            dealer_forced()
            dealer_cards()
            if sum(player) > 21:
                print("You have busted!")
                break
            elif sum(player) == 21:
                print("You have a blackjack! You win!")
                break
            elif sum(dealer) > 21:
                print("Dealer has busted!")
                break
            elif sum(dealer) == 21:
                print("Dealer has blackjack and wins!")
                break
        elif action_taken == "S" or action_taken == "s": 
            player_cards()
            dealer_forced()
            dealer_cards()
            if sum(dealer) == sum(player):
                print("It's a push!")
                break
            elif sum(dealer) > 21: 
                print("Dealer has busted!")
                break
            elif sum(dealer) == 21:
                print("Dealer has a blackjack! Dealer wins!")
                break
            elif sum(dealer) > sum(player):
                print("Dealer wins!")
                break
            else:
                print("You win!")
                break
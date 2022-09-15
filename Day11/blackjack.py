import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5,6, 7, 8, 9, 10, 10, 10]

def random_card():
    """Returns a random card in cards array"""
    return random.choice(cards)

cardOne = random_card()
cardTwo = random_card()
print(f"\nHand one: {cardOne}")
print(f"Hand two: {cardTwo}")

dealerOne = random_card()
dealerTwo = random_card()
print(f"\nDealer hand one: {dealerOne}")

def handTotal(cardOne, cardTwo):
    """Returns the total value of the cards in the hand"""
    return cardOne + cardTwo

hand = handTotal(cardOne, cardTwo)
dealerHand = handTotal(dealerOne, dealerTwo)

if hand > 21:
    print("Dealer Wins!")

print(f"\nYou have {hand} points in your hand.")

choice = input(f"\nWish buy another card? (y/n): ")

while choice == 'y' or choice == 'Y':
    card = random_card()

    print(f"You got a {card}")

    hand += card

    print(f"\nYou have {hand} points in total")

    if hand > 21:
        print("Dealer Wins!")
        break

    choice = input(f"\nYou have {hand} points, wish buy another card? (y/n): ")

if choice == 'n' or choice == 'N':
    print(f"\nThe second dealer's card is {dealerTwo}")
    print(f"\nDealer have {dealerHand} points in total")

    if hand > 21:
        print("You Win!")

    if dealerHand >= hand:
        print("Dealer Wins!")
    elif dealerHand < hand:
        print("You Win!")
    else:
        print("Draw!")

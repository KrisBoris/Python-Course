# Blackjack game

import random

# 0 - spades, 1 - clubs, 2 - hearts, 3 - diamonds
suits = ["spades", "clubs", "hearts", "diamonds"]

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards = []

suit = "heart"  # color
rank = "K"
value = 10      # card's in-game value

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

random.shuffle(cards)
print(cards)
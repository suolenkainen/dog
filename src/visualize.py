"""This visualizes the card game in terminal and later to a text file"""

# variables
faces = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["hearts", "spades", "clubs", "diamonds"]
# unicode
"""In Unicode	U+2660 ♠ BLACK SPADE SUIT
U+2661 ♡ WHITE HEART SUIT
U+2662 ♢ WHITE DIAMOND SUIT
U+2663 ♣ BLACK CLUB SUIT
U+2664 ♤ WHITE SPADE SUIT
U+2665 ♥ BLACK HEART SUIT
U+2666 ♦ BLACK DIAMOND SUIT
U+2667 ♧ WHITE CLUB SUIT"""

for suit in suits:
    for card in faces:
        print(suit, card)
readme

1. Cards
    - Val
    - __eq__ method

2. Deck
    - List of cards
    - 52 cards
    - Shuffle
    - Draw a card

3. Player Class
    - Draws card from card
    - Holds hand

3. Game
    - Player Hands - Set? No, because we could have multiples, so Dict
    - Turn
        - while book_counter < 13
        - player requests random card in hand from random player
        - if player has 4 of those cards then player gets a book
        - else
            - If the player gets the card, the player's turn continues
            - Else the player draws a card and the turn changes
    - book_counter
        - Game ends when we all 13 books are made
    - Winner
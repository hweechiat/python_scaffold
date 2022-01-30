'''
Initialize a class coin_tossing_game 

Count of heads and tails is tracked using attributes:
1. num_heads
2. num_tails

A coin flip is defined as method coin_flip

Below is an example:
# game = coin_tossing_game()
# game.num_heads # 0
# game.num_tails # 0
# game.coin_flip() # Coin Flip resulted in tails
# game.coin_flip() # Coin Flip resulted in heads
# game.num_heads # 1
# game.num_tails # 1

'''
import random

class coin_tossing_game:
    def __init__(self):
        self.num_heads = 0
        self.num_tails = 0
    
    def coin_flip(self, print_result = True):
        result = random.choice(["heads", "tails"])

        # Print result by default, pass print_result = False to disable
        if print_result:
            print('Coin Flip resulted in {}'.format(result))
        
        if result == 'heads':
            self.num_heads += 1
        else:
            self.num_tails += 1
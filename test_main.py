from main import  coin_tossing_game

# 100 coin flips result in a total of 100 heads and tails
def test_case_1():
    game = coin_tossing_game()
    game.num_heads # 0
    game.num_tails # 0
    for _ in range(100):
        game.coin_flip(print_result = False) 

    assert game.num_heads + game.num_tails == 100

# 10000 coin flips result in a total of 100 heads and tails
def test_case_2():
    game = coin_tossing_game()
    game.num_heads # 0
    game.num_tails # 0
    for _ in range(10000):
        game.coin_flip(print_result = False) 

    assert game.num_heads + game.num_tails == 10000

# 100000 coin flips result in a 50/50 distribution   
def test_case_3():
    game = coin_tossing_game()
    game.num_heads # 0
    game.num_tails # 0
    for _ in range(100000):
        game.coin_flip(print_result = False) 
    
    # proportion of heads
    prop_heads = game.num_heads / 100000

    # proportion of tails
    prop_tails = game.num_tails / 100000
    
    assert round(prop_heads, 1) == 0.5  and round(prop_tails, 1) == 0.5 




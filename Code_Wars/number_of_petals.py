def how_much_i_love_you(nb_petals):
    petals = {
        0 : "not at all",
        1 : "love love",
        2 : "a little",
        3 : "a lot",
        4 : "passionately",
        5 : "madly",
        
    }
    
    return petals.get(nb_petals % 6)


user_input = int(input("Pick a number: "))
print(f"Your love level for John: {how_much_i_love_you(user_input)}" )
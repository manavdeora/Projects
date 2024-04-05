def GuessTheNumber(Num):
    no_of_chances = 10
    i = 1
    while i <= no_of_chances:
        usr_inp = int(input("enter number here: "))
        if usr_inp == Num:
            print(f"Correct Guess,You Win!\nYou Take {i} chances to complete game.")
            break
        elif no_of_chances == i:    
            print(f"Game Over,You Lose!")
            i+=1
        elif usr_inp > Num:
            print(f"Too High and you have only {no_of_chances-i} chances")
            i+=1
        elif usr_inp < Num:
            print(f"Too low and you have only {no_of_chances-i} chances")
            i+=1 

random_number = 57
GuessTheNumber(random_number)


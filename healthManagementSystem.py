# for getting date
def getdate():
    import datetime
    return datetime.datetime.now()

def log_data(usr_name,usr_food_exe):
    if usr_name == 1:
        if usr_food_exe == 1:
            usr_food_inp = input("Enter your food here: ")
            with open("F:\\Python Project\\HMS\\sunny_food.txt", "a") as f:
                f.write(f"[{getdate()}] {usr_food_inp}\n")
                print("Log add Successfully!")
                
        elif usr_food_exe == 2:
            usr_exe_inp = input("Enter your Exercise here: ")
            with open("F:\\Python Project\\HMS\\sunny_exe.txt", "a") as f:
                f.write(f"[{getdate()}] {usr_exe_inp}\n")
                print("Log add Successfully!")
                
    if usr_name == 2:
        if usr_food_exe == 1:
            usr_food_inp = input("Enter your food here: ")
            with open("F:\\Python Project\\HMS\\annes_food.txt", "a") as f:
                f.write(f"[{getdate()}] {usr_food_inp}\n")
                print("Log add Successfully!")
                
        elif usr_food_exe == 2:
            usr_exe_inp = input("Enter your Exercise here: ")
            with open("F:\\Python Project\\HMS\\annes_exe.txt", "a") as f:
                f.write(f"[{getdate()}] {usr_exe_inp}\n")
                print("Log add Successfully!")
                
    if usr_name == 3:
        if usr_food_exe == 1:
            usr_food_inp = input("Enter your food here: ")
            with open("F:\\Python Project\\HMS\\mansoor_food.txt", "a") as f:
                f.write(f"[{getdate()}] {usr_food_inp}\n")
                print("Log add Successfully!")
                
        elif usr_food_exe == 2:
            usr_exe_inp = input("Enter your Exercise here: ")
            with open("F:\\Python Project\\HMS\\mansoor_exe.txt", "a") as f:
                f.write(f"[{getdate()}] {usr_exe_inp}\n")
                print("Log add Successfully!")
                
def retrieve_data(usr_name,usr_food_exe):
    if usr_name == 1:
        if usr_food_exe == 1:
            with open("F:\\Python Project\\HMS\\sunny_food.txt") as f:
                data = f.read()
                print(data)
                
        elif usr_food_exe == 2:
            with open("F:\\Python Project\\HMS\\sunny_exe.txt") as f:
                data = f.read()
                print(data)
    
    elif usr_name == 2:
        if usr_food_exe == 1:
            with open("F:\\Python Project\\HMS\\annes_food.txt") as f:
                data = f.read()
                print(data)
                
        elif usr_food_exe == 2:
            with open("F:\\Python Project\\HMS\\annes_exe.txt") as f:
                data = f.read()
                print(data)
                
    elif usr_name == 3:
        if usr_food_exe == 1:
            with open("F:\\Python Project\\HMS\\mansoor_food.txt") as f:
                data = f.read()
                print(data)
                
        elif usr_food_exe == 2:
            with open("F:\\Python Project\\HMS\\mansoor_exe.txt") as f:
                data = f.read()
                print(data)

usr_lr = int(input("What You Want - Press (1) for Log Data and Press (2 ) for Retrieve Data: "))
usr_name = int(input("For Which Client - (1) for Sunny, (2) for Annes and (3) for Mansoor: "))
usr_food_exe = int(input(f"What You Want for client {usr_name} - (1) for Food and (2) for Exercise: "))

if usr_lr == 1:
    log_data(usr_name,usr_food_exe)
elif usr_lr == 2:
    retrieve_data(usr_name,usr_food_exe)
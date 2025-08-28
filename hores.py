from random import randint

length=0

def speed_limit():
    if Player_horse["speed"]>8 or Player_horse["speed"]<1:
        Player_horse["speed"]=5
        print("let me check real quick o is a five")
    elif Player_horse["stamina"]>8 or Player_horse["stamina"]<1:
        Player_horse["stamina"]=5
        print("Yea let me help you there o is a five nice")
    else:
        pass



def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")



Player_horse ={

    "name": "",
    "speed": 1,
    "stamina":1,
}


Player_horse["name"]=input("What is your juan name")
print("")
x=input_int("Fast MAx 8 ")





while True:
    
    Speed_x=Player_horse["speed"]
    length += Speed_x+randint(1,6)
    
    print(length)
         
    pass

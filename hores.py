from random import randint
import random 
length=0

def skills():
    skill=11
    min_value= 1
    max_value= 8


    print(f"Skill Points:{skill}")
    player_chose=input_int(f"What is your speed (Max {max_value} Min {min_value}) ")
    if player_chose<min_value or player_chose>max_value :
        while True:
            print(f"Skill Points:{skill}")
            player_chose=input_int(f" Please enter a valid number (Max {max_value} Min {min_value}) ")
            if player_chose<min_value or player_chose>max_value :
                player_horse["speed"]=player_chose            
                skill-=player_chose
                break
            else:
                print("not valid")
    else:
        skill-=player_chose
        player_horse["speed"]=player_chose


    if skill>8:
        max_value=8
    else:
        max_value=skill


    print(f"Skill Points:{skill}")
    player_chose=input_int(f"What is your stamina (Max {max_value} Min {min_value}) ")
    if player_chose<min_value or player_chose>max_value:
        while True:
            print(f"Skill Points:{skill}")
            player_chose=input_int(f" Please enter a valid number (Max {max_value} Min {min_value}) ")
            
            if player_chose<min_value or player_chose>max_value:
                player_horse["stamina"]=player_chose            
                skill-=player_chose
                break
            else:
                print("not valid")
    else:
        skill-=player_chose
        player_horse["stamina"]=player_chose


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def sky_net_horse():
    speed=randint(1,8)
    name_part= ["sky_net","sumsar","evil_gub","yllib","hsa","illit","bob_reverts"]
    evil_horse={

        "name": random.choice(name_part) + " " + random.choice(name_part),
        "speed": speed,
        "stamina":9-speed,
    }
    return evil_horse
    
    
evil_horse=sky_net_horse()

player_horse ={

    "name": "",
    "speed": 1,
    "stamina":1,
}


player_horse["name"]=input("What is your juan name")

skills()




print(player_horse)
print(evil_horse)

def game_turn():
    player_speed = player_horse["speed"] + random.randint(1,6)
    player_stamina =   random.randint(1,6) - player_horse["stamina"]
    if player_stamina >= 0:
        player_speed -= player_stamina

    evil_speed = evil_horse["speed"] + random.randint(1,6)
    evil_stamina =   random.randint(1,6) - evil_horse["stamina"]
    if evil_stamina >= 0:
        evil_speed -= evil_stamina

    print(f"")
    print(f"")
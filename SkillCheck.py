



Player ={

    "name": "",
    "speed": 1,
    "stamina":1,
}



def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")



def skills():
    skill=11
    min_value=1
    max_value=8


    print(f"Skill Points:{skill}")
    x=input_int(f"What is your speed (Max {max_value} Min {min_value}) ")
    if x<min_value or x>max_value :
        while True:
            print(f"Skill Points:{skill}")
            x=input_int(f" Please enter a valid number (Max {max_value} Min {min_value}) ")
            if x >=min_value or skill<= max_value:
                Player["speed"]=x            
                skill-=x
                break
            else:
                print("not valid")
    else:
        skill-=x
        Player["speed"]=x


    if skill>8:
        max_value=8
    else:
        max_value=skill


    print(f"Skill Points:{skill}")
    x=input_int(f"What is your stamina (Max {max_value} Min {min_value}) ")
    if x<min_value or x>max_value:
        while True:
            print(f"Skill Points:{skill}")
            x=input_int(f" Please enter a valid number (Max {max_value} Min {min_value}) ")
            if x >=min_value or skill<= max_value:
                Player["stamina"]=x            
                skill-=x
                break
            else:
                print("not valid")
    else:
        skill-=x
        Player["stamina"]=x






               
            
                
skills()


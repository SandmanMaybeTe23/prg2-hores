tech={
    "tech_one": False,
    "tech_two": False,
    "tech_tree":False,
}

z=True

while True:
    print("________________________________________________________________________________________________________")
    print(f"{tech}")

    picker=input("tech_one[T1] tech_two[T2] tech_tre[T3] ")


    if picker == "T1":
        switch=tech["tech_one"]
    elif picker == "T2":
        switch=tech["tech_two"]
    elif picker == "T3":
        switch=tech["tech_tree"]
    else:
        pass

    


    if tech[switch]==False:
        tech[switch]=True
        switch=""
    elif tech[switch]==True:
        tech[switch]=False
        switch=""
    else:
        pass



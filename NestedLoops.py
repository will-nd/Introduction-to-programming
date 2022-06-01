#Calculate cat age using selection, nested if and while loop

opt= "A" or "B"
while opt not in "X":    #While loop keeps program going till "X" is input
    
 print("Main Menu") #Main Menu
 print('---------')
 print("A: Kitten/Junior")
 print("B: Prime/Mature/Senior/Geriatric")
 print("X: Exit")
 print()
 opt=(input("Please select an option A,B OR X to exit: "))
 opt=opt.upper()
 if opt=="A": #if selection for main menu
    age_m=int(input("Enter age of cat in months: "))
    if 0<=age_m<=3: #Nested if for option a age of cat in months
        print("Cat is Kitten")
        print(f"Human equivalent= {age_m}years")
        print()
    elif(3<age_m<=7):
        print("Cat is Kitten")
        print(f"Human equivalent= {age_m+4}years")
        print()
    else:
        print("Cat is Junior")
        print(f"Human equivalent= {age_m+3}years")
        print()
 elif(opt=="B"):
    age_y=int(input("Enter age of cat in years: "))
    if 3<age_y<=6: #Nested if for option b age of cat in years
        print("Cat is Prime")
        print(f"Human Equivalent= {4*age_y+16}years")
        print()
    elif(6<age_y<=10):
        print("Cat is Mature")
        print(f"Human Equivalent= {4*age_y+16}years")
    elif(10<age_y<=14):
        print("Cat is Senior")
        print(f"Human Equivalent= {4*age_y+16}years")
        print()
    else:
        print("Cat is Mature")
        print(f"Human Equivalent= {4*age_y+16}years")
        print()
 else: #ends while loop
    print("Exiting Program")

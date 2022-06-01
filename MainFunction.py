#Late submission grade calculation using loops and modularisation (definining functions)

def late(): #Define latefunction
    print()
    raw_grade=int(input("Enter grade(0-100): ")) #User inputs raw grade integer
    while raw_grade not in range(101): #while loop for raw grade input outside of range
            print ("Invalid option")
            raw_grade=int(input("Enter grade (0-100): "))
    day_late=int(input("How many days late was the work submitted (0-7): "))
    while day_late not in range(8): #while loop for day late input outside of range
            print ("Invalid option")
            day_late=int(input("How many days late was the work submitted (0-7): "))
    new_grade=(raw_grade-(day_late*5)) #new grade calculation
    if raw_grade>40: #if statement for when penalty is necessary
        if new_grade>40: #nested if statement for when penalty is necessary
            print(f"Raw Grade: {raw_grade}")
            print(f"Number of days late: {day_late}")
            print()
            print("Days late    Mark to award")
            for i in range(day_late+1):#for loop up to inputted value of days late
                new_grade=(raw_grade-(i*5))
                print(i,"          ",new_grade)#prints deduction tab le from for loop
            print(f"Mark Awarded is: {new_grade}")
            print()
        else:
            print(f"Raw Grade: {raw_grade}")
            print(f"Number of days late: {day_late}")
            print()
            print("Days late    Mark to award")
            for i in range(day_late+1):
                new_grade=(raw_grade-(i*5))
                print(i,"          ",new_grade)
            print("This assignment will be capped at 40")
            print()
    else:
        print(f"Mark Awarded is: {raw_grade}")
    late_re=input("Enter another mark? Y/N: ")#user inputs wether or not they would like to enter another mark
    late_re=late_re.upper()#user input is equivalent to uppercase counter part
    while late_re not in ("Y", "N"):
            print ("Invalid option")
            late_re = input ("Enter Y or N: ")
            late_re = late_re.upper()
    if late_re=="Y":#if function to restart late() or enter main() functions
        late()
    else:
        main()

def on_time():#defining on_time() fucntion
    print("Stub: This option is under development")
    print()
    
def main():#defining main() function
     opt=""
     
     while opt!="X":#while loop for when User inputs value that is not X
         print()
         print("Main Menu")
         print('---------')
         print("A: On time")
         print("B: Late")
         print("X: Exit")
         print()
         opt=input("Enter option from menu: ")#User inputs option from main menu
         opt=opt.upper()

         while opt not in ("A", "B", "X"):#while loop for when user inputs invalid option
            print ("Invalid option")
            opt = input ("Enter A, B or X: ")
            opt = opt.upper()

         if opt=="A":#if option a is inputted run on_time() function
             on_time()
         elif (opt=="B"):#if option b is inputted run late() function
             late()
         else:#when x is inputted end program
             print("Exiting Program")

main()#start: run main() function

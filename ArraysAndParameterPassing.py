#creating plane operator dashboard using arrays and parameter passing

import array
import math
#-------------------------------------------------------------------------------
def create_flight():
    empty_list = [] 
    return (empty_list)
#-------------------------------------------------------------------------------

def full_flight(empty_list):
    empty_list = [
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]
        ]
    ff_list=empty_list
    print("Seating for full flight:")
    for row in range (len(ff_list)):
        for column in range(len(ff_list[row])):
            print (ff_list[row][column],end=" ")
        print()
    print()
    
    return(ff_list)

#-------------------------------------------------------------------------------
def part_flight(empty_list):
    import random
    row = 5
    col = 5
    empty_list = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]
    pf_list=empty_list
    
    print("PART FULL FLIGHT")
    print("----------------------------------------------------------------------------------")
    print()
    print("Seating for Part full flight:")
    for r in range(row):
      for c in range(col):
        pf_list[r][c] = random.randint(0,1)
        
    for row in range (len(pf_list)):
        for column in range(len(pf_list[row])):
            print (pf_list[row][column],end=" ")
        print()

    
    return(pf_list)

#-------------------------------------------------------------------------------
def ff_rev(band_a,band_b,cof1,cof5):
    print("FULL FLIGHT NO DRINKS")
    print("----------------------------------------------------------------------------------")
    rev_a=band_a*10
    rev_b=band_b*15
    rev_t=rev_a+rev_b
    print(f"Revenue from Band-A is: £{rev_a:.2f}")
    print(f"Revenue from Band-B is: £{rev_b:.2f}")
    print(f"Total revenue from flight is: £{rev_t:.2f}")
    print()
    print(f"cost of one flight: £{cof1}")
    if rev_t>cof1:
        print(f"You have Surpassed the break even point by: £{(rev_t-cof1):.2f} per flight")
    elif (rev_t==cof1):
        print("You are at the break even point")
    else:
        print(f"You have not reached the break even point are making a loss of: {(cof1-rev_t):.2f} per flight") 
    rev_t5=rev_t*5
    print(f"Total revenue from all 5 flights is: £{rev_t5:.2f}")
    print(f"cost of all 5 flights: £{cof5}")
    if rev_t5>cof5:
        print(f"You are making a {(((rev_t5-cof5)/cof5)*100):.0f}% profit")
    elif(rev_t5==cof5):
        print("Revenue is equal to cost. No profit or loss")
    else:
        print(f"You are making a loss of £{cof5-rev_t5}")
    print()
    
#-------------------------------------------------------------------------------
def ffd_rev1(band_a,band_b,drink,cof1d,cof5d):
    print("FULL FLIGHT WITH DRINKS")
    print("----------------------------------------------------------------------------------")
    rev_a=band_a*10
    rev_b=band_b*15
    rev_d=drink*25
    rev_t=rev_a+rev_b+rev_d
    print(f"Revenue from Band-A is: £{rev_a:.2f}")
    print(f"Revenue from Band-B is: £{rev_b:.2f}")
    print(f"Revenue from drinks is: £{rev_d:.2f}")
    print(f"Total revenue from flight is: £{rev_t:.2f}")
    print()
    print(f"cost of one flight: £{cof1d}")
    if rev_t>cof1d:
        print(f"You have Surpassed the break even point by: £{(rev_t-cof1d):.2f} per flight")
    elif (rev_t==cof1d):
        print("You are at the break even point")
    else:
        print(f"You have not reached the break even point are making a loss of: {(cof1d-rev_t):.2f} per flight") 
    rev_t5=rev_t*5
    print(f"Total revenue from all 5 flights is: £{rev_t5:.2f}")
    print(f"cost of all 5 flights: £{cof5d}")
    if rev_t5>cof5d:
        print(f"You are making a {(((rev_t5-cof5d)/cof5d)*100):.0f}% profit")
    elif(rev_t5==cof5d):
        print("Revenue is equal to cost. No profit or loss")
    else:
        print(f"You are making a loss of £{cof5d-rev_t5}")
    print()

#-------------------------------------------------------------------------------
def pf_rev(pf_list,band_a,band_b,cof1,cof5):
    sum_row = [sum(i) for i in pf_list]
    rev_a=band_a*(sum_row[0]+sum_row[1])
    rev_b=band_b*(sum_row[3]+sum_row[4]+sum_row[2])
    rev_t=rev_a+rev_b
    print(f"Revenue from Band-A is: £{rev_a:.2f}")
    print(f"Revenue from Band-B is: £{rev_b:.2f}")
    print(f"Total revenue from flight is: £{rev_t:.2f}")
    print()
    print(f"cost of one flight: £{cof1}")
    if rev_t>cof1:
        print(f"You have Surpassed the break even point by: £{(rev_t-cof1):.2f} per flight")
    elif (rev_t==cof1):
        print("You are at the break even point")
    else:
        print(f"You have not reached the break even point are making a loss of: {(cof1-rev_t):.2f} per flight") 
    rev_t5=rev_t*5
    print(f"Total revenue from all 5 flights is: £{rev_t5:.2f}")
    print(f"cost of all 5 flights: £{cof5}")
    if rev_t5>cof5:
        print(f"You are making a {(((rev_t5-cof5)/cof5)*100):.0f}% profit")
    elif(rev_t5==cof5):
        print("Revenue is equal to cost. No profit or loss")
    else:
        print(f"You are making a loss of £{cof5-rev_t5}")
    print()
    
#-------------------------------------------------------------------------------
def main():
    band_a = (float(input("Enter Band-A seat price: ")))
    band_b = (float(input("Enter Band-B seat price: ")))
    drink = (float(input("Enter Price of drink: ")))
    
    cof1=5000
    cof1d=5000+(drink*25)/2
    cof5=25000
    cof5d=25000+((drink*25)/2)*5
    print()
    empty_list=create_flight()
    ff_list=full_flight(empty_list)
    ff_rev(band_a,band_b,cof1,cof5)
    ffd_rev1(band_a,band_b,drink,cof1d,cof5d)
    pf_list=part_flight(empty_list)
    pf_rev(pf_list,band_a,band_b,cof1,cof5)
main()

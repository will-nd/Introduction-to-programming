#Use sequences to give succesful calculations

#Input
print("All measurements done in metres.")
print()
length=int(input("Enter Length: ")) #Allows user to input dimensions
breadth=int(input("Enter Breadth: "))
height=int(input("Enter Height: "))
print("Length:",length,"m Breadth:",breadth,"m Height:",height,"m") #Displays chosen dimensions
print()

#Process
sa=float(2*breadth*height+2*length*height+length*breadth) #calculation for Surface Area
print(f"Surface Area: {sa:.2f}")
woi=1.06#weight of iron psm
mass=float(sa*woi)#Calculation for mass of barge
print(f"Mass: {mass:.2f}kg")
draft=float(mass/(length*breadth))#Calculation for breadth using BODMAS
print(f"Draft: {draft:.2f}m")
hob=float(height-draft)#hob=height of barge out p\of water
print(f"The height of the barge that is above the water line: {hob:.2f}m")


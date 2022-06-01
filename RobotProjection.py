#Robot journey on flat plane with selection function and math module

#Input
import math #imports math module
ang=int(input("Please enter an angle between 0 and 90 (inclusive): "))#selection function to ensure correct input
if ang>90:
    ang=int(input("Angle is too large, enter new angle: "))
elif(ang<0):
    ang=int(input("Angle",ang,"° is too small, enter new angle: "))
else:
    print("Angle:",ang,"°")
tot=int(input("Please enter positive time of travel in seconds: "))
if tot<0:
    tot=int(input("Time of travel not positive, enter new time of travel: "))
else:
    print("Time of travel: ",tot,"s")

#Process
spd=1.5
dis=spd*tot #calculates distance
print(f"Distance travelled: {dis:.2f}m")
h_dis=dis*(math.sin(ang*(math.pi/180))) #use of math module to calc horizontal distance
print(f"Horizontal distance: {h_dis:.2f}m")
v_dis=dis*(math.cos(ang*(math.pi/180))) #use of math module to calc vertical distance
print(f"Vertical distance: {v_dis:.2f}m")
b_usg=int(tot*2.7)#Calculates battery used in journey
b_rem=int(100-b_usg)
if b_usg<=50:#selection to inform user on end battery state of robot
    print(f"Estimated battery usage: {b_usg}%")
    print(f"{b_rem}% remains for return trip")
elif(50<b_usg<100):
    print(f"Estimated battery usage: {b_usg}%")
    print("Insufficient battery for return trip")
else:
    print("Robot cannot travel the distance required as the battery will expire before it gets there.")

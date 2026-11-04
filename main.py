Alex=input("ditt namn: ")
print(f"Hej {Alex} och välkommen till spelet")
alex3=3 
import random
alex1=random.randint(1, 10)
while alex3>0:
    alex2=int(input("gissa tal mellan 1 och 10"))
    if alex2==alex1:
        print("Lucky you")
    else:
        print("You're trash") 
        alex3=alex3-1
        



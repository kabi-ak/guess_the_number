def guess(user,comp):
    if (user==comp):
        print("your guess is correct")
    elif (user<comp):
        print("your guess is too small")
    elif (user>comp):
        print("your guess is too high")
import random
l=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
user=str(input("enter your choice between 1 - 20:"))
comp=random.choice(l)
print(comp)
guess(user,comp)
# Rock paper scissors project no. 01
import random

user = input(print("Enter the name of user :"))
print("Type 0 for Rock.\nType 1 for Paper.\nType 2 for Scissors.")
uc = int(input(print("Enter the choice : ")))

cc = random.randint(0,2)
print(f"Computer choose {cc}")
print(f"{user} choose {uc}")


if uc < 2 :
    if cc == uc :
        print("It is a draw.")
    elif cc > uc or cc== 0 & uc==2 :
        print(f"{user} loose")
    elif cc < uc or cc==2 & uc==0 :
        print(f"{user} won")
else :
    print("invalid choice.")
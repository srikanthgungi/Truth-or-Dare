import random
def truthOrdareGame(number):
    if number==0:
        return "its dad"
    elif number==1:
        return "its mom"
    elif number==2:
        return "its anna"
    elif number==3:
        return "its srikanth"
    elif number==4:
        return "its Harshika"
    elif number==5:
        return "its vadhina"
    elif number==6:
        return "its Harshika"
    elif number==7:
        return "its Midhun"
r=random.randint(0,7)
turn=truthOrdareGame(r)
print(turn)
#print(truthOrdareGame(random.randint(0,7)))

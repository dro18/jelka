import random

def daj_okrasek():
    okraski = ["%", "@", "?", "&"]
    if random.randint(0,6)==5:
        return random.choice(okraski)
    else:
        return "+"



def smrekca(velikost):


    x = velikost
    for s in range(2, x,):
        print " "*((x-s)/2) + s*daj_okrasek() + " "*(x-s)
    print "VESELE BOZICNE PRAZNIKE IN SRECNO NOVO LETO!"




y = raw_input("vpisi velikost smrekce: ")
smrekca(int(y))

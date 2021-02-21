import random
print('Press ENTER to generate a random value from 1-6:')
inp=input()
def rando(a,b):
    print(random.randint(a,b))
if inp=='':
    rando(1,6)


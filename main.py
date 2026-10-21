import math
import random as rand

param=8
canidates_num=10000
generations=50

def fitness(p):
    error=0
    for x in range(-314,314):
        x0=x/100
        y=0
        for i in range(len(p)):
            y+= p[i] * x0**i
        error+=abs(math.sin(x0)-y)
    return error

def key(e):
    return e.fitness

class Canidate:
    def __init__(self,p1=None,p2=None):
        global param

        self.params = []
        if p1 is None or p2 is None:
            for i in range(param):
                self.params.append(rand.uniform(-1.0,1.0))
        else:
            for i in range(param):
                #choose traits from parents
                j=rand.randint(1,2)
                if j == 1:
                    self.params.append(p1.params[i])
                else:
                    self.params.append(p2.params[i])
                #mutation
                if rand.randint(1,10)==1:
                    self.params[i]=rand.uniform(-1.0,1.0)
        self.fitness=fitness(self.params)
    def update(self):
        self.fitness=fitness(self.params)

generation=0

canidates=[]
fitness_list=[]

p=[None]
parents=100


for i in range(generations):
    for j in range(canidates_num-parents):
        p1=p[rand.randint(0,len(p)-1)]
        p2=p[rand.randint(0,len(p)-1)]
        canidates.append(Canidate(p1=p1,p2=p2))
    for j in canidates:
        j.update()
    canidates.sort(reverse=False,key=key)
    p=[]
    for j in range(parents):
        p.append(canidates[j])
    print(p[0].fitness)
    print(p[0].params)
    canidates=[]
    for j in p:
        canidates.append(j)

print()
print() 
for i in p:
    print(i.params)

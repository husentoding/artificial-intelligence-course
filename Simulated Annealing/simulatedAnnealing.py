import random
import math


def main():
    x=random.uniform(-10, 10)
    y=random.uniform(-10, 10)
    fx= fungsi(x,y)
    cooling_rate= 0.6
    initial_state= fx
    current_state= initial_state
    best_so_far= current_state
    k=0
    T=1000000
    while (T>0):
        xnew = random.uniform(-10, 10)
        ynew = random.uniform(-10, 10)

        new_state= fungsi(xnew,ynew)
        #evaluasi new state
        deltaE= new_state-current_state
        if(deltaE<0):
            current_state= new_state
            best_so_far= new_state
        elif (deltaE >=0):
            prob= setProbability(deltaE, T)
            rand= random.uniform(0,1)
            if(rand<=prob):
                current_state = new_state
        if (k%3==0):
            T=annealingSchedule(T, cooling_rate)
        k+=1
    print('Best so Far: ',best_so_far)

def annealingSchedule(T, cooling_rate):
    return T-(T*cooling_rate)


def fungsi(x,y):
    p1= (4-2.1*pow(x,2)+(pow(x,4)/3))*pow(x,2)
    p2= x*y
    p3=(-4+4*pow(y,2))*pow(y,2)
    return p1+p2+p3

# f(x,y) = (4-2,1x^2 + x^4/3) x^2 + xy + (-4+4y^2)y^2

def evaluasiState(fnewstate, fcurrentstate):
    return fnewstate-fcurrentstate

def setProbability(delta, T):
    a = math.exp(-delta/T)
    return a




if __name__== '__main__':
    main();


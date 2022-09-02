#Priyal Shah Problem 4
import math

def is_prime(num):
    #num = int(input("> "))
    if(num<2): 
        return False
    for i in range(2, num):
        if(num%i == 0):
            return False
    else:
        return True

if __name__ == "__main__" :
    while True:
        num = int(input("> "))
        is_prime(num)
  

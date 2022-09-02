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
        if(is_prime(num)==True):
            print(is_prime(num))
        else:
            print(is_prime(num))
  

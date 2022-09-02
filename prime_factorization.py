#Priyal Shah Problem 5
import math

def prime_factorization(n):
    answer = []
    while n%2==0:
        answer.append(int(2))
        n = n/2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n% i == 0:
            answer.append(int(i))
            n = n/i
    if(n>2):
        answer.append(int(n))
    return answer


if __name__ == "__main__" :
    while True:
        n = int(input("> "))
        print(prime_factorization(n))
        
    

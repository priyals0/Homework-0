#Priyal Shah Problem 4

def is_prime(num):
    #num = int(input("> "))
    if(num<2): 
        return False
    elif(num%2==0 and num!= 2):
        return False
    elif(num%3==0 and num!= 3):
        return False
    elif(num%5==0 and num!= 5):
        return False
    elif(num%7==0 and num!= 7):
        return False
    elif(num%11==0 and num!= 11):
        return False
    elif(num%13==0 and num!= 13):
        return False
    elif(num%17==0 and num!= 17):
        return False
    elif(num%23==0 and num!= 23):
        return False
    else:
        return True

def main():
    while True:
        num = int(input("> "))
        is_prime(num)    

while True:
    if __name__ == "__main__" :
        main()

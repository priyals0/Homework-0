#Priyal Shah Problem 4

def is_prime(num):
    #num = int(input("> "))
    if(num%2==0 and num!= 2):
        print("False")
    elif(num%3==0 and num!= 3):
        print("False")
    elif(num%5==0 and num!= 5):
        print("False")
    elif(num%7==0 and num!= 7):
        print("False")
    elif(num%11==0 and num!= 11):
        print("False")
    elif(num%13==0 and num!= 13):
        print("False")
    elif(num%17==0 and num!= 17):
        print("False")
    elif(num%23==0 and num!= 23):
        print("False")
    else:
        print("True")

num = int(input("> "))
is_prime(num)

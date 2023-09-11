import random

num =random.randrange(1000,10000)

n=int(input("guess 4 digit number"))

if n==num:
    print("great ,you guessed it right in just 1 try")

else:
    ctr = 0

    while (n!=num):
        ctr+=1
        count=0

        n=str(n)

        num=str(num)

        for i in range(0,4):

            if(n[i]==num[i]):

                count+=1
                correct[i] =n[i]

            else:
                continue
        print("not quite the number ",count,"digits correct")

        print('\n')
        print('\n')
        n=int(input("enter your choice of number"))
        
        elif(count==0):
            print("none matched")
            n=int(input("enter you next choice of nubers"))
    
    if n == num:
            ctr+=1
              print("you are mastermind")
            print("you took only",ctr ,"tries")
            
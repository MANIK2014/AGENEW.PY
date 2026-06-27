try:
    yourage = int(input("Enter your age:"))
    if(yourage<18):
        raise ValueError
    else:
        print("Your age is valid to be considered an adult.")
        
except ValueError:
    print("Your age is not valid to be considered an adult.")

if yourage % 2==0:
    print("Your age is even")
else:
    print("It's odd")    

#THIS CODE WILL GIVE YOU TO OUTPUTS ONE,IF YOUR AGE IS VALID TO BE CONSIDERED ADULT AND SECOND,IF YOUR AGE IS ODD OR EVEN.     




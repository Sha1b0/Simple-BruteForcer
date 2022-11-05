from random import *
guess_pass=input("Enter your pass:")
password=["a","b","c","d","e","f","g","h","i","j","k","l","m","a","n","o","p","q","r","s","t","u","v","x","y","z","0"]
guess=""
while(guess != guess_pass):
    guess=""
    for letter in range(len(guess_pass)):
            guess1=password[randint(0,25)]
            guess=guess1+ str(guess)
    print(guess)
print("pass is :",guess)



# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
# # You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions
import sys

def prim(Value):
    for x in range(1,Value):

        if Value % 2 == 0:
            sys.exit("The number is not prime number")
        elif x % 2 == 1:
            continue

    print("Number is prime Number")

prim(148)


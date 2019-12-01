# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

def odd_even(b):

    c = b % 2
    if c == 1:
        print(" It is ODD")
    else:
        print("It is even")


a = int(input(" Enter the Value to see"))
odd_even(a)


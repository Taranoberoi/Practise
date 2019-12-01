# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

val = int(input("Enter the Random Value"))
n = random.randint(1,10)

print(f"Random number is {n}")
if val == n:
    print(" Exact Match")
elif val < n:
    print("Guess Number is less then actual")
else:
    print("Guess Number is greater then actual")




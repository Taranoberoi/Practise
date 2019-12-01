# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers \

def fib(n):
    a = []
    if n == 1:
        a.append(n)
    elif n == 2:
        a = [1,1]
    elif n > 2:
        a = [1,1]
        for i in range(1, n):
            a.append(a[i] + a[i-1])
    print(a)

fib(9)

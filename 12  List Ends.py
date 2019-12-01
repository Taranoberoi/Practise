# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def list_func(a):
    b = []
    b.append(a[0])
    b.append(a[-1])
    return b


a = [5, 10, 15, 20, 25]
c = []
c= list_func(a)
print(c)

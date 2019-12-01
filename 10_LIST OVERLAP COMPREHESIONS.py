# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

# Take two lists, say for example these two:and write a program that returns a list that contains only the elements that are
# common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Write this in one line of Python using at least one list comprehension.
import random

a = []
b = []
c = []

for i in range(10):
    a.append(random.randrange(1,15))
    b.append(random.randrange(1,15))
for i in b:
    if i in a and i not in c:
        c.append(i)

print(a)
print(b)
print(c)



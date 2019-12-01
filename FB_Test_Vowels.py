n = " I am soumya"
v = 0
for i in n.lower():
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        v = v + 1
        print("show me vowels",i)
print(v)
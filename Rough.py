A = input("Enter the Name of the person: ").strip()
B = input("Enter the age:").strip()
print(f"Value fo A is {A} and Value of B{B}")

# First, create a variable called start, and set it equal to "I am ".
start = " I am "
# Next, create a variable called age and set it equal to your age in years.
age = 37
# Next, create a variable called end, and set it equal to " years old".
end = " years old"

# Next, create a variable called output and use {} symbols and the format() function to stick the start, age and end variables
string = "Value of the {} and age value is {} and end Variable value is {}"
output = string.format(start,age,end)
print(output)
# together to make a string.

# An example output string would be "I am 15 years old"
# print(output)

# Finally, print the output to the screen using the print() function.



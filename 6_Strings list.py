# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

str = input(" Enter the String to eb checked for palindrome value")
str1= str[::-1]

if str == str1:
    print("It is palindrome string")
else:
    print("It is NOT a palindrome string")



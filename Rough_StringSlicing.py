# a = "Super"
# b = "Supercaliforniaismycalculasblablabla"
# # print(a[1:5:1])
# # print(a[0:5:3])
# # print(a[::-1])
# print(a[-2])
# print(b[b.index("cali"):b.index("calculas")])

email = input("Please enter the email address : ").strip()
# a = email.index("@")
a = email[:email.index("@")]
b = email[email.index("@")+1:email.index(".")]

output = "Your username is {} and domain name {}".format(a,b)
print(output)

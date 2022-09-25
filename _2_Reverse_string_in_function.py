def reverse(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1

print("Enter the string you want to reverse: ")
str = input()

print("The reversed string is: ")
print(reverse(str))
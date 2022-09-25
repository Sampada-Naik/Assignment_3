def reverse1(str):
    reversed_str = str[::-1]
    return reversed_str

print("Enter the string you want to reverse:")
str = input()

print("The reversed string is: ")
print(reverse1(str))
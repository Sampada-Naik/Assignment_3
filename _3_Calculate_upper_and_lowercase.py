def countCase(str):
    uppercase_count = 0
    lowercase_count = 0

    for i in str:
        if i.isupper():
            uppercase_count += 1
        if i.islower():
            lowercase_count += 1

    print("Number of uppercase in the string: ",uppercase_count)
    print("Number of lowercase in the string: ",lowercase_count)

print("Enter the string:")
str = input()
countCase(str)



def caseCount(str):
    uppercase_count = 0
    lowercase_count = 0
    for i in str:
        if(i>='a' and i<='z'):
            uppercase_count += 1
        if(i>="A" and i<="Z"):
            lowercase_count += 1
    print("Number of uppercase in the string: ",uppercase_count)
    print("Number of lowercase in the string: ",lowercase_count)

print("Enter the string:")
str = input()
caseCount(str)
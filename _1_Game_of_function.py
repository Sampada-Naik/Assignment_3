def sum_list(lst):
    sum = 0
    for i in range(0,len(lst)):
        if(number_elements == 0):
            return 0
        else:
            sum = sum + lst[i]
    
    return sum        
        
number_elements = int(input("Enter the number of elements: "))
lst = []

for i in range(0,number_elements):
    numbers=int(input())

    lst.append(numbers)

print(lst)
final_sum = sum_list(lst)
print(final_sum)

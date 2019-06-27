#Absolute Prime Number

#import permutations package 
from itertools import permutations

# It rearrange the input data to permform permutation
def rearrange_input(input_data):
    list = []
    while(input_data!=0):
        r = input_data % 10
        list.append(r)
        input_data = int(input_data/10)
    return list

# Permute method returns the list of all the possible permutation of the given number
def permute(list):
    perm = permutations(list)
    list_permutation = []
    for i in perm:
        data = ''.join(map(str,i))
        list_permutation.append(int(data))
    return list_permutation

# The next method checks whether the number is an Absolute Prime number or not
def absolute_prime_data(list_permutation):
    flag = 0
    for num in list_permutation:
        for i in range(2,num//2):
            if num%i==0:
                flag=flag+0
                break
            else:
                flag=flag+1
                break
    if flag==len(list_permutation):
        print("\n")
        print("| ABSOLUTE PRIME NUMBER |\n")
    else:
        print("\n")
        print("| NOT AN ABSOLUTE PRIME NUMBER |\n")

# Get Input from user to check whether a given number is an Absolute Prime Number or not
input_data = int(input("\nEnter the data:"))
# Call the Rearrange the input on input data
list_data = rearrange_input(input_data)
# Call the Permute method 
perm_data = permute(list_data)
print("\nList of all the possible permutations of the Input Number are:")
print(perm_data)
# Call the Absolute Prime Data method
absolute_data = absolute_prime_data(perm_data)
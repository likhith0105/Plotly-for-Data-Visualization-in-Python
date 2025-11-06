#write a python program to check maximum and minimum in a given
#list without using max and min function

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
maxi = mini = numbers[0]

for num in numbers:
    if num > maxi:
        maxi= num
    if num < mini:
        mini = num


print("Maximum element:", maxi)
print("Minimum element:", mini)

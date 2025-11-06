#write a python program that check number of occurance of a given digit in number

number = input("Enter a number: ")
digit = input("Enter a digit to count: ")

count = 0

for d in number:
    if d == digit:
        count += 1

print(f"The digit {digit} occurs {count} times in {number}.")

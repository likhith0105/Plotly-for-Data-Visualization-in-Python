#write a python program to print all the number divisible by 3 and 5 upto 100

print("NUMBERS DIVISIBLE BY 3 AND 5 ARE:")
for i in range (2,101):
    if i%3==0 and i%5==0:
        print(i)
# write a python program to print primr numbers from 1-100

print("Prime numbers from 1 to 100 are:")

for num in range(2, 101): 
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


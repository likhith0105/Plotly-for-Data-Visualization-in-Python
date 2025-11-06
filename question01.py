#  write a python program to read a sentence and list the palindrome 
#  words in it

s=input("enter the sentence:")
w=s.split()
p=[]
for i in w:
    if i==i[::-1]:
     p.append(i)
print("Palindrome words:",p)
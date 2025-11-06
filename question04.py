#write a python program to find the entered number is palindrome or not 
n=input("Enter the number:")
if n==n[::-1]:
   print(n," is a palindrome number. ")
else:
   print(n," Is not a palindrome number. ") 
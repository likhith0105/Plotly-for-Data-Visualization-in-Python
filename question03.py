 #find the nth largest elemnet in the list when n is entered by user 


nums = [10, 25, 7, 50, 32, 18, 90, 60]
print("List:", nums)
n = int(input("Enter the value of n: "))
nums.sort(reverse=True)
if n <= len(nums):
    print(f"The {n}th largest element is:", nums[n - 1])
else:
    print("Invalid input! n is larger than the list size.")

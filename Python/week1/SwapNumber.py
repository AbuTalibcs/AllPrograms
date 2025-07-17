a = int(input("Enter the first number: "))
b = int(input("Enter the secound Number: "))
temp =0

print("The First number Before Swap is ", a)
print("The Secound number Before Swap is ", b)

temp = a
a = b
b = temp

print("The First number After Swap is ", a)
print("The Secound number After Swap is ", b)

# METHOD 2
num1 = 5
num2 = 8

num1 , num2 = num2 , num1

#print("After Sawap Number 1 is ", num1 " and Number 2 is " , num2)
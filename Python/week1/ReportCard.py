# Input parts.
print("             Student Report Card                     ")
print("------------------------------------------------------------------")
name=input("Enter your name : ")
roll=int(input("Enter your roll number : "))
print("Enter your subjects marks : ")
marks_1=float(input("English : Enter marks : "))
marks_2=float(input("Science : Enter marks : "))
marks_3=float(input("SST : Enter marks : "))
# logic parts.
Subjects={'English': marks_1,'Science':marks_2, 'SST':marks_3}
students={name: {roll:Subjects}}
calculate=marks_1+marks_2+marks_3
averge=calculate/3
# Output parts.
print("------------------------------------------------------------------")
if averge >=40:
	print(name)
	print("Your roll number", roll)
	print("Subject :")
	print("English :",Subjects['English'])
	print("Science :",Subjects['Science'])
	print("SST :",Subjects['SST'])
	print("Total marks : ",calculate)
	print("Averge marks :",averge)
	print("You are PASS ; - )")
	print("– ","Success is not the end, it's just the beginning of new possibilities.")
	print("-----------------------------------------------------------------")
	if averge >=90:
		print("The Topper Student")
		print(name)
	else:
		print("The Topper Student")
		print("none")
		print("-------------------------------------------------------------------")
else:
	print(name)
	print("Your roll number", roll)
	print("Subject :")
	print("English :",marks_1)
	print("Science :",marks_2)
	print("SST :",marks_3)
	print("Total marks : ",calculate)
	print("Averge marks :",averge)
	print("You are Fail :( ")
	print("– ","Failure is not the opposite of success, it's a part of success.")
print("-----------------------------------------------------------------")
print("               Thankyou very much...             ")
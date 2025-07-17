marks = int(input("Enter marks: "))
if marks >= 60 :
    if marks >= 90:
        print("Grade A+")
    elif marks < 90 and marks > 80:
        print("Grade A")
    elif marks >= 70 and marks <= 80:
        print("Grade B")
    else : 
        print("Grade C")
else :
    print("You are failed!")


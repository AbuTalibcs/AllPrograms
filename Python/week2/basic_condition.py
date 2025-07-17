# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if new_word[-3] == 'ing' :
    new_word = new_word[:-3]
    print(new_word)
# add the suffix "ing" to `new_word` if `continuous_tense` is True
if continuous_tense == 1 :
     new_word = new_word + 'ing'
     print(new_word)
# write the whole if else block here

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age < 18 :
    print("Child")

else:
    print("Adult")

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block
if age < 18 :
    print("child Non-member")
else : 
    print("Adult Member")
    
# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if color_code == "R":
    print('red')
elif color_code == 'B':
    print('Blue')
elif color_code == 'G':
    print("green")
else:
    print("Black")

is_time_valid = ... # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = ...

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here


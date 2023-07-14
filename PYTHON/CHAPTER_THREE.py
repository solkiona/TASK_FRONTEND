#CHAPTER THREE(3)
#EXERCISES


# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

Hours = input("Enter Hours: ")

Rate = input("Enter Rate: ")

OvertimePay = ((Hours - 40) * 10) * 1.5

Pay = (40 * Rate ) + OvertimePay
print (Pay)


# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input


try:
    Hours = input("Enter Hours: ")
    Rate = input("Enter Rate: ")
    OvertimePay = ((Hours - 40) * 10) * 1.5
    Pay = (40 * Rate ) + OvertimePay
    print (Pay)
except:
    print("Please enter numeric input")

# Exercise 3: Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# 3.11. EXERCISES 41
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

score = input("Enter score: ")

if score >= 0 and score <= 1:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
else:
        print("Bad score")

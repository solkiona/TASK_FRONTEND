#CHAPTER FIVE(5)
#EXERCISES

# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.


accumulator = 0
count = 0
average = 0

while True:

    Number = input("Enter a value: ")

    if Number == "done":
        print(accumulator, count, average)
        break
    try:
        accumulator = accumulator + int(Number)
        count = count + 1
        average = accumulator / count

    except:
        print("Invalid Input")

    


# 5.9. EXERCISES 65
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333


# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

min = None
max = None
NumList = []
count = 0

while True:

    Number = input("Enter a value: ")

    if Number == "done":
        break
    try:

        NumList.append(int(Number))
        count = count + 1

    except:
        print("Invalid Input")

for item in NumList:
    if max == None and min == None:
        max = item
        min = item
    elif item > max:
            max = item
    elif item < min:
            min = item

print("Maximum number is : {}".format(max) , "Minimum number is : {}".format(min))
    

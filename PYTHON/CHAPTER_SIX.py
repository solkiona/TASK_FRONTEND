#CHAPTER SIX (6)
# EXERCISES 

# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

fruit = "Bannana"
index = len(fruit)-1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1

# Exercise 2: Given that fruit is a string, what does fruit[:] mean?

fruit = "String"

print(fruit[:])
OUTPUT:
String 

# fruit[:] means from the beginning of the string to the end of the string 



# Exercise 3: Encapsulate this code in a function named count, and gen-
# eralize it so that it accepts the string and the letter as arguments

def count(word, letter):
    count = 0
    
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

# Exercise 5: Take the following Python code that stores a string:

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number

str = 'X-DSPAM-Confidence:0.8475'

index = str.find(":")
num = str[index+1:]
num = float(num)

print(type(num))

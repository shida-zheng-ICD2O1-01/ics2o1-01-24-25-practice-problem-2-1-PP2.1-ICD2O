'''
    Lesson: If statments
    Author: Mr. Kalisz
    Date Created: Oct 9, 2024
    Date Last Modified: Oct 9, 2024
'''

#if statement

num = int(input("Input an integer: "))

#if <condition>:
if num < 6:
    #Indenting means this code is inside the if statement
    #Code inside the if statement only runs when the condition is true
    num = num + 7
    print("num is less than 6")


if num > 6:
    print("num is greater than 6")

print("This always runs")
print(num)
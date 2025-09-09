# task 1
num1 = float((input("write the first number:")))
num2 = float((input("write the second number:")))
print("select an operator from the following (+,-,*,/)")
operator = (input("enter an operator"))
if operator == '*':
    print(num1 * num2)
elif operator == '+':
    print(num1 + num2)
elif operator == '/':
    if num2 == 0:
        print("invalid")
    else:
        print(num1/num2)
    
else:
   print( num1 - num2)

# task 2
numbers= int(input("Student marks are:"))
if numbers >= 85:
    print('the grade of the student is A')
elif numbers >=70:
    print('the grade of the student is B')
elif numbers >= 50:
    print('the grade of the student is C')
else :
    print('the grade of the student is F')


# task 3
year = int(input('Please type in a year: '))

if year % 400 == 0:
    print('That year is a leap year.')
elif year % 100 == 0:
    print('That year is not a leap year.')
elif year % 4 == 0:
    print('That year is a leap year.')
else:
    print('That year is not a leap year.')
    

    






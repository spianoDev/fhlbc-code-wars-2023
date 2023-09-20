# Exercise 42

'''
Write a function that returns the product of two parameters
'''


def multi(num1, num2):
    print(num1 * num2)
    return num1 * num2


multi(2, 2)
multi(2, -2)

# Exercise 43

'''
Write a function that converts a number into the day of the week
'''


def return_day(num):
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if num < 1 or num > 7:
        return None
    else:
        return days_of_week[num - 1]


print(return_day(-99))

# Exercise 44

'''
Write a function that returns the last element in a list. If the list is empty, return None
'''


def last_element(lst):
    return lst[-1] if len(lst) > 0 else None


print(last_element([1, 2, 3]))
print(last_element([]))
print(last_element(['Sarah', 'Adam', 'Penny', 'Sophia']))

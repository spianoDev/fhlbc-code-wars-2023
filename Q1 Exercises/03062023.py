# Unfinished Loop - Bug Fixing #1
# Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

## Original Code Provided ##

# def create_array(n):
#     res=[]
#     i=1
#     while i<=n: res+=[i]
#     return res

## Corrected Loop ##

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
        print(res)
    return res


create_array(2)

# Thinkful - List and Loop Drills: Grade calculator
# You're a statistics professor and the deadline for submitting your students' grades is tonight at midnight.
# Each student's grade is determined by their mean score across all of the tests they took this semester.
#
# You've decided to automate grade calculation by writing a function calculate_grade() that takes a list  of test
# scores as an argument and returns a one character string representing the student's grade calculated as follows:
#
# 90% <= mean score <= 100%: "A",
# 80% <= mean score < 90%: "B",
# 70% <= mean score < 80%: "C",
# 60% <= mean score < 70%: "D",
# mean score < 60%: "F"
# For example, calculate_grade([92, 94, 99]) would return "A" since the mean score is 95,
# and calculate_grade([50, 60, 70, 80, 90]) would return "C" since the mean score is 70.
#
# Your function should handle an input list of any length greater than zero.

def calculate_grade(scores):
    total_score = 0
    for score in scores:
        total_score += score
    print(total_score)
    mean_score = total_score/len(scores)
    print(mean_score)
    if mean_score >= 90:
        print('Nice work, you get an A!')
        return 'A'
    elif mean_score >= 80:
        print('Good effort, you get a B.')
        return 'B'
    elif mean_score >= 70:
        print('Keep trying, you get a C.')
        return 'C'
    elif mean_score >= 60:
        print('Let\'s work on this together to help you improve. You get a D')
        return 'D'
    else:
        print('Yikes! You have failed with an F')
        return 'F'

calculate_grade([92, 94, 99]) # => "A"
calculate_grade([50, 60, 70, 80, 90]) # => "C"
calculate_grade([50, 55]) # => "F"

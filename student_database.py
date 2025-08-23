# In this series of exercises you will create a 
# simple student database. Before diving in, 
# please spend a moment reading through the 
# instructions and thinking about what sort of data 
# structures are necessary for organising the data 
# stored by your program.


# Part 1: Adding Students
# First write a function named add_student, which 
# adds a new student to the database. Also write a 
# preliminary version of the function print_student, 
# which prints out the information of a single student.

# These function are used as follows:

def add_student(students:dict,name:str):
    students[name] = []

def print_student(students:dict,name:str):
    average = 0

    if name in students and len(students[name]) == 0:
        print(f"{name}:")
        print(' no completed courses')
    elif name in students:
        print(f"{name}:")
        print(f' {len(students[name])} completed courses:')
        for i in students[name]:
            print(f'  {i[0]} {i[1]}')

            average += i[1]

        average = (average / len(students[name]))
        
        print(f' average grade {average}')
    elif name not in students:
        print(f'{name}: no such person in the database')


def add_course(students:dict,name:str,course:tuple):

    found = False
    index_of_course = None
    course_name = course[0]


    for i in students[name]:
        if course_name in i:
            found = True
            try:
                index_of_course = i.index(course_name)
            except:
                continue

            if found == True:
                break


    if found == False:
        if course[1] != 0:
            students[name].append(course)

    if found == True:

        if index_of_course >= 0:
            if students[name][index_of_course][1] < course[1]:
                students[name][index_of_course] = course

def summary(students:dict):
    num_students = 0

    most_courses = [None,0]

    best_avg = [None,0]


    for i in students:
        grade_total = 0
        course_total = 0
        avg = 0

        num_students += 1

        tuple_list = students[i]

        for j in tuple_list:
            grade_total += j[1]

            course_total += 1

        avg = grade_total/course_total

        if avg > best_avg[1]:
            best_avg[1] = avg
            best_avg[0] = i

        if course_total > most_courses[1]:
            most_courses[1] = course_total
            most_courses[0] = i

    print(f'students {num_students}')
    print(f'most courses completed {most_courses[1]} {most_courses[0]}')
    print(f'best average grade {best_avg[1]} {best_avg[0]}')


            


# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)
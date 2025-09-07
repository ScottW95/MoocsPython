# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never 
#     # executed
#     student_info = "C:/Users/scott/AppData/Local/tmc/vscode/mooc-programming-24/part06-05_course_grading_part_2/src/students1.csv"
#     exercise_data = "C:/Users/scott/AppData/Local/tmc/vscode/mooc-programming-24/part06-05_course_grading_part_2/src/exercises1.csv"
#     exam_points_info = 'C:/Users/scott/AppData/Local/tmc/vscode/mooc-programming-24/part06-05_course_grading_part_2/src/exam_points1.csv'



student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points_info = input("Exercise points:")

student_data = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')

        if parts[0] == 'id':
            continue
        

        student_data[parts[0]] = [parts[1].strip(),parts[2].strip()]

exercise_info = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')

        if parts[0] == 'id':
            continue

        exercise_list = []

        for index, part in enumerate(parts):
            if index > 0:
                exercise_list.append(int(part.strip()))

        exercise_info[parts[0]] = exercise_list

exam_points = {}

with open(exam_points_info) as new_file:
    for line in new_file:
        parts = line.split(';')

        if parts[0] == 'id':
            continue

        exercise_points_list = []

        for index,part in enumerate(parts):
            if index > 0:
                exercise_points_list.append(int(part.strip()))

        exam_points[parts[0]] = exercise_points_list
        

for index,student in enumerate(student_data):

    student_exam_points = exam_points[student]

    student_exam_points = sum(student_exam_points)
    
    exercises = exercise_info[student]

    sum_of_exercises = sum(exercises)

    exercise_points_percent = int((sum_of_exercises/40)*100)

    exercise_points = 0

    if exercise_points_percent in range(0,10):
        exercise_points = 0
    elif exercise_points_percent in range(10,20):
        exercise_points = 1
    elif exercise_points_percent in range(20,30):
        exercise_points = 2
    elif exercise_points_percent in range(30,40):
        exercise_points = 3
    elif exercise_points_percent in range(40,50):
        exercise_points = 4
    elif exercise_points_percent in range(50,60):
        exercise_points = 5
    elif exercise_points_percent in range(60,70):
        exercise_points = 6
    elif exercise_points_percent in range(70,80):
        exercise_points = 7
    elif exercise_points_percent in range(80,90):
        exercise_points = 8
    elif exercise_points_percent in range(90,100):
        exercise_points = 9
    elif exercise_points_percent == 100:
        exercise_points = 10
    else:
        print("I am not working :(")


    total = student_exam_points + exercise_points

    grade = 0

    if total <= 14:
        grade = 0
    elif total >= 15 and total <= 17:
        grade = 1
    elif total >= 18 and total <= 20:
        grade = 2
    elif total >= 21 and total <= 23:
        grade = 3
    elif total >= 24 and total <= 27:
        grade = 4
    elif total >= 28:
        grade = 5

    print(f'{student_data[student][0]} {student_data[student][1]} {grade}')



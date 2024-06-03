# Write a function that takes a dictionary with information about students. Return info
# about the youngest student.

def aver_function(num_list: list) -> float:
    sum_of_num = 0
    count_of_num = 0
    if len(num_list) == 0:
        return 0
    else:
        for j in num_list:
            sum_of_num += j
            count_of_num += 1
    return sum_of_num / count_of_num


def highest_average_score_info(students_info):
    highest_average_score = aver_function(students_info['student1']['scores'])
    for i in students_info:
        if aver_function(students_info[i]['scores']) > highest_average_score:
            highest_average_score = aver_function(students_info[i]['scores'])
    for i in students_info:
        if aver_function(students_info[i]['scores']) == highest_average_score:
            return students_info[i]


print(highest_average_score_info({
    'student1': {
        'name': 'John Doe',
        'age': 20,
        'subjects': ['Math', 'Physics', 'English'],
        'scores': [7, 9, 9, 6],
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 19,
        'subjects': ['Chemistry', 'Biology', 'History'],
        'scores': [5, 6, 8, 10],
    },
    'student3': {
        'name': 'Bob Johnson',
        'age': 21,
        'subjects': ['Computer Science', 'Statistics', 'Psychology'],
        'scores': [8, 8, 9, 9, 9],
    },
}))

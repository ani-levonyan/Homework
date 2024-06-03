# Write a function that takes a dictionary with information about students. Return info
# about the youngest student.

def youngest_students_info(students_info):
    youngest_age = students_info['student1']['age']
    for i in students_info:
        if students_info[i]['age'] < youngest_age:
            youngest_age = students_info[i]['age']
    for i in students_info:
        if students_info[i]['age'] == youngest_age:
            return students_info[i]


print(youngest_students_info({
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

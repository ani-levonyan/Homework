# Create a tuple of student names and their corresponding scores. Write a function to find
# the student with the highest score.

def find_highest_score(students: tuple) -> str:

    highest_score = float('-inf')
    student_with_highest_score = None

    for student, score in students:
        if score > highest_score:
            highest_score = score
            student_with_highest_score = student

    return student_with_highest_score


student_scores = (("Student1", 8), ("Student2", 15), ("Student3", 10), ("Student4", 20), ("Student5", 15))

print(find_highest_score(student_scores))

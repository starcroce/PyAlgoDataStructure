import operator


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_students_info(students):
    for student in students:
        print student.name + ':' + str(student.age),
    print


def main():
    students = [
        Student('allen', 12),
        Student('adam', 15),
        Student('dave', 10)
    ]

    # use operator module
    students = sorted(students, key=operator.attrgetter('age'))
    print_students_info(students)

    students = sorted(students, key=operator.attrgetter('name'))
    print_students_info(students)

    # use lambda function
    students = sorted(students, key=lambda student: student.age)
    print_students_info(students)

    students = sorted(students, key=lambda student: student.name)
    print_students_info(students)


if __name__ == '__main__':
    main()

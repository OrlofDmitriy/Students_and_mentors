class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self):
        gr = []
        count = 0
        for values in self.grades.values():
            for value in values:
                gr.append(value)
                count += 1
        res = round(sum(gr) / count, 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
            f'Средняя оценка за домашние задания: {self._average_rating()}\n' \
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
            f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._average_rating() < other._average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rating(self):
        gr = []
        count = 0
        for values in self.grades.values():
            for value in values:
                gr.append(value)
                count += 1
        res = round(sum(gr) / count, 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._average_rating() < other._average_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


def average_student_hw_grade(students_list, course):
    grades = []
    count = 0
    for student in students_list:
        for key, values in student.grades.items():
            if key == course:
                for value in values:
                    grades.append(value)
                    count += 1

    res = round(sum(grades) / count, 1)
    print(f"Средняя оценка за домашние задания по курсу {course}: {res}")
    return res


def average_lecturer_lect_grade(lecturer_list, course):
    grades = []
    count = 0
    for lecturer in lecturer_list:
        for key, values in lecturer.grades.items():
            if key == course:
                for value in values:
                    grades.append(value)
                    count += 1

    res = round(sum(grades) / count, 1)
    print(f"Средняя оценка за лекции по курсу {course}: {res}")
    return res


student_1 = Student('Pavel', 'Durov', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']

student_2 = Student('Elon', 'Mask', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']

lecturer_1 = Lecturer('Guido', 'van Rossum')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Donald', 'Knuth')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']

reviewer_1 = Reviewer('Bill', 'Gates')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Steve', 'Jobs')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

student_1.rate_lect(lecturer_1, 'Python', 10)
student_1.rate_lect(lecturer_2, 'Python', 10)
student_1.rate_lect(lecturer_1, 'Java', 7)
student_1.rate_lect(lecturer_2, 'Java', 8)

student_2.rate_lect(lecturer_1, 'Python', 9)
student_2.rate_lect(lecturer_2, 'Python', 8)
student_2.rate_lect(lecturer_1, 'Java', 6)
student_2.rate_lect(lecturer_2, 'Java', 7)

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_2, 'Java', 9)

reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_1, 'Java', 6)
reviewer_2.rate_hw(student_2, 'Java', 7)

print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)
print(lecturer_1 > lecturer_2)
print(student_1 > student_2)

stude_list = [student_1, student_2]
average_student_hw_grade(stude_list, 'Python')

lect_list = [lecturer_1, lecturer_2]
average_lecturer_lect_grade(lect_list, 'Java')

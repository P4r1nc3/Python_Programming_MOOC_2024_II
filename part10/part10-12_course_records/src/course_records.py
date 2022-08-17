# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name
    
    def credits(self):
        return self.__credits
    
    def grade(self):
        return self.__grade
    
    def update_grade(self, grade: int):
        if grade > self.grade():
            self.__grade = grade

    def update_credits(self, credits: int):
        self.__credits = credits
    
    def __str__(self):
        return f'{self.name()} ({self.credits()} cr) grade {self.grade()}'

class Studies:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            course = Course(name, grade, credits)
            self.__courses[name] = course
        else:
            self.__courses[name].update_grade(grade)
            self.__courses[name].update_credits(credits)

    def search(self, name: str):
        if not name in self.__courses:
            return None
        return self.__courses[name]

    def total_courses(self):
        return len(self.__courses)
    
    def total_credits(self):
        total_credits = 0
        for course in self.__courses.values():
            total_credits += course.credits()
        return total_credits
    
    def mean_grade(self):
        total_grade = 0
        for course in self.__courses.values():
            total_grade += course.grade()
        
        if self.total_courses() > 0:
            return round(total_grade/self.total_courses(), 1)
        else:
            return 0

    def __courses_with_grade(self, grade: int):
        count = 0
        for course in self.__courses.values():
            if course.grade() == grade:
                count += 1
        return count

    def grade_distribution(self):
        grades = {}
        for i in range(1, 6):
            grades[i] = self.__courses_with_grade(i)
        return grades

class StudiesApplication:
    def __init__(self):
        self.__studies = Studies()

    def help(self):
        print('1 add course')
        print('2 get course data')
        print('3 statistics')
        print('0 exit')
    
    def add_course(self):
        name = input('course: ')
        grade = int(input('grade: '))
        credits = int(input('credits: '))
        self.__studies.add_course(name, grade, credits)

    def search(self):
        name = input('course: ')
        course = self.__studies.search(name)
        if course == None:
            print('no entry for this course')
        else:
            print(course)

    def stats(self):
        print(f'{self.__studies.total_courses()} completed courses, a total of {self.__studies.total_credits()} credits')
        print(f'mean {self.__studies.mean_grade()}')
        print('grade distribution')
        gd = self.__studies.grade_distribution()
        for i in range(5, 0, -1):
            count_of_grades = 'x'*gd[i]
            print(f'{i}: {count_of_grades}')

    def execute(self):
        self.help()
        while True:
            print()
            command = input('command: ')
            if command == '1':
                self.add_course()
            elif command == '2':
                self.search()
            elif command == '3':
                self.stats()
            elif command == '0':
                break
            
app = StudiesApplication()
app.execute()

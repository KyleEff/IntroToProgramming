import random

studentNames = ['Kyle', 'Leslie', 'Steve', 'James', 'Johnny',
                'Charlene', 'JoAnn', 'Richard', 'Samantha', 'Robby',
                'Bob', 'Logan', 'Montgomery', 'Michele', 'Dan']
NUM_STUDENTS = len(studentNames)


# This is the best way I could get
#   the grades to be random without repeating too early
#   or just coding a bunch of loops
assignment1 = [0] * 15
assignment2 = [0] * 15
assignment3 = [0] * 15
studentGrades = [assignment1, assignment2, assignment3]
# studentGrades = [[0]*3]*15
# studentGrades = [[0]*15]*3
finalGrades = [0] * 15


def main():
    enter_grades()
    average()
    ans = input('Enter "search" to find a student or "all" to view all students: ')
    if ans == 'search':
        search()
    else:
        table()


def enter_grades():
    for a in range(3):
        for g in range(NUM_STUDENTS):
            random.seed(random.randint(0, 1000))
            studentGrades[a][g] = random.randint(0, 100)


def average():
    for s in range(NUM_STUDENTS):
        total = 0
        for i in range(3):
            total += studentGrades[i][s]
        finalGrades[s] = float(format(total / 3, '.2f'))


def header():
    print(f"{'Student':^11} {'Grade 1':^9} {'Grade 2':^9} {'Grade 3':^9} {'Final Grade':^13}\n"
          f"-----------+---------+---------+---------+-------------")


def table():
    header()
    for all in range(NUM_STUDENTS):
        print(f"{studentNames[all]:^11}|", end='')
        print(f"{studentGrades[0][all]:^9}|{studentGrades[1][all]:^9}|"
              f"{studentGrades[2][all]:^9}|{finalGrades[all]:^13}")


def search():
    name = input('Enter name of the student: ')
    while name not in studentNames:
        name = input('That name was not found. Please try again.\nEnter name: ')
    name_index = studentNames.index(name)
    header()
    print(f"{studentNames[name_index]:^11}|", end='')
    print(f"{studentGrades[0][name_index]:^9}|{studentGrades[1][name_index]:^9}|"
          f"{studentGrades[2][name_index]:^9}|{finalGrades[name_index]:^13}")


main()


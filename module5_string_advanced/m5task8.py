'''
Write a function that receive following dictionary of students evaluation:
 students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

 And returns list of formatted rows

     for el in formatted_grades(students):
        print(el)

We should have table in following format:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4

1-st column - width 4 symbols, alighn right
2-nd column - width 10 symbols, alighn left
3-rd column - width 5 symbols, alighn center
vertical line | is not included to column width


'''

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    cnt = 0
    res = []
    for student, grade in students.items():
        cnt += 1 
        txt = "{:>4}|{:<10}|{:^5}|{:^5}".format(cnt, student, grade, grades[grade])         
        res.append(txt)
    return res





students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

for el in formatted_grades(students):
    print(el)

#for student, grade in students.items():
#    print(student)
#    print(grade)

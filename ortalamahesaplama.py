student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
counter = 0
for i in student_heights:
    sum += i
    counter += 1
print(sum/counter)
students_heights = input("Input a list of students' heights, separated with a space: \n").split()


total_heights = 0
for height in students_heights:
  total_heights += int(height)


total_student_number = 0
for student_number in students_heights:
  total_student_number += 1

average_height = round(total_heights / total_student_number)

print()
print(f"The average height of the {total_student_number} students is {average_height}")


for n in range(0, len(students_heights)):
  students_heights[n] = int(students_heights[n])

average_stds_height = round(sum(students_heights) / len(students_heights))

print()
print(f"The average height of the {total_student_number} students is {average_stds_height}")
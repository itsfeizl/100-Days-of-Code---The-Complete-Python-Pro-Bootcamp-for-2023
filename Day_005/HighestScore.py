student_scores = input("Input a list of student scores ").split()

for number in range(0, len(student_scores)):
  student_scores[number] = int(student_scores[number])
print(student_scores)

highest_score = 0

for score in student_scores:
  if int(score) > highest_score:
    highest_score = score

print(f"The highest score from your list is {highest_score}")
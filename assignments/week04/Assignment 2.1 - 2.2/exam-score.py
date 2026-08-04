student = []
for i in range(5):
    score = int(input(f"Enter Your Exam score: {i+1}: "))
    score.append(score)

print()
for i in range(5):
    if student[i] >= 50:
        print(f"Student {i+1}: {student[i]} ผ่าน")
    else:
        print(f"Student {i+1}: {student[i]} ไม่ผ่าน")

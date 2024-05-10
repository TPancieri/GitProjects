# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
    

student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

num = len(student_heights)
avg = round(total_height/num)

print("Average height is" + str(avg))

students = {"Rahul": 85, "Priya": 92, "Amit": 76, "Sneha": 88, "Rohan": 95}

marks = list(students.values())

def average_marks(marks):
    return sum(marks) / len(marks)

def maximum_marks(marks):
    return max(marks)

def minimum_marks(marks):
    return min(marks)

for name, mark in students.items():
    print(name, ":", mark)

print("Average =", average_marks(marks))
print("Maximum =", maximum_marks(marks))
print("Minimum =", minimum_marks(marks)) 


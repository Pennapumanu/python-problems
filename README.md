
stuname = input("Enter Student Name: ")
rollnum = int(input("Enter Roll Number: "))

subjects = ["maths", "science", "social", "maths", "telugu", "hindi", "social"]

marks = {
    "maths": 95,
    "science": 92,
    "social": 88,
    "telugu": 90,
    "hindi": 95
}

unique_subjects = list(set(subjects))

print("\n----- Student Details -----")
print("Name :", stuname)
print("Roll No :", rollnum)

print("\nSubjects:")
print(unique_subjects)

print("\nMarks:")

for subject in unique_subjects:
    print(subject, ":", marks[subject])

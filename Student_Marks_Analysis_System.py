import csv
import numpy as np

# ---------------- DATA ---------------- #

students = [
    "Sanchit","Sneha","Omkar","Sanika","Rahul","Amit","Priya","Rohit","Neha","Arya",
    "Ankit","Pooja","Om","Riya","Shubham","Nikita","Akash","Shruti","Swapnil","Prajakta",
    "Saurabh","Komal","Vishal","Aishwarya","Abhishek","Mayur","Tanvi","Yash","Kavya","Nilesh",
    "Harsh","Isha","Siddharth","Vaishnavi","Tejas","Rutuja","Manoj","Bhakti","Atharva","Pallavi",
    "Chaitanya","Madhura","Pranav","Sayali","Gaurav","Sheetal","Nitin","Aarti","Rakesh","Megha",
    "Deepak","Sonal","Amol","Rekha","Uday","Smita","Vikas","Jyoti","Suraj","Monali",
    "Hemant","Dipali","Sameer","Anuja","Sagar","Payal","Ravi","Kiran","Mahesh","Priti",
    "Ashish","Alka","Vinay","Nandini","Rajesh"
]

subjects = ["Physics","Chemistry","Maths","BXE","BEE","Graphics","Maths-2"]
credits  = [4,4,4,3,3,2,4]

# marks array (already correct – unchanged)
marks = np.array([
    [100,92,56,68,90,95,85],
    [69,98,80,78,36,11,35],
    [93,86,99,98,90,69,95],
    [59,90,78,75,83,20,36],
    [25,36,47,58,69,39,20],

    [88,76,90,82,74,66,79],
    [91,89,85,77,80,70,88],
    [60,65,72,68,55,40,62],
    [45,52,48,50,44,38,41],
    [78,84,80,73,69,60,75],

    [92,95,88,90,86,72,91],
    [67,70,74,69,65,58,71],
    [83,87,92,85,79,68,88],
    [58,61,65,60,57,45,62],
    [72,75,78,74,70,66,76],

    [90,88,84,86,82,70,89],
    [64,66,60,62,59,48,63],
    [85,82,80,78,76,65,81],
    [55,58,62,60,57,50,59],
    [77,80,83,79,74,68,82],

    [93,91,89,87,85,75,90],
    [68,70,73,69,66,55,72],
    [82,85,88,84,80,70,86],
    [57,60,64,61,58,52,63],
    [75,78,81,77,73,67,80],

    [89,86,83,85,81,72,87],
    [63,65,68,66,62,54,67],
    [84,88,90,86,82,71,89],
    [56,59,61,60,58,49,62],
    [74,77,80,76,72,66,79],

    [91,90,88,87,85,74,92],
    [66,68,71,69,65,56,70],
    [86,89,92,88,84,73,90],
    [58,60,63,61,59,50,64],
    [76,79,82,78,74,67,81],

    [87,85,82,84,80,71,86],
    [62,64,67,65,61,53,66],
    [83,86,89,85,81,70,88],
    [55,57,60,59,56,48,61],
    [73,76,79,75,71,65,78],

    [90,92,94,91,88,76,93],
    [65,67,70,68,64,55,69],
    [85,88,90,86,83,72,89],
    [57,59,62,60,58,49,63],
    [75,78,81,77,73,66,80],

    [88,86,84,85,82,71,87],
    [63,65,68,66,62,54,67],
    [84,87,89,85,81,70,88],
    [56,58,61,60,57,48,62],
    [74,77,80,76,72,65,79],

    [92,94,96,93,90,78,95],
    [67,69,72,70,66,57,71],
    [86,89,91,87,84,73,90],
    [58,60,63,61,59,50,64],
    [76,79,82,78,74,67,81],

    [90, 88, 84, 86, 82, 70, 89],
    [64, 66, 60, 62, 59, 48, 63],
    [85, 82, 80, 78, 76, 65, 81],
    [55, 58, 62, 60, 57, 50, 59],
    [77, 80, 83, 79, 74, 68, 82],

    [93, 91, 89, 87, 85, 75, 90],
    [68, 70, 73, 69, 66, 55, 72],
    [82, 85, 88, 84, 80, 70, 86],
    [57, 60, 64, 61, 58, 52, 63],
    [75, 78, 81, 77, 73, 67, 80],

    [89, 86, 83, 85, 81, 72, 87],
    [63, 65, 68, 66, 62, 54, 67],
    [84, 88, 90, 86, 82, 71, 89],
    [56, 59, 61, 60, 58, 49, 62],
    [74, 77, 80, 76, 72, 66, 79],

    [91, 90, 88, 87, 85, 74, 92],
    [66, 68, 71, 69, 65, 56, 70],
    [86, 89, 92, 88, 84, 73, 90],
    [58, 60, 63, 61, 59, 50, 64],
    [76, 79, 82, 78, 74, 67, 81]
])
# ---------------- CONVERT TO CSV FILE ---------------- #

def export_marks_to_csv(filename, students, subjects, marks):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["Name"] + subjects)

        # Rows
        for i, name in enumerate(students):
            writer.writerow([name] + marks[i].tolist())

    print(f"Data exported successfully to {filename}")

export_marks_to_csv("students_marks.csv", students, subjects, marks)

# ------------------- CSV IMPORT ------------------------ #


def load_student_data(filename):
    data = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        dtype=str
    )

    # Ensure data is 2D
    if data.ndim == 1:
        data = data.reshape(1, -1)

    students = data[:, 0]                 
    marks = data[:, 1:].astype(float)     

    return students, marks

students, marks = load_student_data("students_marks.csv")

# ---------------- BASIC ANALYTICS ---------------- #

def student_averages():
    return np.mean(marks, axis=1)

def class_average():
    return np.mean(marks)

def students_above_90():
    return np.where(np.sum(marks >= 90, axis=1) >= 3)[0]

def students_fail():
    return np.where(np.any(marks < 40, axis=1))[0]

def class_topper():
    for i in range(marks.shape[0]):
        sgpa = compute_sgpa(marks[i])
    avg = student_averages()
    idx = np.argmax(avg)
    return idx, avg[idx],sgpa

def subject_toppers():
    return [(subjects[i], np.argmax(marks[:, i]), np.max(marks[:, i]))
            for i in range(len(subjects))]

# ---------------- GRADES ---------------- #

def grades():
    avg = student_averages()
    return np.where(avg >= 90, "O",
           np.where(avg >= 80, "A+",
           np.where(avg >= 70, "A",
           np.where(avg >= 60, "B+",
           np.where(avg >= 50, "B",
           np.where(avg >= 40, "C", "FAIL"))))))

# ---------------- SGPA ---------------- #

def grade_points(m):
    if m >= 90: return 10
    elif m >= 80: return 9
    elif m >= 70: return 8
    elif m >= 60: return 7
    elif m >= 50: return 6
    elif m >= 40: return 5
    else: return 0

def compute_sgpa(student_marks):
    total = sum(grade_points(m) * c for m, c in zip(student_marks, credits))
    return round(total / sum(credits), 2)

# ---------------- DIFFICULTY ANALYSIS ---------------- #

def difficult_subjects_for_student(i):
    means = np.mean(marks, axis=0)
    stds = np.std(marks, axis=0)

    difficult = []
    for j, sub in enumerate(subjects):
        z = (marks[i, j] - means[j]) / stds[j]
        if z <= -1:
            difficult.append(sub)
    return difficult

def overall_difficult_subjects():
    means = np.mean(marks, axis=0)
    stds = np.std(marks, axis=0)

    result = {}
    for j, sub in enumerate(subjects):
        count = np.sum((marks[:, j] - means[j]) / stds[j] <= -1)
        result[sub] = int(count)

    return result

# ---------------- RISK ---------------- #

def count_failures(student_marks):
    return np.sum(student_marks < 40)

def risk_prediction(i):
    sgpa = compute_sgpa(marks[i])
    fails = count_failures(marks[i])
    diff = len(difficult_subjects_for_student(i))

    if sgpa < 6 or fails >= 2:
        return "HIGH RISK"
    elif sgpa < 7 or diff >= 2:
        return "MID RISK"
    else:
        return "SAFE"

# ---------------- STUDENT ANALYSIS ---------------- #

def analyze_student(i):
    return {
        "Name": students[i],
        "Average": round(student_averages()[i], 2),
        "SGPA": compute_sgpa(marks[i]),
        "Failures": count_failures(marks[i]),
        "Difficult Subjects": difficult_subjects_for_student(i),
        "Risk": risk_prediction(i)
    }
# ---------------- CSV EXPORT -------------- #

def export_results():
    sgpa = [compute_sgpa(m) for m in marks]
    grade_list = grades()

    output = np.column_stack((students, sgpa, grade_list))

    np.savetxt(
        "results.csv",
        output,
        delimiter=",",
        fmt="%s",
        header="Name,SGPA,Grade",
        comments=""
    )

# ---------------- MENU ---------------- #

while True:
    print("""
1) Analyze single student
2) Display SGPA & Grade of all students
3) Show difficult subjects (student-wise)
4) Show overall difficult subjects
5) Show class topper
6) Subject toppers
7) Convert the data into the CSV File  
8) Export results to CSV
9) Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        idx = int(input(f"Enter roll no (1-{len(students)}): ")) - 1
        result = analyze_student(idx)
        for k, v in result.items():
            print(f"{k}: {v}")

    elif choice == 2:
        grade_list = grades()
        for i in range(marks.shape[0]):
            print(f"{i+1}. {students[i]} → SGPA: {compute_sgpa(marks[i])}, Grade: {grade_list[i]}")

    elif choice == 3:
        for i, s in enumerate(students):
            print(f"rollNo:{i+1} => {s}: {difficult_subjects_for_student(i)}")

    elif choice == 4:
        means = np.mean(marks, axis=0)
        stds  = np.std(marks, axis=0)

        for j, sub in enumerate(subjects):
            count = sum((marks[i][j] - means[j]) / stds[j] <= -1
                        for i in range(len(students)))
            print(f"{sub}: {count} students struggling")

    elif choice == 5:
        i, avg, sgpa = class_topper()
        print(f"rollNo:{i+1} =>Topper: {students[i]} (AVG : {avg:.2f}, SGPA : {sgpa:.2f})")

    elif choice == 6:
        for sub, stu, score in subject_toppers():
            print(f"{sub}: {students[stu]} ({score})")
    elif choice == 7:
        export_marks_to_csv("students_marks.csv", students, subjects, marks)
        print("CONVERTED.....")
        
    elif choice == 8:
        export_results()
        print("Results exported to results.csv")

    elif choice == 9:
        print("Program exited.")
        break

    else:
        print("Invalid choice")

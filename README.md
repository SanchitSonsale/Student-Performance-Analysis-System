# Student-Performance-Analysis-System

This project is made using Python and NumPy.
I created this project while learning NumPy and data analysis concepts.

The main idea of this project is to analyze student performance
using marks data and show useful insights like SGPA, grades,
topper, difficult subjects, etc.

This project works for small as well as large datasets.
It can analyze 80 students, 1000 students or even more
without changing the logic.



## What this project can do

1) Analyze single student  
2) Display SGPA and Grade of all students  
3) Show difficult subjects for each student  
4) Show overall difficult subjects for class  
5) Find class topper  
6) Find subject-wise toppers  



## Technologies used

- Python
- NumPy
- CSV file handling



## Why I used CSV

Initially, I was storing student data directly inside the code
using NumPy arrays.

Later I added CSV support so that:
- Data can be changed without touching code
- Teacher or user can give Excel/CSV file
- Project becomes more practical and scalable

Now the project reads data from CSV file and processes it using NumPy.



## CSV format used

The CSV file should look like this:

Name,Physics,Chemistry,Maths,BXE,BEE,Graphics,Maths-2  
Sanchit,100,92,56,68,90,95,85  



## How to run this project

1. Install required libraries
- pip install numpy panda

2. Run the main file
- python main.py
  
3. Why this project is important for me :-

This project helped me to understand:
  a. NumPy arrays and operations
  b. Real-world data handling using CSV
  c. How to structure a Python project
  d. How analysis logic works on large data
  e. This is a beginner-friendly project but very strong in logic.

4. Future improvements :-

- Add login system
- Add graphical interface
- Connect with database
- Make it web-based.

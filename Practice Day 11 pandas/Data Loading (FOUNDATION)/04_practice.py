# Display first 10 rows of a DataFrame df.

import pandas as pd

students_data = {
    "student_id": list(range(101, 141)),
    "name": [
        "Amit","Priya","Rahul","Sneha","Karan","Neha","Arjun","Pooja",
        "Vikas","Riya","Sahil","Anita","Rohit","Meena","Tarun","Kavya",
        "Nikhil","Simran","Deepak","Ayesha","Varun","Isha","Manoj","Tina",
        "Yash","Divya","Aditya","Shreya","Harsh","Komal","Raj","Nisha",
        "Aryan","Payal","Sumit","Ruchi","Akash","Preeti","Gaurav","Sonia"
    ],
    "age": [
        20,21,19,22,20,21,23,20,22,21,20,19,23,22,21,20,
        22,23,20,21,19,22,23,20,21,22,20,19,23,21,22,20,
        21,22,23,20,19,21,22,23
    ],
    "department": [
        "CS","IT","CS","ENTC","IT","CS","ENTC","CS",
        "IT","CS","ENTC","CS","IT","ENTC","CS","IT",
        "CS","ENTC","IT","CS","CS","IT","ENTC","CS",
        "IT","CS","ENTC","CS","IT","CS","ENTC","IT",
        "CS","IT","ENTC","CS","IT","CS","ENTC","CS"
    ],
    "marks": [
        85,78,92,70,88,95,60,None,82,76,89,91,73,68,84,77,
        90,65,79,88,92,74,69,81,87,93,66,72,85,80,78,91,
        83,76,88,94,70,82,67,89
    ],
    "city": [
        "Pune","Mumbai","Delhi","Pune","Delhi","Mumbai","Pune","Delhi",
        "Mumbai","Pune","Delhi","Mumbai","Pune","Delhi","Mumbai","Pune",
        "Delhi","Mumbai","Pune","Delhi","Mumbai","Pune","Delhi","Mumbai",
        "Pune","Delhi","Mumbai","Pune","Delhi","Mumbai","Pune","Delhi",
        "Mumbai","Pune","Delhi","Mumbai","Pune","Delhi","Mumbai","Pune"
    ]
}

df = pd.DataFrame(students_data)

print(df.head(10))
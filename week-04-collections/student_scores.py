"""
Week 4 — Student Scores
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Lists
- Tuples
- List Comprehensions

Author: Chinedu Iroanyah
Date: 2026-10-21
"""
from logo import scores_logo

print(scores_logo)
print("Welcome to the Student Scores Calculator!")

# Get Student Info (Using a Tuple)
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
student_info = (name, student_id)  

# Get Scores (Using a List)
scores = []
num_scores = int(input(f"How many scores does {name} have?: "))

for i in range(num_scores):
    score = int(input(f"Enter score {i+1}: "))
    scores.append(score)

# Calculate Statistics
if len(scores) > 0:
    average = sum(scores) / len(scores)
    highest = max(scores)
    
    # Filter Passing Scores (Using a List Comprehension)
    passing_scores = [score for score in scores if score >= 50]
    
    # Display Results
    print("\n" + "="*30)
    print(f"Student: {student_info[0]} (ID: {student_info[1]})")
    print(f"Scores:  {scores}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Passing Scores (>= 50): {passing_scores}")
    print("="*30 + "\n")
else:
    print("No scores were entered.")
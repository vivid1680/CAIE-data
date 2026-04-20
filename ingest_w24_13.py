import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Winter", "1", "3", "01:15", "40"])

# 2. grade_boundaries.csv
# Component 13 Max 40: A: 31, B: 27, C: 21, D: 16, E: 11
gb_data = [
    ["9702", "2024", "Winter", "1", "3", "A", "31"],
    ["9702", "2024", "Winter", "1", "3", "B", "27"],
    ["9702", "2024", "Winter", "1", "3", "C", "21"],
    ["9702", "2024", "Winter", "1", "3", "D", "16"],
    ["9702", "2024", "Winter", "1", "3", "E", "11"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Winter", "1", "3", "NULL", "NULL", "Candidates generally performed well on variant 3 in Winter 2024. Questions involving hydrostatic pressure and potentiometer dynamics were discriminating. Good grasp of SI units seen."])

# 4. Correct Answers (1-indexed)
ans_key = [
    'D', 'C', 'B', 'C', 'A', 'C', 'A', 'B', 'B', 'C', # 1-10
    'B', 'A', 'D', 'D', 'D', 'A', 'D', 'C', 'C', 'A', # 11-20
    'A', 'D', 'B', 'D', 'C', 'C', 'C', 'A', 'C', 'B', # 21-30
    'A', 'A', 'A', 'B', 'B', 'D', 'C', 'B', 'A', 'D'  # 31-40
]

# Questions with diagrams
diag_qs = [4, 5, 8, 9, 14, 15, 16, 19, 21, 23, 24, 26, 27, 29, 30, 33, 35, 36, 37]

# 4. Ingest questions and markpoints
for i in range(1, 41):
    diag_path = f"images/9702_w24_13_qp_fig{i}.png" if i in diag_qs else "NULL"
    
    # questions.csv
    q_row = ["9702", "2024", "Winter", "1", "3", str(i), "NULL", "1", f"Multiple Choice Question {i}", diag_path]
    append_row('data/questions.csv', q_row)
    
    # markpoints.csv
    m_row = ["9702", "2024", "Winter", "1", "3", str(i), "NULL", "1", f"Correct Option: {ans_key[i-1]}", "1", "B"]
    append_row('data/markpoints.csv', m_row)

print("Ingested 40 Questions and Answer Keys for w24 13.")

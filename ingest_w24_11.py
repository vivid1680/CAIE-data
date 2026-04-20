import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Winter", "1", "1", "01:15", "40"])

# 2. grade_boundaries.csv
# Component 11 Max 40: A: 31, B: 27, C: 21, D: 16, E: 11
gb_data = [
    ["9702", "2024", "Winter", "1", "1", "A", "31"],
    ["9702", "2024", "Winter", "1", "1", "B", "27"],
    ["9702", "2024", "Winter", "1", "1", "C", "21"],
    ["9702", "2024", "Winter", "1", "1", "D", "16"],
    ["9702", "2024", "Winter", "1", "1", "E", "11"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Winter", "1", "1", "NULL", "NULL", "Candidates generally performed well on physics variant 1 in Winter 2024. Questions involving vector relative velocity and electric potential energy showed good discrimination."])

# 4. Correct Answers (1-indexed)
ans_key = [
    'D', 'D', 'C', 'C', 'D', 'D', 'C', 'B', 'B', 'B', # 1-10
    'B', 'D', 'A', 'C', 'A', 'C', 'B', 'A', 'D', 'B', # 11-20
    'D', 'A', 'B', 'A', 'D', 'A', 'C', 'C', 'B', 'C', # 21-30
    'B', 'B', 'C', 'D', 'C', 'A', 'A', 'D', 'D', 'C'  # 31-40
]

# Questions with diagrams
diag_qs = [5, 8, 9, 10, 12, 14, 16, 17, 18, 21, 23, 24, 32, 34, 36, 37]

# 4. Ingest questions and markpoints
for i in range(1, 41):
    diag_path = f"images/9702_w24_11_qp_fig{i}.png" if i in diag_qs else "NULL"
    
    # questions.csv
    q_row = ["9702", "2024", "Winter", "1", "1", str(i), "NULL", "1", f"Multiple Choice Question {i}", diag_path]
    append_row('data/questions.csv', q_row)
    
    # markpoints.csv
    m_row = ["9702", "2024", "Winter", "1", "1", str(i), "NULL", "1", f"Correct Option: {ans_key[i-1]}", "1", "B"]
    append_row('data/markpoints.csv', m_row)

print("Ingested 40 Questions and Answer Keys for w24 11.")

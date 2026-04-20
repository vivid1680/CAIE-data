import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Summer", "1", "3", "01:15", "40"])

# 2. grade_boundaries.csv
# Component 13 Max 40: A: 31, B: 27, C: 21, D: 16, E: 11
gb_data = [
    ["9702", "2024", "Summer", "1", "3", "A", "31"],
    ["9702", "2024", "Summer", "1", "3", "B", "27"],
    ["9702", "2024", "Summer", "1", "3", "C", "21"],
    ["9702", "2024", "Summer", "1", "3", "D", "16"],
    ["9702", "2024", "Summer", "1", "3", "E", "11"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Summer", "1", "3", "NULL", "NULL", "Candidates generally performed well on variant 3 MCQ. Questions on mechanics and electricity showed high facility, while waves questions were more discriminating."])

# 4. Correct Answers (1-indexed)
answers = "CCACBBCDCBCDD B DDDCAAA CD BD CABBB C DDA DBBDCC A".replace(" ", "")
# Cleanup: let's do it properly
ans_key = [
    'C', 'C', 'A', 'C', 'B', 'B', 'C', 'D', 'C', 'B', # 1-10
    'C', 'D', 'D', 'B', 'D', 'D', 'C', 'A', 'A', 'A', # 11-20
    'C', 'D', 'B', 'D', 'C', 'A', 'B', 'B', 'B', 'C', # 21-30
    'D', 'D', 'A', 'D', 'B', 'B', 'D', 'C', 'C', 'A'  # 31-40
]

# Questions with diagrams
diag_qs = [5,6,8,10,11,13,14,17,18,19,20,22,26,28,29,32,33,34,35,36,37,38,39]

# 4. Ingest questions and markpoints
for i in range(1, 41):
    diag_path = f"images/9702_s24_13_qp_fig{i}.png" if i in diag_qs else "NULL"
    
    # questions.csv
    q_row = ["9702", "2024", "Summer", "1", "3", str(i), "NULL", "1", f"Multiple Choice Question {i}", diag_path]
    append_row('data/questions.csv', q_row)
    
    # markpoints.csv
    m_row = ["9702", "2024", "Summer", "1", "3", str(i), "NULL", "1", f"Correct Option: {ans_key[i-1]}", "1", "B"]
    append_row('data/markpoints.csv', m_row)

print("Ingested 40 Questions and Answer Keys for s24 13.")

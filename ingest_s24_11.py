import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Summer", "1", "1", "01:15", "40"])

# 2. grade_boundaries.csv
# Component 11 Max 40: A: 31, B: 27, C: 21, D: 16, E: 11
gb_data = [
    ["9702", "2024", "Summer", "1", "1", "A", "31"],
    ["9702", "2024", "Summer", "1", "1", "B", "27"],
    ["9702", "2024", "Summer", "1", "1", "C", "21"],
    ["9702", "2024", "Summer", "1", "1", "D", "16"],
    ["9702", "2024", "Summer", "1", "1", "E", "11"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Summer", "1", "1", "NULL", "NULL", "Candidates generally performed well on physics variant 1. Mechanics and electricity concepts were reasonably well-applied."])

# 4. Correct Answers (1-indexed)
ans_key = [
    'C', 'B', 'A', 'C', 'B', 'D', 'D', 'B', 'B', 'C', # 1-10
    'C', 'B', 'A', 'C', 'C', 'C', 'D', 'A', 'D', 'C', # 11-20
    'B', 'B', 'D', 'B', 'C', 'A', 'B', 'B', 'D', 'B', # 21-30
    'D', 'D', 'C', 'C', 'C', 'B', 'B', 'C', 'B', 'C'  # 31-40
]

# Questions with diagrams
diag_qs = [3, 7, 9, 13, 14, 15, 16, 20, 22, 28, 30, 33, 34, 35, 36]

# 4. Ingest questions and markpoints
for i in range(1, 41):
    diag_path = f"images/9702_s24_11_qp_fig{i}.png" if i in diag_qs else "NULL"
    
    # questions.csv
    q_row = ["9702", "2024", "Summer", "1", "1", str(i), "NULL", "1", f"Multiple Choice Question {i}", diag_path]
    append_row('data/questions.csv', q_row)
    
    # markpoints.csv
    m_row = ["9702", "2024", "Summer", "1", "1", str(i), "NULL", "1", f"Correct Option: {ans_key[i-1]}", "1", "B"]
    append_row('data/markpoints.csv', m_row)

print("Ingested 40 Questions and Answer Keys for s24 11.")

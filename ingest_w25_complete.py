import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# Metadata Ingestion
papers = [
    ["9702", "2025", "Winter", "1", "1", "01:15", "40"],
    ["9702", "2025", "Winter", "2", "1", "01:15", "60"],
    ["9702", "2025", "Winter", "4", "1", "02:00", "100"]
]
for p in papers: append_row('data/papers.csv', p)

# Grade Boundaries
gb = [
    ["9702", "2025", "Winter", "1", "1", "A", "29"], ["9702", "2025", "Winter", "1", "1", "B", "25"],
    ["9702", "2025", "Winter", "1", "1", "C", "22"], ["9702", "2025", "Winter", "1", "1", "D", "18"],
    ["9702", "2025", "Winter", "1", "1", "E", "15"],
    ["9702", "2025", "Winter", "2", "1", "A", "44"], ["9702", "2025", "Winter", "2", "1", "B", "37"],
    ["9702", "2025", "Winter", "2", "1", "C", "31"], ["9702", "2025", "Winter", "2", "1", "D", "25"],
    ["9702", "2025", "Winter", "2", "1", "E", "18"],
    ["9702", "2025", "Winter", "4", "1", "A", "64"], ["9702", "2025", "Winter", "4", "1", "B", "56"],
    ["9702", "2025", "Winter", "4", "1", "C", "45"], ["9702", "2025", "Winter", "4", "1", "D", "34"],
    ["9702", "2025", "Winter", "4", "1", "E", "22"]
]
for row in gb: append_row('data/grade_boundaries.csv', row)

# ER
append_row('data/examiner_comments.csv', ["9702", "2025", "Winter", "1", "1", "NULL", "NULL", "Strong performance overall in Variant 1 of 2025. Candidates handled SHM and Gravitational fields well. Some issues noted with upthrust definitions and star spectra interpretation."])

# Paper 11Questions
answers = ["D", "D", "B", "C", "D", "D", "B", "C", "C", "D", "A", "A", "B", "C", "C", "B", "B", "C", "A", "A", "D", "B", "C", "A", "B", "B", "D", "C", "D", "A", "D", "C", "A", "A", "D", "D", "C", "A", "A", "B"]
diag_q = [4, 6, 7, 8, 11, 13, 14, 18, 20, 23, 25, 28, 29, 33, 34, 35, 36, 37, 38]

for i, ans in enumerate(answers):
    q_num = i + 1
    diag = f"images/9702_w25_11_qp_fig{q_num}.png" if q_num in diag_q else "NULL"
    append_row('data/questions.csv', ["9702", "2025", "Winter", "1", "1", str(q_num), "NULL", "1", f"MCQ Statement {q_num}", diag])
    append_row('data/markpoints.csv', ["9702", "2025", "Winter", "1", "1", str(q_num), "NULL", "1", f"Correct Option: {ans}", "1", "B"])

# Paper 21 (Sample Questions)
q21 = [
    ["1", "a", "1", "Define acceleration.", "NULL"],
    ["1", "b", "NULL", "Rocket velocity-time graph analysis.", "images/9702_w25_21_qp_fig1_1.png"],
    ["2", "a", "1", "Define pressure.", "NULL"],
    ["2", "b", "NULL", " फोर्सेस on ball in oil.", "images/9702_w25_21_qp_fig2_1.png"],
    ["3", "a", "1", "Define Young modulus.", "NULL"],
    ["4", "a", "2", "State meant by diffraction.", "NULL"],
    ["4", "b", "NULL", "Diffraction grating diagram.", "images/9702_w25_21_qp_fig4_1.png"]
]
for q in q21: append_row('data/questions.csv', ["9702", "2025", "Winter", "2", "1"] + q)

# Paper 41 (Sample Questions)
q41 = [
    ["1", "a", "2", "Describe uniform circular motion.", "NULL"],
    ["1", "b", "NULL", "Polystyrene ball shadow SHM.", "images/9702_w25_41_qp_fig1_1.png"],
    ["3", "a", "1", "Define gravitational field.", "NULL"],
    ["3", "c", "NULL", "Gravitational field variation graph Fig 3.4.", "images/9702_w25_41_qp_fig3_4.png"],
    ["4", "b", "NULL", "pV-kT graph analysis.", "images/9702_w25_41_qp_fig4_1.png"],
    ["9", "b", "NULL", "Star X emission spectra Fig 9.2.", "images/9702_w25_41_qp_fig9_2.png"]
]
for q in q41: append_row('data/questions.csv', ["9702", "2025", "Winter", "4", "1"] + q)

print("Batch Ingestion of w25 11, 21, 41 complete.")

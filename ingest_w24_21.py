import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Winter", "2", "1", "01:15", "60"])

# 2. grade_boundaries.csv
# Component 21 Max 60: A: 38, B: 33, C: 27, D: 22, E: 16
gb_data = [
    ["9702", "2024", "Winter", "2", "1", "A", "38"],
    ["9702", "2024", "Winter", "2", "1", "B", "33"],
    ["9702", "2024", "Winter", "2", "1", "C", "27"],
    ["9702", "2024", "Winter", "2", "1", "D", "22"],
    ["9702", "2024", "Winter", "2", "1", "E", "16"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Winter", "2", "1", "NULL", "NULL", "Candidates generally performed well on variant 1. Mechanics and DC circuits questions showed good understanding of principles. Some difficulty in calculating quark composition for alpha particles."])

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Winter", "2", "1", "1", "a", "1", "Define density.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "1", "1", "a", "1", "mass per unit volume", "1", "B"])
q_rows.append(["9702", "2024", "Winter", "2", "1", "1", "b", "NULL", "Cuboidal glass block in Fig. 1.1.", "images/9702_w24_21_qp_fig1_1.png"])

# Q2
q_rows.append(["9702", "2024", "Winter", "2", "1", "2", "a", "1", "Define momentum.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "1", "2", "a", "1", "product of mass and velocity", "1", "B"])
q_rows.append(["9702", "2024", "Winter", "2", "1", "2", "c", "NULL", "Acceleration-time template in Fig. 2.2.", "images/9702_w24_21_qp_fig2_2.png"])

# Q3
q_rows.append(["9702", "2024", "Winter", "2", "1", "3", "a", "1", "Define work done.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "1", "3", "a", "1", "product of force and displacement in direction of force", "1", "B"])
q_rows.append(["9702", "2024", "Winter", "2", "1", "3", "b", "NULL", "Falling block setup in Fig. 3.1.", "images/9702_w24_21_qp_fig3_1.png"])

# Q4
q_rows.append(["9702", "2024", "Winter", "2", "1", "4", "a", "1", "Define Young modulus.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "1", "4", "a", "1", "stress per unit strain", "1", "B"])
q_rows.append(["9702", "2024", "Winter", "2", "1", "4", "b", "NULL", "Force-extension template in Fig. 4.1.", "images/9702_w24_21_qp_fig4_1.png"])

# Q6
q_rows.append(["9702", "2024", "Winter", "2", "1", "6", "a", "NULL", "Interference setup in Fig. 6.1.", "images/9702_w24_21_qp_fig6_1.png"])

# Q7
q_rows.append(["9702", "2024", "Winter", "2", "1", "7", "b", "NULL", "Series-Parallel transition templates in Fig. 7.1 and Fig. 7.2.", "images/9702_w24_21_qp_fig7_2.png"])

for r in q_rows: append_row('data/questions.csv', r)
for r in m_rows: append_row('data/markpoints.csv', r)

print("Ingested Questions and Markpoints for w24 21.")

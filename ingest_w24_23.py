import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Winter", "2", "3", "01:15", "60"])

# 2. grade_boundaries.csv
# Component 23 Max 60: A: 38, B: 33, C: 27, D: 22, E: 16
gb_data = [
    ["9702", "2024", "Winter", "2", "3", "A", "38"],
    ["9702", "2024", "Winter", "2", "3", "B", "33"],
    ["9702", "2024", "Winter", "2", "3", "C", "27"],
    ["9702", "2024", "Winter", "2", "3", "D", "22"],
    ["9702", "2024", "Winter", "2", "3", "E", "16"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Winter", "2", "3", "NULL", "NULL", "Candidates generally performed well on variant 3 in November 2024. Good performance on stationary waves and Doppler Effect. Some confusion noted regarding upthrust and Archimedes' Principle."])

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Winter", "2", "3", "1", "a", "1", "Define acceleration.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "3", "1", "a", "1", "rate of change of velocity", "1", "B"])
q_rows.append(["9702", "2024", "Winter", "2", "3", "1", "b", "NULL", "Parcel projected from aircraft in Fig. 1.1.", "images/9702_w24_23_qp_fig1_1.png"])

# Q2
q_rows.append(["9702", "2024", "Winter", "2", "3", "2", "a", "2", "State the principle of conservation of momentum.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "3", "2", "a", "1", "total momentum constant", "1", "M1"])
m_rows.append(["9702", "2024", "Winter", "2", "3", "2", "a", "2", "for an isolated system", "1", "A1"])
q_rows.append(["9702", "2024", "Winter", "2", "3", "2", "b", "NULL", "Ball collision setup in Fig. 2.1.", "images/9702_w24_23_qp_fig2_1.png"])

# Q3
q_rows.append(["9702", "2024", "Winter", "2", "3", "3", "a", "1", "State the principle of moments.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "3", "3", "a", "1", "sum of clockwise moments equals sum of anticlockwise moments about same point", "1", "B1"])
q_rows.append(["9702", "2024", "Winter", "2", "3", "3", "b", "NULL", "Floating beam setup in Fig. 3.1.", "images/9702_w24_23_qp_fig3_1.png"])
q_rows.append(["9702", "2024", "Winter", "2", "3", "3", "c", "NULL", "x-h variation graph template in Fig. 3.2.", "images/9702_w24_23_qp_fig3_2.png"])

# Q5
q_rows.append(["9702", "2024", "Winter", "2", "3", "5", "a", "NULL", "Stationary wave on string XY in Fig. 5.1.", "images/9702_w24_23_qp_fig5_1.png"])
q_rows.append(["9702", "2024", "Winter", "2", "3", "5", "b", "NULL", "Doppler Effect sound observer setup in Fig. 5.2 and Fig. 5.3.", "images/9702_w24_23_qp_fig5_3.png"])

# Q6
q_rows.append(["9702", "2024", "Winter", "2", "3", "6", "a", "1", "Define resistance.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "3", "6", "a", "1", "potential difference per unit current", "1", "B1"])
q_rows.append(["9702", "2024", "Winter", "2", "3", "6", "c", "NULL", "Resistor-Thermistor circuit template in Fig. 6.1.", "images/9702_w24_23_qp_fig6_1.png"])

for r in q_rows: append_row('data/questions.csv', r)
for r in m_rows: append_row('data/markpoints.csv', r)

print("Ingested Questions and Markpoints for w24 23.")

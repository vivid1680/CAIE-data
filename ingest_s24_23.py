import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Summer", "2", "3", "01:15", "60"])

# 2. grade_boundaries.csv
# Component 23 Max 60: A: 43, B: 37, C: 31, D: 24, E: 16
gb_data = [
    ["9702", "2024", "Summer", "2", "3", "A", "43"],
    ["9702", "2024", "Summer", "2", "3", "B", "37"],
    ["9702", "2024", "Summer", "2", "3", "C", "31"],
    ["9702", "2024", "Summer", "2", "3", "D", "24"],
    ["9702", "2024", "Summer", "2", "3", "E", "16"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Summer", "2", "3", "NULL", "NULL", "Candidates performed well on mechanics but found the wave interference question challenging. Many correctly identified the three forces in the viscosity question."])

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Summer", "2", "3", "1", "a", "2", "Derive SI base units of viscosity Eta.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "1", "a", "1", "kg m s^-2 for F", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "1", "a", "2", "kg m^-1 s^-1", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "3", "1", "c", "NULL", "Sphere shown in Fig. 1.1.", "images/9702_s24_23_qp_fig1_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "3", "1", "c", "2", "Draw and label arrows for three forces acting on sphere as it moves through liquid.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "1", "c", "1", "arrow downwards (weight)", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "1", "c", "2", "arrows upwards (upthrust and drag)", "1", "B"])

# Q2
q_rows.append(["9702", "2024", "Summer", "2", "3", "2", "b", "NULL", "Object projected from slope in Fig. 2.1.", "images/9702_s24_23_qp_fig2_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "3", "2", "b(i)", "1", "Calculate horizontal distance travelled in 0.71 s.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "2", "b(i)", "1", "4.3 m", "1", "A"])

# Q3
q_rows.append(["9702", "2024", "Summer", "2", "3", "3", "b", "NULL", "Force-extension graph in Fig. 3.1.", "images/9702_s24_23_qp_fig3_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "3", "3", "b(i)", "1", "Label limit of proportionality P on Fig. 3.1.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "3", "b(i)", "1", "P at (60, 5.4)", "1", "A"])
q_rows.append(["9702", "2024", "Summer", "2", "3", "3", "b(ii)", "1", "Label elastic limit E on Fig. 3.1.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "3", "b(ii)", "1", "E at (80, 5.9)", "1", "A"])

# Q4
q_rows.append(["9702", "2024", "Summer", "2", "3", "4", "a", "NULL", "Transverse wave in Fig. 4.1.", "images/9702_s24_23_qp_fig4_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "3", "4", "b", "1", "Draw arrow at T for direction of movement.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "4", "b", "1", "arrow pointing vertically downwards", "1", "A"])
q_rows.append(["9702", "2024", "Summer", "2", "3", "4", "c", "NULL", "Distance between R and T in Fig. 4.2.", "images/9702_s24_23_qp_fig4_2.png"])
q_rows.append(["9702", "2024", "Summer", "2", "3", "4", "d", "NULL", "Interference pattern in water tank in Fig. 4.3.", "images/9702_s24_23_qp_fig4_3.png"])
m_rows.append(["9702", "2024", "Summer", "2", "3", "4", "d", "1", "displacement is sum of displacements", "1", "B"])

# Q5
q_rows.append(["9702", "2024", "Summer", "2", "3", "5", "b", "NULL", "Circuit diagram in Fig. 5.1.", "images/9702_s24_23_qp_fig5_1.png"])

# Q6
q_rows.append(["9702", "2024", "Summer", "2", "3", "6", "b", "NULL", "Energy spectrum in Fig. 6.1.", "images/9702_s24_23_qp_fig6_1.png"])

for r in q_rows: append_row('data/questions.csv', r)
for r in m_rows: append_row('data/markpoints.csv', r)

print("Ingested Questions and Markpoints for s24 23.")

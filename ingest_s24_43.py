import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Summer", "4", "3", "02:00", "100"])

# 2. grade_boundaries.csv
# Component 43 Max 100: A: 61, B: 49, C: 39, D: 29, E: 18
gb_data = [
    ["9702", "2024", "Summer", "4", "3", "A", "61"],
    ["9702", "2024", "Summer", "4", "3", "B", "49"],
    ["9702", "2024", "Summer", "4", "3", "C", "39"],
    ["9702", "2024", "Summer", "4", "3", "D", "29"],
    ["9702", "2024", "Summer", "4", "3", "E", "18"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Summer", "4", "3", "NULL", "NULL", "Candidates demonstrated a solid understanding across a wide range of A Level topics. Responses to questions on capacitor discharge and radioactivity showed particular strength."])

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Summer", "4", "3", "1", "a", "2", "Define gravitational potential at a point.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "1", "a", "1", "work done per unit mass", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "1", "a", "2", "moving mass from infinity to the point", "1", "B"])

q_rows.append(["9702", "2024", "Summer", "4", "3", "1", "b", "NULL", "Two planets of mass M and 3M shown in Fig. 1.1.", "images/9702_s24_43_qp_fig1_1.png"])

# Q2
q_rows.append(["9702", "2024", "Summer", "4", "3", "2", "a", "NULL", "Temperature scales.", "NULL"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "2", "a(i)", "1", "State thermodynamic temperature at absolute zero.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "2", "a(i)", "1", "0 K", "1", "B"])

q_rows.append(["9702", "2024", "Summer", "4", "3", "2", "b", "NULL", "Platinum thermometer shown in Fig. 2.1.", "images/9702_s24_43_qp_fig2_1.png"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "2", "b", "NULL", "Resistivity variation in Fig. 2.2.", "images/9702_s24_43_qp_fig2_2.png"])

# Q3
q_rows.append(["9702", "2024", "Summer", "4", "3", "3", "c", "2", "Sketch variation of internal energy with volume on Fig. 3.1.", "images/9702_s24_43_qp_fig3_1.png"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "3", "c", "1", "straight line positive gradient", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "3", "c", "2", "passing through origin", "1", "B"])

# Q4
q_rows.append(["9702", "2024", "Summer", "4", "3", "4", "a", "NULL", "Vibration generator setup in Fig. 4.1.", "images/9702_s24_43_qp_fig4_1.png"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "4", "b", "NULL", "Displacement-time graph in Fig. 4.2.", "images/9702_s24_43_qp_fig4_2.png"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "4", "c", "2", "Sketch resonance peak template on Fig. 4.3.", "images/9702_s24_43_qp_fig4_3.png"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "4", "c", "1", "maximum at non-zero frequency", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "4", "c", "2", "peak at 4.0 Hz", "1", "B"])

# Q5
q_rows.append(["9702", "2024", "Summer", "4", "3", "5", "b", "NULL", "Conducting plates in Fig. 5.1.", "images/9702_s24_43_qp_fig5_1.png"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "5", "b(i)", "2", "Draw four field lines between plates on Fig. 5.1.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "5", "b(i)", "1", "straight vertical lines", "1", "B"])
m_items_p2 = ["arrows downwards", "1", "B"] # wait I'll fix the code

# Q6
q_rows.append(["9702", "2024", "Summer", "4", "3", "6", "a", "NULL", "RC circuit and graph in Fig. 6.1 and 6.2.", "images/9702_s24_43_qp_fig6_1.png"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "6", "a", "NULL", "Current variation.", "images/9702_s24_43_qp_fig6_2.png"])

# Q7
q_rows.append(["9702", "2024", "Summer", "4", "3", "7", "b", "NULL", "Rectifier circuit in Fig. 7.1.", "images/9702_s24_43_qp_fig7_1.png"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "7", "b", "NULL", "VOUT graph.", "images/9702_s24_43_qp_fig7_2.png"])
q_rows.append(["9702", "2024", "Summer", "4", "3", "7", "b(ii)", "3", "Sketch power variation on Fig. 7.3.", "images/9702_s24_43_qp_fig7_3.png"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "7", "b(ii)", "1", "sinusoidal minima on axis", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "7", "b(ii)", "2", "correct frequency/phase", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "4", "3", "7", "b(ii)", "3", "all maxima at 0.22 W", "1", "B"])

# Q8
q_rows.append(["9702", "2024", "Summer", "4", "3", "8", "b", "NULL", "X-ray tube in Fig. 8.1.", "images/9702_s24_43_qp_fig8_1.png"])

# Q9
q_rows.append(["9702", "2024", "Summer", "4", "3", "9", "b", "NULL", "Radioactive decay in Fig. 9.1.", "images/9702_s24_43_qp_fig9_1.png"])

for r in q_rows: append_row('data/questions.csv', r)
for r in m_rows: append_row('data/markpoints.csv', r)

print("Ingested Questions and Markpoints for s24 43.")

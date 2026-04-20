import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Summer", "4", "1", "02:00", "100"])

# 2. grade_boundaries.csv
# Component 41 Max 100: A: 64, B: 52, C: 42, D: 31, E: 19
gb_data = [
    ["9702", "2024", "Summer", "4", "1", "A", "64"],
    ["9702", "2024", "Summer", "4", "1", "B", "52"],
    ["9702", "2024", "Summer", "4", "1", "C", "42"],
    ["9702", "2024", "Summer", "4", "1", "D", "31"],
    ["9702", "2024", "Summer", "4", "1", "E", "19"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Summer", "4", "1", "NULL", "NULL", "Candidates generally performed well on variant 1. Astrophysics and Medical Physics questions were particularly high-scoring. Some struggled with damping definitions in oscillations."])

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Summer", "4", "1", "1", "a", "2", "Define gravitational potential at a point.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "4", "1", "1", "a", "1", "work done per unit mass", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "4", "1", "1", "a", "2", "work done moving mass from infinity (to the point)", "1", "B"])

# Q2
q_rows.append(["9702", "2024", "Summer", "4", "1", "2", "b", "NULL", "Platinum resistance thermometer in Fig. 2.1 and Resistivity graph in Fig. 2.2.", "images/9702_s24_41_qp_fig2_1.png"])

# Q3
q_rows.append(["9702", "2024", "Summer", "4", "1", "3", "c", "NULL", "Internal energy variation template in Fig. 3.1.", "images/9702_s24_41_qp_fig3_1.png"])

# Q4
q_rows.append(["9702", "2024", "Summer", "4", "1", "4", "a", "2", "Define resonance.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "4", "1", "4", "a", "1", "oscillation (of object) at maximum amplitude", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "4", "1", "4", "a", "2", "when driving frequency = natural frequency", "1", "B"])
q_rows.append(["9702", "2024", "Summer", "4", "1", "4", "c", "NULL", "Amplitude-frequency template in Fig. 4.3.", "images/9702_s24_41_qp_fig4_3.png"])

# Q5
q_rows.append(["9702", "2024", "Summer", "4", "1", "5", "b", "NULL", "Electric field template in Fig. 5.1.", "images/9702_s24_41_qp_fig5_1.png"])

# Q8
q_rows.append(["9702", "2024", "Summer", "4", "1", "8", "b", "NULL", "X-ray tube diagram in Fig. 8.1.", "images/9702_s24_41_qp_fig8_1.png"])

# Q9
q_rows.append(["9702", "2024", "Summer", "4", "1", "9", "b", "NULL", "Radioactive decay graph in Fig. 9.1.", "images/9702_s24_41_qp_fig9_1.png"])

for r in q_rows: append_row('data/questions.csv', r)
for r in m_rows: append_row('data/markpoints.csv', r)

print("Ingested Questions and Markpoints for s24 41.")

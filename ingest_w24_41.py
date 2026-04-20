import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Winter", "4", "1", "02:00", "100"])

# 2. grade_boundaries.csv
# Component 41 Max 100: A: 62, B: 51, C: 41, D: 31, E: 21
gb_data = [
    ["9702", "2024", "Winter", "4", "1", "A", "62"],
    ["9702", "2024", "Winter", "4", "1", "B", "51"],
    ["9702", "2024", "Winter", "4", "1", "C", "41"],
    ["9702", "2024", "Winter", "4", "1", "D", "31"],
    ["9702", "2024", "Winter", "4", "1", "E", "21"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Winter", "4", "1", "NULL", "NULL", "Candidates found the gravitation and thermal physics questions accessible. Some difficulty seen in the field potential gradient explanation and specific details of pair annihilation in PET."])

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Winter", "4", "1", "1", "a", "2", "State Newton's law of gravitation.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "1", "1", "a", "1", "force proportional to product of masses", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "1", "1", "a", "2", "force inversely proportional to square of separation", "1", "B"])

# Q2
q_rows.append(["9702", "2024", "Winter", "4", "1", "2", "a", "2", "Define specific heat capacity.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "1", "2", "a", "1", "thermal energy per unit mass", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "1", "2", "a", "2", "energy per unit change in temperature", "1", "B"])
q_rows.append(["9702", "2024", "Winter", "4", "1", "2", "b", "NULL", "Temperature-time blocks in Fig. 2.1.", "images/9702_w24_41_qp_fig2_1.png"])

# Q4
q_rows.append(["9702", "2024", "Winter", "4", "1", "4", "a", "2", "Define simple harmonic motion (SHM).", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "1", "4", "a", "1", "acceleration proportional to displacement", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "1", "4", "a", "2", "acceleration opposite to displacement", "1", "B"])

# Q6
q_rows.append(["9702", "2024", "Winter", "4", "1", "6", "c", "NULL", "Input VIN square wave in Fig. 6.2 and VOUT in Fig. 6.3.", "images/9702_w24_41_qp_fig6_3.png"])

# Q10
q_rows.append(["9702", "2024", "Winter", "4", "1", "10", "c", "NULL", "Hubble Law v-d template in Fig. 10.1.", "images/9702_w24_41_qp_fig10_1.png"])

for r in q_rows: append_row('data/questions.csv', r)
for r in m_rows: append_row('data/markpoints.csv', r)

print("Ingested Questions and Markpoints for w24 41.")

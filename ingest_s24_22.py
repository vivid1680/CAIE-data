import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Summer", "2", "2", "01:15", "60"])

# 2. grade_boundaries.csv
# Component 22 Max 60: A: 46, B: 39, C: 31, D: 24, E: 16
gb_data = [
    ["9702", "2024", "Summer", "2", "2", "A", "46"],
    ["9702", "2024", "Summer", "2", "2", "B", "39"],
    ["9702", "2024", "Summer", "2", "2", "C", "31"],
    ["9702", "2024", "Summer", "2", "2", "D", "24"],
    ["9702", "2024", "Summer", "2", "2", "E", "16"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
ec_data = [
    ["9702", "2024", "Summer", "2", "2", "NULL", "NULL", "Candidates performed consistently well in structured calculations, particularly in electricity and mechanics. Descriptive questions involving particle physics were answered with good technical vocabulary."],
    ["9702", "2024", "Summer", "2", "2", "5", "b(ii)", "Successful responses correctly identified the resistance of the thermistor as 25 Ohm from the graph."],
    ["9702", "2024", "Summer", "2", "2", "6", "a", "Fundamental particles are those which cannot be subdivided into smaller particles."],
    ["9702", "2024", "Summer", "2", "2", "6", "b(ii)", "Mesons consist of a quark and antiquark pair."]
]
for row in ec_data:
    append_row('data/examiner_comments.csv', row)

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Summer", "2", "2", "1", "a", "1", "Circle all scalar quantities in the list: acceleration, charge, displacement, momentum, weight.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "1", "a", "1", "charge underlined (and no others)", "1", "B"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b", "NULL", "A square solar panel with sides of length 1300 mm is shown in Fig. 1.1.", "images/9702_s24_22_qp_fig1_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b(i)", "3", "Solar radiation power 750 W. Determine intensity.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b(i)", "1", "I = P / A", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b(i)", "2", "substitution with area conversion", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b(i)", "3", "440 W m^-2", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b(ii)", "2", "Uncertainty in length 5 mm, in power 3%. Calculate percentage uncertainty in intensity.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b(ii)", "1", "3 + 2 * (5/1300) * 100", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "1", "b(ii)", "2", "4%", "1", "A"])

# Q2
q_rows.append(["9702", "2024", "Summer", "2", "2", "2", "a", "NULL", "A skydiver jumps from aircraft. Velocity-time graph is shown in Fig. 2.1.", "images/9702_s24_22_qp_fig2_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "2", "a(i)", "1", "State terminal velocity.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "2", "a(i)", "1", "39 m s^-1", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "2", "a(ii)", "2", "Determine acceleration at 18 s.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "2", "a(ii)", "1", "tangent gradient", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "2", "a(ii)", "2", "1.0 m s^-2", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "2", "b", "3", "Mass 68 kg. Parachute opens and average upward force 1800 N. Determine acceleration.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "2", "b", "1", "Net Force = mg - F_up", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "2", "b", "2", "17 m s^-2", "1", "A"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "2", "b", "3", "upwards", "1", "B"])

# Q3
q_rows.append(["9702", "2024", "Summer", "2", "2", "3", "a", "2", "Average current 3.3 * 10^4 A for 2.6 * 10^-5 s. Calculate charge.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "a", "1", "Q = It", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "a", "2", "0.86 C", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "3", "b", "2", "Potential 3.0 * 10^7 V. Calculate power GW.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "b", "1", "P = IV", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "b", "2", "990 GW", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "3", "c", "NULL", "Copper building strip shown in Fig. 3.1.", "images/9702_s24_22_qp_fig3_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "3", "c(i)", "3", "Resistance 9.6 mOhm, resistivity 1.7 * 10^-8, length 95 m. Determine radius.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "c(i)", "1", "R = rho L / A", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "c(i)", "2", "A = pi r^2", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "c(i)", "3", "2.3 * 10^-4 m", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "3", "d", "NULL", "Pressure applied as shown in Fig. 3.2.", "images/9702_s24_22_qp_fig3_2.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "3", "d", "3", "Pressure 1.9 * 10^6 Pa. Young modulus 1.3 * 10^11 Pa. Width 0.12 m. Calculate compression x.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "d", "1", "E = stress / strain", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "d", "2", "substitutions", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "3", "d", "3", "1.8 * 10^-6 m", "1", "A"])

# Q4
q_rows.append(["9702", "2024", "Summer", "2", "2", "4", "a", "NULL", "Pinball machine spring 8.0 cm compressed as shown in Fig. 4.1.", "images/9702_s24_22_qp_fig4_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "4", "a", "2", "Spring constant 29 N m^-1. Calculate elastic energy.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "a", "1", "E = 1/2 k x^2", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "a", "2", "0.093 J", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(i)", "3", "Ball mass 45 g launched angle 15 degrees. Determine gain in GPE.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(i)", "1", "GPE = mgh", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(i)", "2", "h = L sin theta", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(i)", "3", "0.0091 J", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(ii)", "3", "Calculate launch speed.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(ii)", "1", "EK = EE - delta GPE", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(ii)", "2", "EK = 1/2 m v^2", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "b(ii)", "3", "1.9 m s^-1", "1", "A"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "4", "c", "NULL", "Ball launched as shown in Fig. 4.2.", "images/9702_s24_22_qp_fig4_2.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "4", "c(i)", "3", "Force 1.7 N at 2.0 cm. Calculate distance d from hinge.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "c(i)", "1", "F * x = mg * d", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "c(i)", "2", "moment equation", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "4", "c(i)", "3", "0.077 m", "1", "A"])

# Q5
q_rows.append(["9702", "2024", "Summer", "2", "2", "5", "a", "1", "State Kirchhoff's second law.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "5", "a", "1", "sum of emf = sum of pd in closed loop", "1", "B"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "5", "b", "NULL", "Circuit and thermistor graph shown in Fig. 5.1 and 5.2.", "images/9702_s24_22_qp_fig5_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "5", "b", "NULL", "Thermistor characteristic.", "images/9702_s24_22_qp_fig5_2.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "5", "b(i)", "2", "9.0 V supply. PD across X is 4.0 V at 11 mA. Calculate resistance of X.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "5", "b(i)", "1", "R = V / I", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "5", "b(i)", "2", "450 Ohm", "1", "A"])

# Q6
q_rows.append(["9702", "2024", "Summer", "2", "2", "6", "a", "NULL", "Semicircular screen shown in Fig. 6.1.", "images/9702_s24_22_qp_fig6_1.png"])
q_rows.append(["9702", "2024", "Summer", "2", "2", "6", "a", "3", "Wavelength 520 nm, slit separation 3.8 microns. Calculate number of bright fringes.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "6", "a", "1", "n lambda = d sin theta", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "6", "a", "2", "n = 7.3 for 90 degrees", "1", "C"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "6", "a", "3", "15 fringes", "1", "A"])

# Q7
q_rows.append(["9702", "2024", "Summer", "2", "2", "7", "a", "1", "Identify category (category/hadron).", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "7", "a", "1", "meson or hadron", "1", "B"])

q_rows.append(["9702", "2024", "Summer", "2", "2", "7", "b", "2", "Identify second quarks in Q and R from Table 7.1.", "NULL"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "7", "b", "1", "Q: anti-up / anti-charm", "1", "B"])
m_rows.append(["9702", "2024", "Summer", "2", "2", "7", "b", "2", "R: up / charm", "1", "B"])

# Write to CSV
for row in q_rows:
    append_row('data/questions.csv', row)
for row in m_rows:
    append_row('data/markpoints.csv', row)

print(f"Ingested {len(q_rows)} Questions and {len(m_rows)} Markpoints for s24 22.")

import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
append_row('data/papers.csv', ["9702", "2024", "Summer", "4", "2", "02:00", "100"])

# 2. grade_boundaries.csv
# Component 42 Max 100: A: 64, B: 52, C: 42, D: 31, E: 19
gb_data = [
    ["9702", "2024", "Summer", "4", "2", "A", "64"],
    ["9702", "2024", "Summer", "4", "2", "B", "52"],
    ["9702", "2024", "Summer", "4", "2", "C", "42"],
    ["9702", "2024", "Summer", "4", "2", "D", "31"],
    ["9702", "2024", "Summer", "4", "2", "E", "19"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
ec_data = [
    ["9702", "2024", "Summer", "4", "2", "NULL", "NULL", "Candidates showed a strong grasp of astrophysics and nuclear physics. High marks were awarded for correct use of standard equations."],
    ["9702", "2024", "Summer", "4", "2", "10", "b(ii)", "The intensity reflection coefficient for ultrasound between water and glass was calculated as 0.61 using the acoustic impedance values."]
]
for row in ec_data:
    append_row('data/examiner_comments.csv', row)

# 4. questions.csv & markpoints.csv
q_items = []
m_items = []

# Q1
q_items.append(["9702", "2024", "Summer", "4", "2", "1", "a", "1", "Define radian.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "a", "1", "angle when arc = radius", "1", "B"])

q_items.append(["9702", "2024", "Summer", "4", "2", "1", "b", "NULL", "Metal disc spins as shown in Fig. 1.1.", "images/9702_s24_42_qp_fig1_1.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "1", "b(i)", "1", "Draw arrow V for velocity of clay.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "b(i)", "1", "arrow V pointing NE", "1", "B"])
q_items.append(["9702", "2024", "Summer", "4", "2", "1", "b(ii)", "1", "Draw arrow A for acceleration.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "b(ii)", "1", "arrow A pointing NW", "1", "B"])

q_items.append(["9702", "2024", "Summer", "4", "2", "1", "c", "NULL", "Disc radius 9.3 cm. Clay speed 0.68 m s^-1.", "NULL"])
q_items.append(["9702", "2024", "Summer", "4", "2", "1", "c(i)", "2", "Determine angular speed Omega.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "c(i)", "1", "v = r w", "1", "C"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "c(i)", "2", "8.4 rad s^-1", "1", "A"])

q_items.append(["9702", "2024", "Summer", "4", "2", "1", "d", "NULL", "Second clay attached as shown in Fig. 1.2.", "images/9702_s24_42_qp_fig1_2.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "1", "d", "3", "Compare angular speed, linear speed, and acceleration for second piece.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "d", "1", "angular speed: same", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "d", "2", "linear speed: less", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "1", "d", "3", "acceleration: less", "1", "B"])

# Q2
q_items.append(["9702", "2024", "Summer", "4", "2", "2", "a", "1", "State what is meant by thermal equilibrium.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "2", "a", "1", "no net transfer of energy", "1", "B"])

q_items.append(["9702", "2024", "Summer", "4", "2", "2", "b", "NULL", "Two cylinders shown in Fig. 2.1.", "images/9702_s24_42_qp_fig2_1.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "2", "b(i)", "2", "Cylinder X: 0.740 mol, 0.0260 m^3, 1.20 * 10^5 Pa. Determine temperature.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "2", "b(i)", "1", "pV = nRT substitution", "1", "M1"])
m_items.append(["9702", "2024", "Summer", "4", "2", "2", "b(i)", "2", "234 degrees C", "1", "A1"])

# Q4
q_items.append(["9702", "2024", "Summer", "4", "2", "4", "a", "NULL", "Oscillating block and graph shown in Fig. 4.1 and 4.2.", "images/9702_s24_42_qp_fig4_1.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "4", "a", "NULL", "Acceleration-displacement graph.", "images/9702_s24_42_qp_fig4_2.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "4", "a", "2", "Explain how Fig. 4.2 shows SHM.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "4", "a", "1", "straight line through origin (a proportional to x)", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "4", "a", "2", "negative gradient (opposite directions)", "1", "B"])

# Q5
q_items.append(["9702", "2024", "Summer", "4", "2", "5", "a", "2", "Define electric potential.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "5", "a", "1", "work done per unit charge", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "5", "a", "2", "from infinity to the point", "1", "B"])

q_items.append(["9702", "2024", "Summer", "4", "2", "5", "b", "NULL", "Two spheres and graph in Fig. 5.1 and 5.2.", "images/9702_s24_42_qp_fig5_1.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "5", "b", "NULL", "Potential variation graph.", "images/9702_s24_42_qp_fig5_2.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "5", "b", "3", "State three conclusions about the spheres from Fig. 5.2.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "5", "b", "1", "Radius X = 0.30 m, Radius Y = 0.10 m", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "5", "b", "2", "Both charges are positive", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "5", "b", "3", "Charge magnitudes are equal", "1", "B"])

# Q6
q_items.append(["9702", "2024", "Summer", "4", "2", "6", "a", "NULL", "Capacitor circuit shown in Fig. 6.1.", "images/9702_s24_42_qp_fig6_1.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "6", "a", "3", "Derive expression for total capacitance in series.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "6", "a", "1", "equal charge Q", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "6", "a", "2", "VX + VY = V", "1", "M1"])
m_items.append(["9702", "2024", "Summer", "4", "2", "6", "a", "3", "final derivation", "1", "A"])

q_items.append(["9702", "2024", "Summer", "4", "2", "6", "b(iii)", "2", "Sketch energy stored variation with CQ graph template in Fig. 6.2.", "images/9702_s24_42_qp_fig6_2.png"])
m_items.append(["9702", "2024", "Summer", "4", "2", "6", "b(iii)", "1", "positive gradient starts at 2.5", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "6", "b(iii)", "2", "passes through (400, 7.5)", "1", "B"])

# Q7
q_items.append(["9702", "2024", "Summer", "4", "2", "7", "a", "2", "State Faraday's law of electromagnetic induction.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "7", "a", "1", "emf proportional to rate of change", "1", "M1"])
m_items.append(["9702", "2024", "Summer", "4", "2", "7", "a", "2", "of magnetic flux linkage", "1", "A1"])

q_items.append(["9702", "2024", "Summer", "4", "2", "7", "b", "NULL", "Coil in field shown in Fig. 7.1.", "images/9702_s24_42_qp_fig7_1.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "7", "b", "NULL", "B-t graph variation in Fig. 7.2.", "images/9702_s24_42_qp_fig7_2.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "7", "b", "NULL", "Induced emf variation template in Fig. 7.3.", "images/9702_s24_42_qp_fig7_3.png"])

# Q8
q_items.append(["9702", "2024", "Summer", "4", "2", "8", "a", "NULL", "Hydrogen emission spectrum in star star shown in Fig. 8.1.", "images/9702_s24_42_qp_fig8_1.png"])
q_items.append(["9702", "2024", "Summer", "4", "2", "8", "a(i)", "2", "Explain why observed lines differ.", "NULL"])
m_items.append(["9702", "2024", "Summer", "4", "2", "8", "a(i)", "1", "movement causes redshift", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "8", "a(i)", "2", "observed frequency lower", "1", "B"])

# Q9
q_items.append(["9702", "2024", "Summer", "4", "2", "9", "c(i)", "2", "Sketch binding energy per nucleon variation with A graph template in Fig. 9.1.", "images/9702_s24_42_qp_fig9_1.png"])
m_items.append(["9702", "2024", "Summer", "4", "2", "9", "c(i)", "1", "rising to peak left of 90", "1", "B"])
m_items.append(["9702", "2024", "Summer", "4", "2", "9", "c(i)", "2", "steep positive then shallow negative", "1", "B"])

# Write to CSV
for row in q_items:
    append_row('data/questions.csv', row)
for row in m_items:
    append_row('data/markpoints.csv', row)

print(f"Ingested Questions and Markpoints for s24 42.")

import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
# subject_code,year,session,paper_number,variant,duration,total_marks
append_row('data/papers.csv', ["9702", "2024", "Winter", "2", "2", "01:15", "60"])

# 2. grade_boundaries.csv
# subject_code,year,session,paper_number,variant,grade,min_mark
gb_data = [
    ["9702", "2024", "Winter", "2", "2", "A", "44"],
    ["9702", "2024", "Winter", "2", "2", "B", "37"],
    ["9702", "2024", "Winter", "2", "2", "C", "30"],
    ["9702", "2024", "Winter", "2", "2", "D", "25"],
    ["9702", "2024", "Winter", "2", "2", "E", "18"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
# subject_code,year,session,paper_number,variant,question_number,label,comment_text
ec_data = [
    ["9702", "2024", "Winter", "2", "2", "NULL", "NULL", "Candidates generally showed a solid understanding of core principles. Performance was high in calculations involving energy and electricity, though explanations regarding fundamental particles required more precision."],
    ["9702", "2024", "Winter", "2", "2", "6", "a", "A fundamental particle cannot be subdivided into smaller particles."],
    ["9702", "2024", "Winter", "2", "2", "6", "b(i)", "Mesons consist of one quark and one antiquark."],
    ["9702", "2024", "Winter", "2", "2", "6", "c(ii)", "Nucleon number is unchanged as emitted particles have a nucleon number of zero."]
]
for row in ec_data:
    append_row('data/examiner_comments.csv', row)

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Winter", "2", "2", "1", "a", "1", "State what is meant by a vector quantity.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "1", "a", "1", "quantity with magnitude and direction", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b", "NULL", "A sphere falls vertically through a liquid that has density 830 kg m^-3. The sphere has radius r and constant velocity v, as shown in Fig. 1.1.", "images/9702_w24_22_qp_fig1_1.png"])
q_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(i)", "3", "The drag force D acting on the sphere is given by D = 6 pi r eta v. Determine the SI base units of eta.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(i)", "1", "SI base units of D: kg m s^-2", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(i)", "2", "SI base units of r, v", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(i)", "3", "kg m^-1 s^-1", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(ii)", "1", "State an equation showing relationship between magnitudes of weight W, drag force D and upthrust U.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(ii)", "1", "W = U + D", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(iii)", "2", "Volume is 4.6 cm^3. D is 0.32 N. Calculate weight of sphere.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(iii)", "1", "U = rho g V", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "1", "b(iii)", "2", "0.36 N", "1", "A"])

# Q2
q_rows.append(["9702", "2024", "Winter", "2", "2", "2", "a", "1", "Define momentum.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "a", "1", "product of mass and velocity", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "2", "b", "2", "Child on scooter, mass 16 kg. Accelerates from rest for 1.1 s to speed 0.60 m s^-1. Determine average resultant force.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "b", "1", "F = m delta v / delta t", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "b", "2", "8.7 N", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "2", "c", "2", "Travels down slope shown in Fig. 2.1. Acceleration 0.85 m s^-2 for 3.7 s from speed 0.60 m s^-1. Calculate distance x.", "images/9702_w24_22_qp_fig2_1.png"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "c", "1", "x = ut + 1/2 at^2", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "c", "2", "8.0 m", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "2", "d(i)", "2", "Braking force to maintain constant velocity from B to C (18 m) as shown in Fig. 2.2. Work done 250 J. Determine braking force.", "images/9702_w24_22_qp_fig2_2.png"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "d(i)", "1", "F = W / s", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "d(i)", "2", "14 N", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "2", "d(ii)", "3", "On Fig. 2.3, sketch variation of kinetic energy with distance from A to C.", "images/9702_w24_22_qp_fig2_3.png"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "d(ii)", "1", "starting at distance 0 with non-zero KE", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "d(ii)", "2", "straight line from 0 to x with positive gradient", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "2", "d(ii)", "3", "straight horizontal line from x to x+18", "1", "B"])

# Q3
q_rows.append(["9702", "2024", "Winter", "2", "2", "3", "a(i)", "2", "Stress vs strain in Fig. 3.1. Determine Young modulus.", "images/9702_w24_22_qp_fig3_1.png"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "a(i)", "1", "E = stress / strain", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "a(i)", "2", "2.4 * 10^10 Pa", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "3", "a(ii)", "1", "On Fig. 3.1, draw cross to show limit of proportionality Q.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "a(ii)", "1", "cross at (1.0%, 24 * 10^7 Pa)", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "3", "b", "2", "State conditions for equilibrium.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "b", "1", "resultant force is zero", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "b", "2", "resultant torque is zero", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(i)", "3", "Shelf AB horizontally as shown in Fig. 3.2. Weight 33 N. Cup 1.5 N at 0.12 m from B. Determine tension T.", "images/9702_w24_22_qp_fig3_2.png"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(i)", "1", "individual moments", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(i)", "2", "sum of moments equation", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(i)", "3", "46 N", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(ii)", "2", "Stress is 1.5 * 10^7 Pa. Determine radius.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(ii)", "1", "sigma = F / A", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(ii)", "2", "9.9 * 10^-4 m", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(iii)", "2", "Stress doubles. State and explain behavior using Fig. 3.1.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(iii)", "1", "elastic limit not reached", "1", "M"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "3", "c(iii)", "2", "behaves elastically", "1", "A"])

# Q4
q_rows.append(["9702", "2024", "Winter", "2", "2", "4", "a", "2", "Compare oscillations of transverse and longitudinal waves.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "a", "1", "longitudinal: parallel to energy transfer", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "a", "2", "transverse: perpendicular to energy transfer", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(i)", "1", "Stationary wave in Fig. 4.1. Mark A at antinode.", "images/9702_w24_22_qp_fig4_1.png"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(i)", "1", "A at open end", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(ii)", "3", "Distance 4.5 * 10^-2 m. Speed 340 m s^-1. Determine frequency.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(ii)", "1", "f = v / lambda", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(ii)", "2", "lambda = 4 * distance", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(ii)", "3", "1900 Hz", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(iii)", "2", "Piston moved left. Frequency changed to form same number of antinodes. Explain change to frequency.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(iii)", "1", "wavelength longer", "1", "M"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "4", "b(iii)", "2", "frequency lower", "1", "A"])

# Q5
q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "a", "1", "Define potential difference.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "a", "1", "energy transferred per unit charge", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b", "NULL", "Power supply 230 V. Current 7.0 A. Circuit shown in Fig. 5.1.", "images/9702_w24_22_qp_fig5_1.png"])
q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(i)", "1", "Identify component X.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(i)", "1", "heater", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(ii)", "1", "Show pd across 0.86 Ohm is 6.0 V.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(ii)", "1", "V = 7.0 * 0.86 = 6.0 V", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(iii)", "2", "Determine current I1.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(iii)", "1", "I = V/R", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(iii)", "2", "5.7 A", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(iv)", "2", "Calculate pd across component X.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(iv)", "1", "Kirchhoff voltage law", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(iv)", "2", "210 V", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(v)", "2", "Calculate power in X.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(v)", "1", "P = IV", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(v)", "2", "1200 W", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(vi)", "2", "Determine percentage efficiency.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(vi)", "1", "useful power / total power", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(vi)", "2", "75% or 74%", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(vii)", "1", "170 Ohm removed. State if current in supply increases/decreases.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "5", "b(vii)", "1", "decreases", "1", "A"])

# Q6
q_rows.append(["9702", "2024", "Winter", "2", "2", "6", "a", "3", "Compare alpha with beta+ in terms of mass and charge.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "a", "1", "mass of alpha much greater", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "a", "2", "both positively charged", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "a", "3", "charge on alpha is twice", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "6", "b", "NULL", "P undergoes alpha-decay to Q, then Q decays to R. Fig. 6.1 shows proton/nucleon numbers.", "images/9702_w24_22_qp_fig6_1.png"])
q_rows.append(["9702", "2024", "Winter", "2", "2", "6", "b(i)", "1", "On Fig. 6.1, draw cross for Q.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "b(i)", "1", "cross at (82, 212) labelled Q", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "6", "b(ii)", "2", "State names of particles as Q decays to R.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "b(ii)", "1", "beta-minus / electron", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "b(ii)", "2", "antineutrino", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c", "NULL", "P traveling at constant velocity. After decay Q at 68 degrees. Alpha at theta as shown in Fig. 6.2.", "images/9702_w24_22_qp_fig6_2.png"])
q_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c(i)", "3", "Determine theta.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c(i)", "1", "conservation of momentum component", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c(i)", "2", "equation substitution", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c(i)", "3", "25 degrees", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c(ii)", "2", "Calculate kinetic energy of alpha.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c(ii)", "1", "E = 1/2 m v^2", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "2", "2", "6", "c(ii)", "2", "7.5 * 10^-13 J", "1", "A"])

# Write to questions.csv
for row in q_rows:
    append_row('data/questions.csv', row)

# Write to markpoints.csv
for row in m_rows:
    append_row('data/markpoints.csv', row)

print(f"Ingested {len(q_rows)} Questions and {len(m_rows)} Markpoints for w24 22.")

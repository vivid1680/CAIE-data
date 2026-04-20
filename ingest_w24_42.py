import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
# subject_code,year,session,paper_number,variant,duration,total_marks
append_row('data/papers.csv', ["9702", "2024", "Winter", "4", "2", "02:00", "100"])

# 2. grade_boundaries.csv
# subject_code,year,session,paper_number,variant,grade,min_mark
gb_data = [
    ["9702", "2024", "Winter", "4", "2", "A", "70"],
    ["9702", "2024", "Winter", "4", "2", "B", "63"],
    ["9702", "2024", "Winter", "4", "2", "C", "51"],
    ["9702", "2024", "Winter", "4", "2", "D", "39"],
    ["9702", "2024", "Winter", "4", "2", "E", "26"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
# subject_code,year,session,paper_number,variant,question_number,label,comment_text
ec_data = [
    ["9702", "2024", "Winter", "4", "2", "NULL", "NULL", "Candidates showed a strong grasp of astrophysics and nuclear physics. High marks were awarded for correct use of standard equations."],
    ["9702", "2024", "Winter", "4", "2", "9", "c(ii)", "Intensity ratio for ultrasound was calculated as 0.41 using the reflection coefficient formula, resulting in a transmitted fraction of 59%."],
    ["9702", "2024", "Winter", "4", "2", "10", "a(i)", "Stefan-Boltzmann law was applied to find the stellar radius, resulting in 6.96 * 10^8 m."]
]
for row in ec_data:
    append_row('data/examiner_comments.csv', row)

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "Winter", "4", "2", "1", "NULL", "NULL", "A metal wheel consists of an axle A, eight spokes and a rim, as shown in Fig. 1.1.", "images/9702_w24_42_qp_fig1_1.png"])
q_rows.append(["9702", "2024", "Winter", "4", "2", "1", "a(i)", "2", "Determine the speed of point X.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "a(i)", "1", "v = r w", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "a(i)", "2", "120 m s^-1", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "1", "a(ii)", "2", "Determine centripetal acceleration.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "a(ii)", "1", "a = r w^2", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "a(ii)", "2", "1.7 * 10^4 m s^-2", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(i)", "2", "State Lenz's law.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(i)", "1", "direction of induced e.m.f. opposes change", "1", "M"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(i)", "2", "produce effects that oppose it", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(ii)", "1", "Show time for one revolution is 45 ms.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(ii)", "1", "T = 2 pi / w = 0.045 s", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(iii)", "3", "Calculate magnetic flux cut by spoke AX.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(iii)", "1", "Phi = B A", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(iii)", "2", "A = pi r^2", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "1", "b(iii)", "3", "0.41 Wb", "1", "A"])

# Q2
q_rows.append(["9702", "2024", "Winter", "4", "2", "2", "a", "1", "Define gravitational field.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "a", "1", "force per unit mass", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "2", "b(i)", "2", "Probe distance 1.47 * 10^11 m. Calculate g.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "b(i)", "1", "g = GM/x^2", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "b(i)", "2", "6.14 * 10^-3 N kg^-1", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "2", "b(ii)", "2", "Determine gravitational potential energy.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "b(ii)", "1", "EP = -GMm/x", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "b(ii)", "2", "-2.37 * 10^9 J", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "2", "c(i)", "3", "Show g and F relation.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "c(i)", "1", "F = L / 4 pi x^2", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "c(i)", "2", "x^2 = GM/g", "1", "M"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "c(i)", "3", "algebra leading to result", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "2", "c(ii)", "2", "Fig. 2.1 shows variation. Determine luminosity L.", "images/9702_w24_42_qp_fig2_1.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "c(ii)", "1", "read-off substitution", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "2", "c(ii)", "2", "3.8 * 10^26 W", "1", "A"])

# Q3
q_rows.append(["9702", "2024", "Winter", "4", "2", "3", "a", "2", "Define specific latent heat.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "a", "1", "energy per unit mass to cause change of state", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "a", "2", "at constant temperature", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "3", "b(i)", "2", "Liquid vaporises. Show work done is 1.7 kJ.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "b(i)", "1", "W = p delta V", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "b(i)", "2", "1.7 kJ", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "3", "b(ii)", "2", "Calculate thermal energy Q.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "b(ii)", "1", "delta U = Q + W", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "b(ii)", "2", "19.3 kJ", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "3", "c", "3", "Suggest and explain if LF less than LV.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "c", "1", "fusion involves smaller volume change", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "c", "2", "smaller change in internal energy", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "3", "c", "3", "negligible work done", "1", "B"])

# Q4
q_rows.append(["9702", "2024", "Winter", "4", "2", "4", "a", "3", "State three basic assumptions of kinetic theory.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "a", "1", "random motion", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "a", "2", "elastic collisions", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "a", "3", "no intermolecular forces", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "4", "b", "3", "Explain how molecular movement causes pressure.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "b", "1", "momentum change during collision with wall", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "b", "2", "force on wall by molecule", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "b", "3", "many molecules exert force across area", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "4", "c", "3", "Conclusions from Fig. 4.1 and 4.2.", "images/9702_w24_42_qp_fig4_1.png"])
q_rows.append(["9702", "2024", "Winter", "4", "2", "4", "c", "3", "Fig 4.2 data", "images/9702_w24_42_qp_fig4_2.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "c", "1", "both are ideal", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "c", "2", "mass comparison", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "4", "c", "3", "number of molecules comparison", "1", "B"])

# Q5
q_rows.append(["9702", "2024", "Winter", "4", "2", "5", "a", "1", "Draw arrow on Fig. 5.1 for resultant force.", "images/9702_w24_42_qp_fig5_1.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "5", "a", "1", "arrow left and down", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "5", "b(i)", "1", "State amplitude from Fig. 5.2.", "images/9702_w24_42_qp_fig5_2.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "5", "b(i)", "1", "0.016 m", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "5", "b(ii)", "2", "Determine angular frequency.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "5", "b(ii)", "1", "w = 2 pi / T", "1", "C"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "5", "b(ii)", "2", "16 rad s^-1", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "5", "c", "3", "Sketch kinetic energy in Fig. 5.3.", "images/9702_w24_42_qp_fig5_3.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "5", "c", "1", "dome starting/ending on x-axis", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "5", "c", "2", "max EK 4.7 * 10^-3 J", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "5", "c", "3", "correct domain", "1", "B"])

# Q6
q_rows.append(["9702", "2024", "Winter", "4", "2", "6", "a", "2", "State Coulomb's law.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "6", "a", "1", "force proportional to product of charges", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "6", "a", "2", "inversely proportional to square of separation", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "6", "b", "3", "Draw field lines on Fig. 6.1.", "images/9702_w24_42_qp_fig6_1.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "6", "b", "1", "radial lines", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "6", "b", "2", "equally spaced", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "6", "b", "3", "arrows away", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "6", "c(i)", "1", "Determine radius from Fig. 6.2.", "images/9702_w24_42_qp_fig6_2.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "6", "c(i)", "1", "3.2 cm", "1", "A"])

# Q7
q_rows.append(["9702", "2024", "Winter", "4", "2", "7", "a", "2", "Define capacitance.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "7", "a", "1", "charge / potential difference", "1", "M"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "7", "a", "2", "charge on one plate", "1", "A"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "7", "b(i)", "2", "Sketch charge vs p.d. in Fig. 7.1.", "images/9702_w24_42_qp_fig7_1.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "7", "b(i)", "1", "straight line", "1", "B"])

q_rows.append(["9702", "2024", "Winter", "4", "2", "7", "c(i)", "3", "Connected to Y in Fig. 7.2. Complete Table 7.1.", "images/9702_w24_42_qp_fig7_2.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "7", "c(i)", "1", "final pd V/4", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "7", "c(i)", "2", "total charge Q", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "7", "c(i)", "3", "correct division", "1", "B"])

# Q8
q_rows.append(["9702", "2024", "Winter", "4", "2", "8", "b(ii)", "3", "Sketch I vs t in Fig. 8.1.", "images/9702_w24_42_qp_fig8_1.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "8", "b(ii)", "1", "sinusoidal from origin", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "8", "b(ii)", "2", "2 cycles", "1", "B"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "8", "b(ii)", "3", "peak 3.5 A", "1", "B"])

# Q9
q_rows.append(["9702", "2024", "Winter", "4", "2", "9", "d(i)", "2", "Sketch p vs 1/lambda in Fig. 9.1.", "images/9702_w24_42_qp_fig9_1.png"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "9", "d(i)", "1", "straight line through origin", "1", "B"])

# Q10
q_rows.append(["9702", "2024", "Winter", "4", "2", "10", "a(i)", "1", "State meant by random.", "NULL"])
m_rows.append(["9702", "2024", "Winter", "4", "2", "10", "a(i)", "1", "cannot predict when/which nucleus decays", "1", "B"])

# Write to questions.csv
for row in q_rows:
    append_row('data/questions.csv', row)

# Write to markpoints.csv
for row in m_rows:
    append_row('data/markpoints.csv', row)

print(f"Ingested {len(q_rows)} Questions and {len(m_rows)} Markpoints for w24 42.")

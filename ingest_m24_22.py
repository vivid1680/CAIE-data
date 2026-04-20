import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
# subject_code,year,session,paper_number,variant,duration,total_marks
append_row('data/papers.csv', ["9702", "2024", "March", "2", "2", "01:15", "60"])

# 2. grade_boundaries.csv
# subject_code,year,session,paper_number,variant,grade,min_mark
gb_data = [
    ["9702", "2024", "March", "2", "2", "A", "47"],
    ["9702", "2024", "March", "2", "2", "B", "42"],
    ["9702", "2024", "March", "2", "2", "C", "37"],
    ["9702", "2024", "March", "2", "2", "D", "31"],
    ["9702", "2024", "March", "2", "2", "E", "24"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv (Mapping ER "Q6" to QP Q8 and ER "Q7" to QP Q7)
# subject_code,year,session,paper_number,variant,question_number,label,comment_text
ec_data = [
    ["9702", "2024", "March", "2", "2", "NULL", "NULL", "Candidates performed consistently well in structured calculations, particularly in electricity and mechanics. Descriptive questions involving particle physics and nuclear decay were answered with good technical vocabulary."],
    ["9702", "2024", "March", "2", "2", "8", "b(i)", "Knowledge that mesons consist of a quark-antiquark pair was necessary."],
    ["9702", "2024", "March", "2", "2", "8", "c(ii)", "Candidates correctly identified that the nucleon number remains the same, as the emitted particles have nucleon numbers of zero."],
    ["9702", "2024", "March", "2", "2", "7", "b", "This question involved calculating internal resistance r. Successful candidates used E = I(R+r) or E = V+Ir, correctly identifying E= 1.8V and I= 0.25A to find r= 1.2 Ω."]
]
for row in ec_data:
    append_row('data/examiner_comments.csv', row)

# 4. questions.csv & markpoints.csv
# subject_code,year,session,paper_number,variant,question_number,label,marks,text_statement,image_path
# markpoints: subject_code,year,session,paper_number,variant,question_number,label,point_number,description,marks,type

q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "March", "2", "2", "1", "a", "1", "Table 1.1 lists some SI quantities. Complete the table by indicating with a tick (✓) which rows are SI base quantities.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "1", "a", "1", "current and mass only ticked", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "1", "b", "2", "Use the definition of power to determine its SI base units.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "1", "b", "1", "work (done) / time", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "1", "b", "2", "kg m^2 s^-3", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "1", "c", "3", "A light meter is used to measure the intensity of light in a classroom. Daylight is incident normally on the sensor of the meter. The sensor has an area of 2.2 cm^2. The reading on the meter is 950 W m^-2. Calculate the power of the daylight incident on the sensor.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "1", "c", "1", "power = intensity * area", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "1", "c", "2", "= 950 * 2.2 * 10^-4", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "1", "c", "3", "0.21 W", "1", "A"])

# Q2
q_rows.append(["9702", "2024", "March", "2", "2", "2", "a", "1", "Define acceleration.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "a", "1", "rate of change of velocity", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "2", "b", "3", "An Olympic diver stands on a platform above a pool of water, as shown in Fig. 2.1. When the diver is on the platform his centre of gravity is a vertical height of 9.0 m above the surface of the water. The diver jumps from the platform with a velocity of 5.9 m s^-1 at an angle of 60° to the horizontal. Air resistance is negligible. When the diver hits the surface of the water, his centre of gravity is a vertical height of 1.2 m above the surface of the water. Calculate the speed of the diver at the instant he hits the surface of the water.", "images/9702_m24_22_qp_fig2_1.png"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "b", "1", "1/2 m(delta)v^2 = mg(delta)h", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "b", "2", "v^2 = 5.9^2 + 2 * 9.81 * 7.8", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "b", "3", "14 m s^-1", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "2", "c(i)", "2", "The diver in (b) enters the water and decelerates. Describe and explain the variation of the viscous drag force acting on the diver in the water as he moves downwards.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "c(i)", "1", "speed decreases", "1", "B"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "c(i)", "2", "viscous force / drag decreases", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "2", "c(ii)", "1", "The diver has a volume of 7.5 * 10^-2 m^3. The density of the water is 1.0 * 10^3 kg m^-3. Show that the upthrust acting on the diver when he is entirely underwater is 740 N.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "c(ii)", "1", "(F =) rho * g * V = 1000 * 9.81 * 7.5 * 10^-2 = 740 (N)", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "2", "c(iii)", "4", "At a particular instant when the diver is entirely underwater his horizontal velocity is zero. The viscous drag force acting on him at this instant is 950 N vertically upwards. The diver has mass 78 kg. Determine the magnitude and direction of the acceleration of the diver.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "c(iii)", "1", "resultant force = 740 + 950 - (78 * 9.81) = 925", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "c(iii)", "2", "acceleration = F / m = 925 / 78", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "c(iii)", "3", "12 m s^-2", "1", "A"])
m_rows.append(["9702", "2024", "March", "2", "2", "2", "c(iii)", "4", "vertically upwards", "1", "B"])

# Q3
q_rows.append(["9702", "2024", "March", "2", "2", "3", "NULL", "NULL", "A thin metal wire X, of diameter 1.2 * 10^-3 m, is used to suspend a model planet, as shown in Fig. 3.1.", "images/9702_m24_22_qp_fig3_1.png"])
q_rows.append(["9702", "2024", "March", "2", "2", "3", "a(i)", "3", "The variation with strain of the stress for wire X is shown in Fig. 3.2. The strain in X is 5.4 * 10^-3. Use Fig. 3.2 to calculate the force exerted on the wire by the model planet.", "images/9702_m24_22_qp_fig3_2.png"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "a(i)", "1", "stress = 0.72 * 10^9", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "a(i)", "2", "force = stress * Area = 0.72 * 10^9 * pi * (1.2 * 10^-3 / 2)^2", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "a(i)", "3", "810 N", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "3", "a(ii)", "3", "The elastic potential energy of X is 0.31 J. Calculate the original length of the wire before the model planet was attached.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "a(ii)", "1", "Ep = 1/2 Fx", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "a(ii)", "2", "x = 2Ep / F = 2 * 0.31 / 810 = 7.7 * 10^-4", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "a(ii)", "3", "L = x / strain = 7.7 * 10^-4 / 5.4 * 10^-3 = 0.14 m", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "3", "b", "2", "Wire X is replaced by a new wire, Y, with the same original length and diameter but double the Young modulus of X. Wire Y also obeys Hooke's law. On Fig. 3.2, draw a line representing the variation with strain of the stress for Y.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "b", "1", "straight line from origin with larger gradient than X", "1", "M"])
m_rows.append(["9702", "2024", "March", "2", "2", "3", "b", "2", "gradient is twice that of X", "1", "A"])

# Q4
q_rows.append(["9702", "2024", "March", "2", "2", "4", "a", "2", "A nucleus P undergoes alpha-decay to form nucleus Q. Complete the equation for this decay: 215/84 P -> .../... Q + .../... alpha", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "4", "a", "1", "4/2 alpha", "1", "B"])
m_rows.append(["9702", "2024", "March", "2", "2", "4", "a", "2", "211/82 Q", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "4", "b(i)", "2", "State the principle of conservation of momentum.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "4", "b(i)", "1", "total momentum is constant / before = after", "1", "M"])
m_rows.append(["9702", "2024", "March", "2", "2", "4", "b(i)", "2", "isolated system / no external force", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "4", "b(ii)", "2", "Before the decay, nucleus P has a speed of 3.2 * 10^5 m s^-1. After the decay, nucleus Q is stationary. Calculate the speed of the alpha particle after the decay.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "4", "b(ii)", "1", "4 * v = 215 * 3.2 * 10^5", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "4", "b(ii)", "2", "1.7 * 10^7 m s^-1", "1", "A"])

# Q5
q_rows.append(["9702", "2024", "March", "2", "2", "5", "a", "1", "By reference to the direction of propagation of energy, state what is meant by a transverse wave.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "5", "a", "1", "vibrations perpendicular to the direction of energy propagation", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "5", "b", "1", "A space telescope is designed to detect electromagnetic radiation with wavelengths in the range 12 um to 28 um. State the region of the electromagnetic spectrum for this radiation.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "5", "b", "1", "infrared", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "5", "c", "3", "A detector on another space telescope detects an electromagnetic wave. The signal from the detector is transmitted to Earth and displayed on an oscilloscope as shown in Fig. 5.1. The time-base setting on the oscilloscope is 5.0 * 10^-15 s cm^-1. Calculate the wavelength of the detected electromagnetic wave.", "images/9702_m24_22_qp_fig5_1.png"])
m_rows.append(["9702", "2024", "March", "2", "2", "5", "c", "1", "T = 6 * 5.0 * 10^-15 = 3.0 * 10^-14 s", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "5", "c", "2", "lambda = c * T", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "5", "c", "3", "9.0 * 10^-6 m", "1", "A"])

# Q6
q_rows.append(["9702", "2024", "March", "2", "2", "6", "a(i)", "3", "Coherent visible light... is illustrated in Fig. 6.1. There are seven bright fringes. Explain how the pattern of bright and dark interference fringes is formed.", "images/9702_m24_22_qp_fig6_1.png"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "a(i)", "1", "Light diffracts at the slits", "1", "B"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "a(i)", "2", "Light meets / superposes", "1", "B"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "a(i)", "3", "Phase diff 0 for bright / 180 for dark", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "6", "a(ii)", "3", "The distance between the centres of bright fringe X and bright fringe Y in the pattern is 10.2 mm. The slit spacing is 1.2 mm. The distance from the slits to the screen is 3.1 m. Calculate the wavelength of the light incident on the slits.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "a(ii)", "1", "lambda = ax / D", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "a(ii)", "2", "lambda = 1.2 * 10^-3 * (10.2 * 10^-3 / 6) / 3.1", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "a(ii)", "3", "6.6 * 10^-7 m", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "6", "a(iii)", "1", "The light is replaced by different visible light with a shorter wavelength. State how the new fringe separation will compare to the original fringe separation.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "a(iii)", "1", "smaller", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "6", "b(i)", "1", "A stationary wave is formed on a stretched string AB, as shown in Fig. 6.2. P, Q and R are points on the string. On Fig. 6.2, draw a cross (x) to show the position of a node.", "images/9702_m24_22_qp_fig6_2.png"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "b(i)", "1", "Cross at intersection of string and mean line", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "6", "b(ii)", "1", "State the phase difference between P and Q.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "b(ii)", "1", "0", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "6", "b(iii)", "1", "State the phase difference between P and R.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "6", "b(iii)", "1", "180", "1", "A"])

# Q7
q_rows.append(["9702", "2024", "March", "2", "2", "7", "a", "1", "Define electric potential difference.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "a", "1", "energy transferred per unit charge", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "7", "b", "3", "A cell of e.m.f. 1.8 V and internal resistance r is connected in parallel with a resistor of resistance 6.0 Ohm and a filament lamp, as shown in Fig. 7.1. The switch S is open. The ammeter reading is 0.25 A. Determine the internal resistance r of the cell.", "images/9702_m24_22_qp_fig7_1.png"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "b", "1", "V = 0.25 * 6 = 1.5", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "b", "2", "Ir = E - V = 1.8 - 1.5 = 0.3", "1", "C"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "b", "3", "r = 0.3 / 0.25 = 1.2 Ohm", "1", "A"])

q_rows.append(["9702", "2024", "March", "2", "2", "7", "c(i)", "1", "At time t1 switch S is closed. Fig. 7.2 shows the variation with time t of the ammeter reading I. State whether the e.m.f. of the cell after t1 is greater than, less than or the same as it was before t1.", "images/9702_m24_22_qp_fig7_2.png"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "c(i)", "1", "The same", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "7", "c(ii)", "3", "By considering the effect of the lamp on the total resistance of the circuit, explain the variation of the ammeter reading shown in Fig. 7.2.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "c(ii)", "1", "at t1 resistance decreases", "1", "B"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "c(ii)", "2", "temperature of lamp increases", "1", "B"])
m_rows.append(["9702", "2024", "March", "2", "2", "7", "c(ii)", "3", "resistance of lamp increases so current decreases", "1", "B"])

# Q8
q_rows.append(["9702", "2024", "March", "2", "2", "8", "a", "1", "State the name of the class (group) of fundamental particles that contains a neutrino.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "8", "a", "1", "lepton(s)", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "8", "b(i)", "1", "A hadron P has a charge of +1e. The hadron P is composed of a down antiquark and only one other quark. Identify a possible flavour for this other quark.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "8", "b(i)", "1", "up or top or charm", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "8", "b(ii)", "1", "State what type of hadron is P.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "8", "b(ii)", "1", "meson(s)", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "8", "c(i)", "1", "Nucleus Q undergoes radioactive decay to form nucleus R, emitting an antineutrino and another particle X, as shown in the decay equation: Q -> R + X + anti-nu. State what particle is represented by X.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "8", "c(i)", "1", "beta-minus / electron", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "8", "c(ii)", "1", "Compare the nucleon numbers of Q and R.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "8", "c(ii)", "1", "equal", "1", "B"])

q_rows.append(["9702", "2024", "March", "2", "2", "8", "c(iii)", "1", "Compare the charges of Q and R.", "NULL"])
m_rows.append(["9702", "2024", "March", "2", "2", "8", "c(iii)", "1", "R is greater than Q", "1", "B"])

# Write to questions.csv
for row in q_rows:
    append_row('data/questions.csv', row)

# Write to markpoints.csv
for row in m_rows:
    append_row('data/markpoints.csv', row)

print(f"Ingested {len(q_rows)} Questions and {len(m_rows)} Markpoints for m24 22.")

import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
# subject_code,year,session,paper_number,variant,duration,total_marks
append_row('data/papers.csv', ["9702", "2024", "March", "4", "2", "02:00", "100"])

# 2. grade_boundaries.csv
# subject_code,year,session,paper_number,variant,grade,min_mark
gb_data = [
    ["9702", "2024", "March", "4", "2", "A", "61"],
    ["9702", "2024", "March", "4", "2", "B", "52"],
    ["9702", "2024", "March", "4", "2", "C", "42"],
    ["9702", "2024", "March", "4", "2", "D", "32"],
    ["9702", "2024", "March", "4", "2", "E", "22"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
# subject_code,year,session,paper_number,variant,question_number,label,comment_text
ec_data = [
    ["9702", "2024", "March", "4", "2", "NULL", "NULL", "This paper presented rigorous challenges in fields such as thermal physics and astrophysics. The use of standard formulae was generally accurate, though candidates must ensure they define variables clearly."],
    ["9702", "2024", "March", "4", "2", "9", "c(ii)", "This calculation required the use of the reflection coefficient formula. Using the provided density and speed values, the intensity ratio was found to be 0.41. The transmitted fraction was then deduced as 59%."],
    ["9702", "2024", "March", "4", "2", "10", "a(i)", "Using the Stefan-Boltzmann law L = 4pi sigma r^2 T^4, candidates calculated the radius of the star. Given the luminosity and temperature, the radius was determined as 6.96 * 10^8 m."]
]
for row in ec_data:
    append_row('data/examiner_comments.csv', row)

# 4. questions.csv & markpoints.csv
q_rows = []
m_rows = []

# Q1
q_rows.append(["9702", "2024", "March", "4", "2", "1", "a", "2", "Explain why the gravitational potential near to a point mass is negative.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "a", "1", "potential is zero at infinity", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "a", "2", "work is done on a mass to move it away / to infinity", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "1", "b(i)", "2", "The variation with 1/r of phi is shown in Fig. 1.1. Show that the mass of the planet is 8.8 * 10^25 kg.", "images/9702_m24_42_qp_fig1_1.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(i)", "1", "M = gradient / G", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(i)", "2", "calculation leading to 8.8 * 10^25 kg", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "1", "b(ii)", "3", "The period of rotation of the planet is 0.72 Earth days. A satellite in orbit around the planet remains above the same point on the surface. Determine the radius R of the orbit.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(ii)", "1", "GMm/r^2 = mrw^2 or similar", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(ii)", "2", "R^3 = ...", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(ii)", "3", "8.3 * 10^7 m", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "1", "b(iii)", "3", "The speed of the satellite is 8400 m s^-1. Mass is 1200 kg. Determine the additional energy required to move the satellite to infinity.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(iii)", "1", "KE = 1/2 mv^2", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(iii)", "2", "PE = -GMm/r", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "1", "b(iii)", "3", "4.3 * 10^10 J", "1", "A"])

# Q2
q_rows.append(["9702", "2024", "March", "4", "2", "2", "a", "2", "By referring to both kinetic energy and potential energy, explain what is meant by the internal energy of an ideal gas.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "a", "1", "total kinetic energy of random motion of molecules", "1", "M"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "a", "2", "plus total potential energy (which is zero)", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "2", "b(i)", "2", "Sealed in a cylinder by a piston, as shown in Fig. 2.1. Initial volume 1.24 * 10^-4 m^3. Thermal energy supplied and volume increases by 5.20 * 10^-5 m^3. Pressure is 1.01 * 10^5 Pa. Calculate work done by gas.", "images/9702_m24_42_qp_fig2_1.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "b(i)", "1", "W = p delta V", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "b(i)", "2", "5.25 J", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "2", "b(ii)", "2", "Calculate the final thermodynamic temperature T of the gas.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "b(ii)", "1", "V1/T1 = V2/T2", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "b(ii)", "2", "416 K", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "2", "b(iii)", "2", "Mass is 16 g. Net transfer of 960 J. Calculate specific heat capacity c at this pressure.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "b(iii)", "1", "c = Q / (m delta T)", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "b(iii)", "2", "490 J kg^-1 K^-1", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "2", "c", "3", "Piston now fixed. Same temp change. Use first law of thermodynamics to compare c for this situation.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "c", "1", "no work done", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "c", "2", "same change in internal energy", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "2", "c", "3", "c is less", "1", "B"])

# Q3
q_rows.append(["9702", "2024", "March", "4", "2", "3", "NULL", "NULL", "A small object of mass 24 g rests on a platform. The platform is attached to an oscillator, as shown in Fig. 3.1.", "images/9702_m24_42_qp_fig3_1.png"])
q_rows.append(["9702", "2024", "March", "4", "2", "3", "a", "3", "Total energy 2.2 * 10^-4 J. Total distance in one oscillation 14 mm. Calculate angular frequency omega.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "3", "a", "1", "E = 1/2 m w^2 x0^2", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "3", "a", "2", "x0 = 14/4 = 3.5 mm", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "3", "a", "3", "39 rad s^-1", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "3", "b(i)", "2", "Calculate maximum amplitude so object does not lose contact.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "3", "b(i)", "1", "acceleration = 9.81", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "3", "b(i)", "2", "6.4 * 10^-3 m", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "3", "b(ii)", "2", "State and explain position where object first loses contact.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "3", "b(ii)", "1", "at top of oscillation", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "3", "b(ii)", "2", "downwards acceleration exceeds g", "1", "B"])

# Q4
q_rows.append(["9702", "2024", "March", "4", "2", "4", "a", "2", "Three capacitors connected as shown in Fig. 4.1. Determine total capacitance.", "images/9702_m24_42_qp_fig4_1.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "a", "1", "parallel = 30", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "a", "2", "18 uF", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "4", "b", "2", "45 uF capacitor. PD increases from 8.0 V to 9.6 V. Calculate increase in energy delta E.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "b", "1", "E = 1/2 CV^2", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "b", "2", "6.3 * 10^-4 J", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "4", "c(i)", "1", "Complete circuit in Fig. 4.2 by adding a smoothing capacitor.", "images/9702_m24_42_qp_fig4_2.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "c(i)", "1", "capacitor in parallel with load", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "4", "c(ii)", "3", "Variation in Fig. 4.3. Determine time constant.", "images/9702_m24_42_qp_fig4_3.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "c(ii)", "1", "two pairs of (t, V)", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "c(ii)", "2", "V = V0 exp(-t/tau)", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "c(ii)", "3", "36 ms", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "4", "d(i)", "1", "Mean power for full-wave rectified (max 16 W).", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "d(i)", "1", "8.0 W", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "4", "d(ii)", "1", "Mean power for half-wave rectified.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "4", "d(ii)", "1", "4.0 W", "1", "A"])

# Q5
q_rows.append(["9702", "2024", "March", "4", "2", "5", "a", "2", "State names of two quantities that vary during circular motion at constant speed.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "a", "1", "velocity", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "a", "2", "acceleration / force / displacement", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "5", "b(i)", "3", "Consider magnetic force. Show that B = 2 pi m / (q T).", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(i)", "1", "Bqv = mv^2/r", "1", "M"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(i)", "2", "v = 2 pi r / T", "1", "M"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(i)", "3", "B = 2 pi m / q T", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "5", "b(ii)", "2", "Alpha particle. T = 2.5 us. Calculate B.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(ii)", "1", "substitution", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(ii)", "2", "0.052 T", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "5", "b(iii)", "1", "Second alpha particle. Radius 2r. State and explain periods.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(iii)", "1", "same because T independent of r", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "5", "b(iv)", "2", "Speed 1.1 * 10^6 m s^-1. Calculate electric field strength E.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(iv)", "1", "qE = Bqv", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "5", "b(iv)", "2", "5.7 * 10^4 N C^-1", "1", "A"])

# Q6
q_rows.append(["9702", "2024", "March", "4", "2", "6", "a(i)", "1", "Coil C inside solenoid shown in Fig. 6.1. Move from X to Y. Sketch flux linkage in Fig. 6.2.", "images/9702_m24_42_qp_fig6_1.png"])
q_rows.append(["9702", "2024", "March", "4", "2", "6", "a(i)", "1", "Sketch Fig 6.2", "images/9702_m24_42_qp_fig6_2.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(i)", "1", "non-zero horizontal straight line", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "6", "a(ii)", "2", "Explain shape of line in (a)(i).", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(ii)", "1", "constant flux density inside", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(ii)", "2", "Phi = BAN and B, A, N constant", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "6", "a(iii)", "2", "Current varies as shown in Fig. 6.3. Calculate maximum flux linkage.", "images/9702_m24_42_qp_fig6_3.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(iii)", "1", "Phi = BAN", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(iii)", "2", "3.6 * 10^-4 Wb", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "6", "a(iv)", "3", "On Fig. 6.4, sketch induced emf E.", "images/9702_m24_42_qp_fig6_4.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(iv)", "1", "0 to t is zero", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(iv)", "2", "non-zero constant after t", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "a(iv)", "3", "opposite signs for t-2t and 2t-4t", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "6", "b", "3", "Metal spring shown in Fig. 6.5. Describe and explain change in distance between turns.", "images/9702_m24_42_qp_fig6_5.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "b", "1", "current creates magnetic field", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "b", "2", "adjacent turns interact", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "6", "b", "3", "attractive so distance decreases", "1", "B"])

# Q7
q_rows.append(["9702", "2024", "March", "4", "2", "7", "a", "2", "Photon energy 3.11 * 10^-19 J. Calculate momentum.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "a", "1", "p = E/c", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "a", "2", "1.04 * 10^-27 N s", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "7", "b(i)", "2", "Laser 350 mW, 640 nm. Determine number of photons in 1.0 s.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "b(i)", "1", "E = hc/lambda", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "b(i)", "2", "1.1 * 10^18", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "7", "b(ii)", "2", "Incident normally and absorbed. Show that F = P/c.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "b(ii)", "1", "F = p/t", "1", "M"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "b(ii)", "2", "p = E/c and t = E/P leading to P/c", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "7", "c(i)", "1", "Work function in Table 7.1. Explain term threshold wavelength.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "c(i)", "1", "maximum wavelength that causes emission", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "7", "c(ii)", "2", "Calculate value of character threshold wavelength for metals in Table 7.1.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "c(ii)", "1", "2.26 eV substitution", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "7", "c(ii)", "2", "5.50 * 10^-7 m", "1", "A"])

# Q8
q_rows.append(["9702", "2024", "March", "4", "2", "8", "a", "2", "State meant by binding energy of a nucleus.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "a", "1", "energy to separate nucleons", "1", "M"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "a", "2", "to infinity", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "8", "b(i)", "1", "U-235 absorbs neutron ... xenon-142 + strontium-90 + neutrons. Determine number of neutrons.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "b(i)", "1", "4", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "8", "b(ii)", "2", "Binding energy in Table 8.1. Calculate energy released from fission of one U-235.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "b(ii)", "1", "energy = product BE - reactant BE", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "b(ii)", "2", "190 MeV", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "8", "b(iii)", "1", "Suggest reason why xenon-142 is unstable.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "b(iii)", "1", "too many neutrons / ratio too high", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "8", "b(iv)", "3", "After 6.0 s, decayed/undecayed = 31. Calculate half-life.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "b(iv)", "1", "N/N0 = 1/32", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "b(iv)", "2", "5 half-lives", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "8", "b(iv)", "3", "1.2 s", "1", "A"])

# Q9
q_rows.append(["9702", "2024", "March", "4", "2", "9", "a(i)", "2", "84 kV PD. Calculate minimum wavelength of X-rays.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "a(i)", "1", "eV = hc/lambda", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "a(i)", "2", "1.5 * 10^-11 m", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "9", "a(ii)", "2", "Melting points in Table 9.1. Suggest why tungsten used.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "a(ii)", "1", "KE converted to thermal / X-rays absorbed", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "a(ii)", "2", "tungsten has higher melting point", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "9", "b", "3", "Soft tissue and bone in Fig. 9.1. Transmitted intensity 13%. Data in Table 9.2. Determine x.", "images/9702_m24_42_qp_fig9_1.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "b", "1", "I = I0 exp(-mu t)", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "b", "2", "0.13 = exp(-3.22x)", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "b", "3", "0.63 cm", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "9", "c(i)", "2", "Define specific acoustic impedance.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "c(i)", "1", "product of density and speed", "1", "M"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "c(i)", "2", "speed of ultrasound", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "9", "c(ii)", "2", "Calculate percentage of intensity of ultrasound transmitted at boundary.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "c(ii)", "1", "fraction transmitted = 1 - reflectance", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "c(ii)", "2", "59%", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "9", "c(iii)", "2", "Suggest two reasons why transmitted intensity is less.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "c(iii)", "1", "multiple boundaries / reflections", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "9", "c(iii)", "2", "attenuation in matter", "1", "B"])

# Q10
q_rows.append(["9702", "2024", "March", "4", "2", "10", "a(i)", "2", "Sun Temp 5780 K, Lum 3.85 * 10^26 W. Calculate radius of Sun.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "a(i)", "1", "L = 4 pi sigma r^2 T^4", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "a(i)", "2", "6.96 * 10^8 m", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "10", "a(ii)", "2", "Earth distance 1.50 * 10^11 m. Calculate radiant flux intensity F.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "a(ii)", "1", "F = L / 4 pi d^2", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "a(ii)", "2", "1.36 * 10^3 W m^-2", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "10", "a(iii)", "2", "Shown in Fig. 10.1. Another star same radius, lower temp. Sketch in Fig. 10.1.", "images/9702_m24_42_qp_fig10_1.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "a(iii)", "1", "peak at greater wavelength", "1", "B"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "a(iii)", "2", "lower peak intensity", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "10", "b(i)", "1", "Galaxy moving away. Sun spectrum in Fig. 10.2. Sketch emission spectrum for star in Corona Borealis in Fig. 10.3.", "images/9702_m24_42_qp_fig10_2.png"])
q_rows.append(["9702", "2024", "March", "4", "2", "10", "b(i)", "1", "Sketch in Fig 10.3", "images/9702_m24_42_qp_fig10_3.png"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "b(i)", "1", "5 lines shifted to longer wavelengths", "1", "B"])

q_rows.append(["9702", "2024", "March", "4", "2", "10", "b(ii)", "2", "Galaxy moving away at 21400 km s^-1. Calculate observed wavelength of lowest visible energy emission.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "b(ii)", "1", "delta lambda / lambda = v/c", "1", "C"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "b(ii)", "2", "703 nm", "1", "A"])

q_rows.append(["9702", "2024", "March", "4", "2", "10", "b(iii)", "1", "State whether temperature calculation is too high or too low.", "NULL"])
m_rows.append(["9702", "2024", "March", "4", "2", "10", "b(iii)", "1", "temperature too low", "1", "B"])

# Write to questions.csv
for row in q_rows:
    append_row('data/questions.csv', row)

# Write to markpoints.csv
for row in m_rows:
    append_row('data/markpoints.csv', row)

print(f"Ingested {len(q_rows)} Questions and {len(m_rows)} Markpoints for m24 42.")

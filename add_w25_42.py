import csv

# Metadata inserts
with open(r"data\papers.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "November", "4", "2"])

with open(r"data\grade_boundaries.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "November", "4", "2", "100", "57", "48", "39", "29", "19"])

ec_rows = [
    ["9702", "2025", "November", "4", "2", "NULL", "Performance on this paper indicated a strong grasp of circular motion and thermodynamics. Precision in sketching field lines and interpreting exponential decay graphs were the main discriminators for higher marks."],
    ["9702", "2025", "November", "4", "2", "1", "Using the bicycle speed of 17ms-1 and rear wheel radius of 0.46m candidates correctly calculated the angular speed as 37 rad s-1."],
    ["9702", "2025", "November", "4", "2", "6", "Candidates were required to show the minimum wavelength of X-rays was 21pm. Using eV=hc/lambda provided the necessary evidence."],
    ["9702", "2025", "November", "4", "2", "9", "Interpretation of photoelectric effect graphs yielded quantitative conclusions."],
    ["9702", "2025", "November", "4", "2", "10", "Comparing activities of isotopes X and Y required solving..."]
]

with open(r"data\examiner_comments.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ec_rows:
        writer.writerow(row)

# Q maps: (q_num, sub_q, max_mark, text, diagram_path)
qs = [
    (1, "a(i)", 1, "The Earth may be considered as a uniform sphere of radius 6.37x10^6 m. Cambridge is at a point on the Earth's surface that has a latitude of 52.2 degrees north. As the Earth spins on its axis, Cambridge moves in a circle... Show that the radius of the circle around which Cambridge moves is 3.90x10^6 m.\n[diagram]", "images/9702_w25_qp_42_fig1_1.png"),
    (1, "a(ii)", 3, "Calculate the speed at which Cambridge moves around the circle.", "NULL"),
    (1, "b(i)", 2, "A student of mass 58.6 kg stands on horizontal ground in Cambridge. Determine the magnitude of the resultant force that acts to cause the circular motion of the student.", "NULL"),
    (1, "b(ii)", 1, "On Fig 1.2, draw an arrow to show the direction of the resultant force that acts on the student.\n[diagram]", "images/9702_w25_qp_42_fig1_2.png"),
    (1, "b(iii)", 2, "On Fig 1.3, draw labelled arrows from the student to show the directions of the forces that act on the student to cause the resultant force in (b)(ii).\n[diagram]", "images/9702_w25_qp_42_fig1_3.png"),

    (2, "a", 2, "State Newton's law of gravitation.", "NULL"),
    (2, "b", 2, "One of the basic assumptions of the kinetic theory of gases is that there are no forces exerted between the molecules of the gas except during collisions. State two other basic assumptions of the kinetic theory of gases.", "NULL"),
    (2, "c(i)", 2, "Hydrogen gas consists of molecules that each have a mass of 3.34x10^-27 kg. A spherical balloon contains 0.0160 mol of hydrogen gas at a temperature of 282 K. Volume is 1.87x10^-4 m^3. Determine the pressure of the gas.", "NULL"),
    (2, "c(ii)", 2, "Estimate the average separation of the hydrogen molecules in the gas.", "NULL"),
    (2, "d(i)", 2, "Use your answer in (c)(ii) to calculate the average gravitational force between adjacent molecules in hydrogen gas.", "NULL"),
    (2, "d(ii)", 1, "By considering the weight of a molecule, suggest with a reason whether your answer in (d)(i) is consistent with the assumption of the kinetic theory of gases.", "NULL"),

    (3, "a", 2, "State what is meant by two objects being in thermal equilibrium.", "NULL"),
    (3, "b(i)", 1, "Fig 3.1 shows a type of thermometer called a constant volume gas thermometer... The value of delta h can be used to calculate the pressure. State the property of the liquid that is used to calculate the pressure.\n[diagram]", "images/9702_w25_qp_42_fig3_1.png"),
    (3, "b(ii)", 2, "State two disadvantages of using a constant volume gas thermometer to measure temperature.", "NULL"),
    (3, "b(iii)", 1, "Suggest one situation in which a constant volume gas thermometer would be an appropriate type of thermometer to choose for measuring temperature.", "NULL"),
    (3, "b(iv)", 3, "Level X aligns with 2.31 cm on the scale. At 0 C, level Y aligns with 8.69 cm. At temperature theta, level Y aligns with 7.83 cm on the scale. Determine a value for theta in C.", "NULL"),

    (4, "a", 2, "A cylinder contains a fixed mass of an ideal gas at pressure 2Y and volume 6X. The gas undergoes a sequence of changes from its initial state A, through B, C, and D back to A. Fig 4.1 shows the variation. Fig 4.2 shows the variation with time of internal energy. State the first law of thermodynamics.\n[diagram]", "images/9702_w25_qp_42_fig4_1.png"),
    (4, "b(i)", 1, "Use Fig 4.1 and Fig 4.2 to determine the general expression for the internal energy U of the gas when it has pressure p and volume V.", "NULL"),
    (4, "b(ii)", 2, "An ideal gas at thermodynamic temperature T contains N molecules. Use your answer in (b)(i) and the equation of state for an ideal gas to deduce an expression for U in terms of N and T. Identify any other symbols you use.", "NULL"),
    (4, "c(i)", 1, "Determine expressions, in terms of X and Y, for the work W done on the gas during change AB.", "NULL"),
    (4, "c(ii)", 1, "Determine expressions, in terms of X and Y, for the work W done on the gas during change CD.", "NULL"),
    (4, "d", 3, "Use your answers in (c) and the first law of thermodynamics to determine an expression, in terms of X and Y, for the net thermal energy Q supplied to the gas during one full cycle ABCDA. Explain your reasoning.", "NULL"),

    (5, "a(i)", 2, "A steel ball on the end of a thin string oscillates with small oscillations, as shown in Fig 5.1. The displacement of the centre of the ball from equilibrium is x. Fig 5.2 shows the variation with x of acceleration a. Explain how Fig 5.2 shows that the oscillations of the ball are simple harmonic.\n[diagram]", "images/9702_w25_qp_42_fig5_1.png"),
    (5, "a(ii)", 3, "Determine the period T of the oscillations.", "NULL"),
    (5, "b(i)", 2, "At time t=0, when the displacement of the ball has its maximum value, the ball is immersed in a trough containing thick oil so that the ball is just below surface... State what is meant by damping.", "NULL"),
    (5, "b(ii)", 3, "On Fig 5.3, sketch a possible variation of the displacement x of the ball with t between t=0 and t=2T.\n[diagram]", "images/9702_w25_qp_42_fig5_3.png"),

    (6, "a", 1, "Define electric field at a point.", "NULL"),
    (6, "b(i)", 2, "An isolated conducting sphere in a vacuum has a capacitance of 69 pF. The charge on the sphere is +83 pC. On Fig 6.1, draw field lines to represent the electric field outside the sphere due to the charge on the sphere.\n[diagram]", "images/9702_w25_qp_42_fig6_1.png"),
    (6, "b(ii)", 2, "Calculate the electric potential at the surface of the sphere.", "NULL"),
    (6, "b(iii)", 2, "Determine the radius of the sphere.", "NULL"),
    (6, "b(iv)", 2, "Calculate the electric field strength E at the surface of the sphere.", "NULL"),
    (6, "c", 2, "The sphere in (b) is discharged by connecting it to earth (0V) through a resistor of 120 MOhms. Calculate the time taken for the charge to fall to 26 pC.", "NULL"),

    (7, "a(i)", 1, "An alternating voltage V varies with time t according to V = 18 cos 40 pi t... show that the period is 0.050 s.", "NULL"),
    (7, "a(ii)", 1, "Determine the root-mean-square (rms) voltage.", "NULL"),
    (7, "b", 3, "On Fig 7.1, sketch the variation of V with t for values of t from t=0 to t=100 ms.\n[diagram]", "images/9702_w25_qp_42_fig7_1.png"),
    (7, "c", 3, "The alternating voltage is rectified to produce an output voltage across load resistor R as shown in Fig 7.2. Fig 7.3 shows the variation with t of the power P in the load resistor. State three conclusions that can be drawn from Fig 7.3.\n[diagram]", "images/9702_w25_qp_42_fig7_2.png"),

    (8, "a", 3, "Fig 8.1 shows the three lowest-frequency lines in the part of the emission spectrum for hydrogen that relates to electron transitions to the ground state. Use the photon model of electromagnetic radiation to explain how the existence of spectral lines in the emission spectrum provides evidence for discrete electron energy levels in the hydrogen atom.\n[diagram]", "images/9702_w25_qp_42_fig8_1.png"),
    (8, "b(i)", 1, "The energy of the ground state in a hydrogen atom is -13.6 eV. Calculate the energy, in J, of the ground state.", "NULL"),
    (8, "b(ii)", 2, "Show that the energy difference between levels n=1 and n=2 is 10.2 eV.", "NULL"),
    (8, "b(iii)", 4, "Complete Table 8.1 to show the energy differences from the ground state.", "NULL"),

    (9, "a", 2, "State what is meant by the mass defect of a nucleus.", "NULL"),
    (9, "b", 4, "The nuclear fusion reaction for the formation of helium-4 from deuterium is represented... Table 9.1 shows masses. Calculate the energy released in the formation of 1.00 mol of helium-4.", "NULL"),
    (9, "c(i)", 2, "The star Sirius has a radius of 1.19x10^9 m and loses mass due to nuclear fusion at a rate of 1.09x10^11 kg s^-1. Determine a value for the luminosity of Sirius. Give a unit.", "NULL"),
    (9, "c(ii)", 2, "Use your answer to determine the surface temperature of Sirius.", "NULL"),
    (9, "d", 3, "Explain how cosmologists use standard candles to estimate the distance of a galaxy from the Earth.", "NULL"),

    (10, "a", 1, "State what is meant by contrast in an X-ray image.", "NULL"),
    (10, "b(i)", 1, "X-rays of intensity I0 are incident normally on a structure as shown in Fig 10.1. Material P has a linear attenuation coefficient of 0.35 cm^-1. The X-rays emerging from region A have intensity 0.053I0. Show that the intensity of X-rays emerging in region B is 0.13I0.\n[diagram]", "images/9702_w25_qp_42_fig10_1.png"),
    (10, "b(ii)", 3, "Determine the linear attenuation coefficient mu of material Q.", "NULL"),
    (10, "b(iii)", 1, "Use the information in b(i) to suggest why the X-rays emerging from the structure form an image that has poor contrast.", "NULL"),
    (10, "c", 3, "Explain how X-rays are used in computed tomography (CT) scanning to produce a three-dimensional image of an internal structure.", "NULL"),
]

q_rows = []
for qn, sqn, mm, txt, img in qs:
    q_rows.append(["9702", "2025", "November", "4", "2", str(qn), sqn, str(mm), txt, img])

with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in q_rows:
        writer.writerow(row)

ms = [
    (1, "a(i)", 1, 1, "radius = 6.37x10^6 * cos 52.2 = 3.90x10^6 m"),
    (1, "a(ii)", 1, 1, "period = 24 hours"),
    (1, "a(ii)", 2, 1, "v = 2pi*r/T OR v=rw and w=2pi/T"),
    (1, "a(ii)", 3, 1, "v = (2pi * 3.90x10^6) / (24*60*60) = 280 m s^-1"),
    (1, "b(i)", 1, 1, "F = mv^2 / r"),
    (1, "b(i)", 2, 1, "F = 1.2 N"),
    (1, "b(ii)", 1, 1, "arrow pointing horizontally to the left"),
    (1, "b(iii)", 1, 1, "arrow from student pointing along the dotted line, labelled weight"),
    (1, "b(iii)", 2, 1, "upwards arrow from student pointing in a direction to the left of normal and above the tangent to the Earth, labelled contact force"),

    (2, "a", 1, 1, "gravitational force is directly proportional to product of masses"),
    (2, "a", 2, 1, "force is inversely proportional to the square of their separation"),
    (2, "b", 1, 1, "molecules are in continuous random motion"),
    (2, "b", 2, 1, "collisions are perfectly elastic"),
    (2, "c(i)", 1, 1, "pV = nRT"),
    (2, "c(i)", 2, 1, "p = 2.01x10^5 Pa"),
    (2, "c(ii)", 1, 1, "number of molecules = 0.0160 x 6.02x10^23"),
    (2, "c(ii)", 2, 1, "separation = cbrt(1.87x10^-4 / ...) = 2.7x10^-9 m"),
    (2, "d(i)", 1, 1, "F = Gm1m2 / r^2 = 6.67x10^-11 * (3.34x10^-27)^2 / (2.7x10^-9)^2"),
    (2, "d(i)", 2, 1, "F = 1.0x10^-46 N"),
    (2, "d(ii)", 1, 1, "numerical comparison between 10^-46 N and 10^-26 N weight leading to conclusion that assumption is supported"),

    (3, "a", 1, 1, "same temperature"),
    (3, "a", 2, 1, "no net transfer of thermal energy between them"),
    (3, "b(i)", 1, 1, "density"),
    (3, "b(ii)", 1, 1, "large response time / large time to reach equilibrium"),
    (3, "b(ii)", 2, 1, "bulky / difficult to set up / difficult to take readings"),
    (3, "b(iii)", 1, 1, "to calibrate other thermometers in a laboratory"),
    (3, "b(iv)", 1, 1, "0 C = 273 K"),
    (3, "b(iv)", 2, 1, "T = 273 * (7.83 - 2.31) / (8.69 - 2.31) (= 236 K)"),
    (3, "b(iv)", 3, 1, "theta = 236 - 273 = -37 C"),

    (4, "a", 1, 1, "increase in internal energy = work done on system + energy transferred to the system by heating"),
    (4, "a", 2, 1, "equation format stated clearly"),
    (4, "b(i)", 1, 1, "U = (3/2) pV"),
    (4, "b(ii)", 1, 1, "pV = NkT and k identified as Boltzmann constant"),
    (4, "b(ii)", 2, 1, "U = (3/2) NkT"),
    (4, "c(i)", 1, 1, "W = (+) 8XY"),
    (4, "c(ii)", 1, 1, "W = - 20XY"),
    (4, "d", 1, 1, "work done during stages BC and DA = 0"),
    (4, "d", 2, 1, "change in internal energy over complete cycle = 0"),
    (4, "d", 3, 1, "thermal energy supplied = 20XY - 8XY = (+) 12XY"),

    (5, "a(i)", 1, 1, "straight line through origin shows that a is proportional to x"),
    (5, "a(i)", 2, 1, "negative gradient shows that a is always in opposite direction to x"),
    (5, "a(ii)", 1, 1, "a0 = w^2 x0"),
    (5, "a(ii)", 2, 1, "w = 2pi / T"),
    (5, "a(ii)", 3, 1, "T = 2pi * sqrt(1.2 / 13) = 1.9 s"),
    (5, "b(i)", 1, 1, "loss of energy of oscillations"),
    (5, "b(i)", 2, 1, "due to resistive forces"),
    (5, "b(ii)", 1, 1, "line starting from x = +-1.2 cm at t = 0"),
    (5, "b(ii)", 2, 1, "line starting from non-zero value of x and entirely above or below t-axis"),
    (5, "b(ii)", 3, 1, "curve starting from non-zero x value, with magnitude continually decreasing"),

    (6, "a", 1, 1, "force per unit positive charge"),
    (6, "b(i)", 1, 1, "radial lines"),
    (6, "b(i)", 2, 1, "arrows pointing away from sphere"),
    (6, "b(ii)", 1, 1, "C = Q / V"),
    (6, "b(ii)", 2, 1, "V = 83 / 69 = (+) 1.2 V"),
    (6, "b(iii)", 1, 1, "V = Q / 4 pi e0 r"),
    (6, "b(iii)", 2, 1, "r = 0.62 m"),
    (6, "b(iv)", 1, 1, "E = Q / 4 pi e0 r^2"),
    (6, "b(iv)", 2, 1, "E = 1.9 N C^-1"),
    (6, "c", 1, 1, "26 = 83 exp [- t / RC]"),
    (6, "c", 2, 1, "t = 9.6x10^-3 s"),

    (7, "a(i)", 1, 1, "T = 2pi / 40pi = 0.050 s"),
    (7, "a(ii)", 1, 1, "Vrms = 18 / sqrt(2) = 13 V"),
    (7, "b", 1, 1, "sinusoidal curve of period 50 ms from t=0 to t=100ms"),
    (7, "b", 2, 1, "correct phase VMAX at t=0,50,100ms"),
    (7, "b", 3, 1, "maximum and minimum voltages shown as +-18 V"),
    (7, "c", 1, 1, "rectification is full-wave"),
    (7, "c", 2, 1, "mean power = 14 W"),
    (7, "c", 3, 1, "resistance of R = 12 Ohms"),

    (8, "a", 1, 1, "electrons moving between levels emit a single photon"),
    (8, "a", 2, 1, "energy of photon = difference between energy levels"),
    (8, "a", 3, 1, "discrete differences between electron energies means energy levels must be discrete"),
    (8, "b(i)", 1, 1, "energy = - (13.6 * 1.6x10^-19) = -2.18x10^-18 J"),
    (8, "b(ii)", 1, 1, "dE = hf"),
    (8, "b(ii)", 2, 1, "dE = 6.63x10^-34 * 2.47x10^15 / 1.6x10^-19 = 10.2 eV"),
    (8, "b(iii)", 1, 1, "n=2 energy level = -3.4 eV"),
    (8, "b(iii)", 2, 1, "n=3 energy difference = 12.1 eV"),
    (8, "b(iii)", 3, 1, "n=4 energy difference = 12.8 eV"),
    (8, "b(iii)", 4, 1, "n=3 energy level = -1.5 eV and n=4 energy level = -0.8 eV"),

    (9, "a", 1, 1, "difference between mass of nucleus and mass of constituent nucleons"),
    (9, "a", 2, 1, "when nucleons are separated to infinity"),
    (9, "b", 1, 1, "dm = 2 * 2.013553 - 4.001505 = 0.025601 u"),
    (9, "b", 2, 1, "E = dm c^2"),
    (9, "b", 3, 1, "energy from one = 3.82x10^-12 J"),
    (9, "b", 4, 1, "energy to form 1 mol = 3.82x10^-12 * 6.02x10^23 = 2.30x10^12 J"),
    (9, "c(i)", 1, 1, "L = 1.09x10^11 * (3.00x10^8)^2"),
    (9, "c(i)", 2, 1, "= 9.81x10^27 W"),
    (9, "c(ii)", 1, 1, "L = 4pi sigma r^2 T^4"),
    (9, "c(ii)", 2, 1, "T = 9930 K"),
    (9, "d", 1, 1, "standard candles have known luminosity"),
    (9, "d", 2, 1, "radiant flux intensity from star measured on Earth"),
    (9, "d", 3, 1, "distance found from F = L / (4pi d^2)"),

    (10, "a", 1, 1, "difference in degrees of blackening"),
    (10, "b(i)", 1, 1, "I = I0 exp(-ux) = I0 exp(-5.8 * 0.35) = 0.13 I0"),
    (10, "b(ii)", 1, 1, "use of exp{-(0.35 * 3.7)} factor"),
    (10, "b(ii)", 2, 1, "0.053I0 = I0 exp{ -[ (0.35*3.7) + 2.1mu ] }"),
    (10, "b(ii)", 3, 1, "mu = 0.78 cm^-1"),
    (10, "b(iii)", 1, 1, "factor of only 2.5 between the intensities so not good contrast"),
    (10, "c", 1, 1, "structure scanned in thin sections"),
    (10, "c", 2, 1, "many scans of each section taken from different angles"),
    (10, "c", 3, 1, "scanning repeated for all sections and data compiled to form 3D image")
]

ms_rows = []
for qn, sqn, mpn, mma, txt in ms:
    ms_rows.append(["9702", "2025", "November", "4", "2", str(qn), sqn, str(mpn), str(mma), txt])

with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in ms_rows:
        writer.writerow(row)

print("w25_42 insertions complete!")

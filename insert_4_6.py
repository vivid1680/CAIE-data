import csv

q_rows = [
    # Question 4
    ["9702", "2025", "March", "4", "2", "4", "NULL", "12", "Simple Harmonic Motion", "NULL"],
    ["9702", "2025", "March", "4", "2", "4", "a", "2", "A small crystal is made to vibrate with simple harmonic motion. The variation with time t of the displacement x of one surface of the crystal from its equilibrium position is shown in Fig. 4.1.\n[diagram]\nShow that the angular frequency of the vibration of the surface is 4.2 × 10^7 rad s^-1.", "images/9702_m25_qp_42_fig4_1.png"],
    ["9702", "2025", "March", "4", "2", "4", "b", "2", "Determine the maximum acceleration a0 of the vibration of the surface.", "NULL"],
    ["9702", "2025", "March", "4", "2", "4", "c", "3", "The crystal may be modelled as a single mass of 2.4 × 10^-4 kg that vibrates as shown in Fig. 4.1.\nCalculate the total energy E of the vibrations.", "NULL"],
    ["9702", "2025", "March", "4", "2", "4", "d(i)", "2", "The crystal generates ultrasound waves that are used to obtain diagnostic information about internal structures.\nThe crystal is made from piezoelectric material.\nExplain how the crystal is made to vibrate.", "NULL"],
    ["9702", "2025", "March", "4", "2", "4", "d(ii)", "3", "A parallel beam of ultrasound waves is incident on a muscle-bone boundary. Data for muscle and bone are given in Table 4.1.\n[diagram]\nCalculate the percentage of the intensity of the ultrasound beam that is transmitted at this boundary.", "images/9702_m25_qp_42_table4_1.png"],

    # Question 5
    ["9702", "2025", "March", "4", "2", "5", "NULL", "9", "Capacitors", "NULL"],
    ["9702", "2025", "March", "4", "2", "5", "a", "2", "A capacitor of capacitance C1 is connected in series with a second capacitor of capacitance C2.\nShow that the combined capacitance C of the two capacitors is given by 1/C = 1/C1 + 1/C2.", "NULL"],
    ["9702", "2025", "March", "4", "2", "5", "b", "3", "Three identical capacitors, each of capacitance C, are connected in a network as shown in Fig. 5.1.\n[diagram]\nThe variation of the charge Q with the potential difference (p.d.) V between the terminals X and Y is shown in Fig. 5.2.\n[diagram]\nShow that C is equal to 44 μF.", "images/9702_m25_qp_42_fig5_1.png"],
    ["9702", "2025", "March", "4", "2", "5", "c(i)", "2", "The capacitor network in Fig. 5.1 is charged and then connected to a resistor of resistance 54 kΩ. The capacitor network discharges through the resistor.\nDetermine the time constant τ of the circuit. Give a unit with your answer.", "NULL"],
    ["9702", "2025", "March", "4", "2", "5", "c(ii)", "2", "Determine the time taken for the discharge current to reduce to 15% of the initial discharge current.", "NULL"],

    # Question 6
    ["9702", "2025", "March", "4", "2", "6", "NULL", "11", "Magnetic Fields", "NULL"],
    ["9702", "2025", "March", "4", "2", "6", "a", "2", "An electric field and a magnetic field are used to form a velocity selector. Charged particles, called ions, pass into a region of uniform electric and magnetic fields that is between parallel plates, as shown in Fig. 6.1.\n[diagram]\nThe potential difference (p.d.) between the plates of the velocity selector is V. The separation of the plates is d and the magnetic flux density is B.\nShow that the speed u of ions that pass undeviated through the velocity selector is given by u = V / Bd.", "images/9702_m25_qp_42_fig6_1.png"],
    ["9702", "2025", "March", "4", "2", "6", "b", "3", "Positive ions with kinetic energy 4.1 × 10^-17 J and mass 3.2 × 10^-27 kg pass undeviated through the velocity selector when V is equal to 980 V and d is equal to 3.6 × 10^-2 m.\nDetermine B.", "NULL"],
    ["9702", "2025", "March", "4", "2", "6", "c", "1", "A proton passes undeviated through the velocity selector.\nAn alpha particle enters the velocity selector at the same speed as the proton.\nState how the expression in (a) predicts that the alpha particle also passes undeviated through the velocity selector.", "NULL"],
    ["9702", "2025", "March", "4", "2", "6", "d", "3", "By reference to Fig. 6.1 and to the forces acting on a positive ion, determine the direction of the magnetic field. Explain your reasoning.", "NULL"],
    ["9702", "2025", "March", "4", "2", "6", "e", "2", "The positive ions in (b) enter the velocity selector with greater kinetic energy.\nOn Fig. 6.1, sketch the path of these ions.", "images/9702_m25_qp_42_fig6_1.png"]
]


ms_rows = [
    # Q4
    ["9702", "2025", "March", "4", "2", "4", "a", "1", "1", "ω = 2π / T"],
    ["9702", "2025", "March", "4", "2", "4", "a", "2", "1", "= 2π / (0.15 × 10^-6) = 4.2 × 10^7 rad s^-1"],
    ["9702", "2025", "March", "4", "2", "4", "b", "1", "1", "a0 = ω^2 x0"],
    ["9702", "2025", "March", "4", "2", "4", "b", "2", "1", "= (4.2 × 10^7)^2 × 40 × 10^-6 = 7.1 × 10^10 m s^-2"],
    ["9702", "2025", "March", "4", "2", "4", "c", "1", "1", "E = 0.5 m ω^2 x0^2"],
    ["9702", "2025", "March", "4", "2", "4", "c", "2", "1", "= 0.5 × 2.4 × 10^-4 × (4.2 × 10^7)^2 × (40 × 10^-6)^2"],
    ["9702", "2025", "March", "4", "2", "4", "c", "3", "1", "= 340 J"],
    ["9702", "2025", "March", "4", "2", "4", "d(i)", "1", "1", "apply alternating p.d. (to / across crystal)"],
    ["9702", "2025", "March", "4", "2", "4", "d(i)", "2", "1", "applying p.d. to / across crystal causes it to distort"],
    ["9702", "2025", "March", "4", "2", "4", "d(ii)", "1", "1", "Z = ρ c, Zm = 1100 × 1600 (= 1.76 × 10^6), Zb = 1900 × 4100 (= 7.79 × 10^6)"],
    ["9702", "2025", "March", "4", "2", "4", "d(ii)", "2", "1", "intensity reflection co-efficient = [(7.79 - 1.76) / (7.79 + 1.76)]^2 = 0.40 or 40%"],
    ["9702", "2025", "March", "4", "2", "4", "d(ii)", "3", "1", "percentage transmitted = 60%"],

    # Q5
    ["9702", "2025", "March", "4", "2", "5", "a", "1", "1", "Q = Q1 = Q2 and V = V1 + V2"],
    ["9702", "2025", "March", "4", "2", "5", "a", "2", "1", "V = Q/C so: Q/C = Q/C1 + Q/C2 leading to 1/C = 1/C1 + 1/C2"],
    ["9702", "2025", "March", "4", "2", "5", "b", "1", "1", "total capacitance = C + 0.5C = (3/2)C"],
    ["9702", "2025", "March", "4", "2", "5", "b", "2", "1", "total capacitance = gradient = 400 × 10^-6 / 6.0"],
    ["9702", "2025", "March", "4", "2", "5", "b", "3", "1", "either: C = (2 × 400 × 10^-6)/ (3 × 6.0) = 4.4 × 10^-5 F = 44 μF or: C = (2 × 400)/ (3 × 6.0) = 44 μF"],
    ["9702", "2025", "March", "4", "2", "5", "c(i)", "1", "1", "τ = RC"],
    ["9702", "2025", "March", "4", "2", "5", "c(i)", "2", "1", "= 54 × 10^3 × (3/2) × 44 × 10^-6 = 3.6 s"],
    ["9702", "2025", "March", "4", "2", "5", "c(ii)", "1", "1", "0.15 = exp(-t / 3.6)"],
    ["9702", "2025", "March", "4", "2", "5", "c(ii)", "2", "1", "t = 6.8 s"],

    # Q6
    ["9702", "2025", "March", "4", "2", "6", "a", "1", "1", "FB = FE"],
    ["9702", "2025", "March", "4", "2", "6", "a", "2", "1", "either: Bqu = qE and E = V / d leading to u = V / Bd or: Bqu = qV / d leading to u = V / Bd"],
    ["9702", "2025", "March", "4", "2", "6", "b", "1", "1", "EK = 0.5 m u^2"],
    ["9702", "2025", "March", "4", "2", "6", "b", "2", "1", "u = √[(2 × 4.1 × 10^-17) / (3.2 × 10^-27)] = 1.6 × 10^5 m s^-1"],
    ["9702", "2025", "March", "4", "2", "6", "b", "3", "1", "B = 980 / (3.6 × 10^-2 × 1.6 × 10^5) = 0.17 T"],
    ["9702", "2025", "March", "4", "2", "6", "c", "1", "1", "expression is independent of mass and charge"],
    ["9702", "2025", "March", "4", "2", "6", "d", "1", "1", "either: electric force is downwards so magnetic force is upwards or: no resultant force so magnetic force is upwards"],
    ["9702", "2025", "March", "4", "2", "6", "d", "2", "1", "(positive ions so) current is from left to right"],
    ["9702", "2025", "March", "4", "2", "6", "d", "3", "1", "from (Fleming’s) left-hand rule, magnetic field is into the page"],
    ["9702", "2025", "March", "4", "2", "6", "e", "1", "1", "curved path inside plates with consistent direction of curvature and with no discontinuity at entry or in curvature"],
    ["9702", "2025", "March", "4", "2", "6", "e", "2", "1", "direction of deflection is upwards"]
]

with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in q_rows:
        writer.writerow(row)

with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in ms_rows:
        writer.writerow(row)


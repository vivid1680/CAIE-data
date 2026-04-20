import csv

q_rows = [
    # Question 1
    ["9702", "2025", "March", "4", "2", "1", "NULL", "9", "Circular Motion", "NULL"],
    ["9702", "2025", "March", "4", "2", "1", "a", "1", 
     "A steel ball is placed on the inside surface of a hollow circular cone. The ball moves in a horizontal circle at constant speed, as shown in Fig. 1.1.\n[diagram]\nThe angle of the side of the cone to the horizontal is 52°. There is no friction between the ball and the cone.\nFig. 1.2 shows a cross-section through the cone and the steel ball.\n[diagram]\nOn Fig. 1.2, draw labelled arrows to show the two forces acting on the ball.", 
     "images/9702_m25_qp_42_fig1_2.png"], # (It actually references fig 1.1 and 1.2, we'll keep the latter as representative, or combine)
    ["9702", "2025", "March", "4", "2", "1", "b", "2", "Describe how the forces acting on the ball cause its acceleration to be centripetal.", "NULL"],
    ["9702", "2025", "March", "4", "2", "1", "c", "3", "The ball moves in a circle of radius 0.15 m.\nShow that the speed of the ball is 1.4 m s^-1.", "NULL"],
    ["9702", "2025", "March", "4", "2", "1", "d", "2", "Calculate the angular speed ω of the ball.", "NULL"],
    ["9702", "2025", "March", "4", "2", "1", "e", "1", "The speed of the ball is increased.\nExplain why the radius of the circular path of the ball increases.", "NULL"],
    
    # Question 2
    ["9702", "2025", "March", "4", "2", "2", "NULL", "7", "Gravitational and Electric Fields", "NULL"],
    ["9702", "2025", "March", "4", "2", "2", "a", "3", 
     "The magnitude of the gravitational potential on the surface of a planet of radius R is φ.\nThe planet can be considered to be an isolated sphere.\nOn Fig. 2.1, sketch the variation of the gravitational potential with distance x from the centre of the planet for values of x between R and 4R.\n[diagram]", 
     "images/9702_m25_qp_42_fig2_1.png"],
    ["9702", "2025", "March", "4", "2", "2", "b", "2", 
     "A satellite is in a geostationary orbit above the Earth. At time t = 0, the magnitude of the gravitational potential due to the Earth at the location of the satellite is φ.\nOn Fig. 2.2, sketch the variation of the gravitational potential due to the Earth at the location of the satellite for values of t between t = 0 and t = 24 hours.\n[diagram]",
     "images/9702_m25_qp_42_fig2_2.png"],
    ["9702", "2025", "March", "4", "2", "2", "c", "2",
     "The electric potential difference (p.d.) between two parallel plates is V, as shown in Fig. 2.3.\n[diagram]\nThe distance between the plates is d. The region between the plates is a vacuum.\nOn Fig. 2.4, sketch the variation of the electric potential with distance from the positive plate.\n[diagram]",
     "images/9702_m25_qp_42_fig2_4.png"],

    # Question 3
    ["9702", "2025", "March", "4", "2", "3", "NULL", "12", "Thermal Physics", "NULL"],
    ["9702", "2025", "March", "4", "2", "3", "a(i)", "2", "Two metal cuboids P and Q are in thermal contact with each other.\nP and Q are in thermal equilibrium.\nState what is meant by the term thermal equilibrium.", "NULL"],
    ["9702", "2025", "March", "4", "2", "3", "a(ii)", "3", "Data for P and Q are given in Table 3.1.\n[diagram]\nP and Q are initially both at the same temperature.\nP is supplied with 24 kJ of thermal energy. After some time, P and Q are once again both at the same temperature as each other.\nP and Q are perfectly insulated from the surroundings.\nDetermine the change in temperature ΔT of Q.", "images/9702_m25_qp_42_table3_1.png"],
    ["9702", "2025", "March", "4", "2", "3", "b(i)", "3", "Nitrogen may be assumed to be an ideal gas. A fixed amount of nitrogen gas is contained at a constant pressure of 1.6 × 10^5 Pa.\nThe variation of the volume V of the gas with the temperature θ of the gas is shown in Fig. 3.1.\n[diagram]\nThe temperature of the nitrogen gas is increased from 0 °C to 210 °C.\nDetermine the work done on the gas.", "images/9702_m25_qp_42_fig3_1.png"],
    ["9702", "2025", "March", "4", "2", "3", "b(ii)", "2", "Determine the number N of molecules of nitrogen gas.", "NULL"],
    ["9702", "2025", "March", "4", "2", "3", "b(iii)", "2", "The mass of a nitrogen molecule is 4.7 × 10^-26 kg.\nCalculate the root-mean-square (r.m.s.) speed of a nitrogen molecule at 210 °C.", "NULL"]
]

ms_rows = [
    # Q1
    ["9702", "2025", "March", "4", "2", "1", "a", "1", "1", "arrow vertically downwards labelled 'weight' and arrow perpendicular to cone, inwards and upwards, labelled 'normal contact force'"],
    ["9702", "2025", "March", "4", "2", "1", "b", "1", "1", "vertical component of contact force = weight (so no resultant force vertically)"],
    ["9702", "2025", "March", "4", "2", "1", "b", "2", "1", "horizontal component of contact force is resultant force towards centre (of circle)"],
    ["9702", "2025", "March", "4", "2", "1", "c", "1", "1", "a = v^2 / r"],
    ["9702", "2025", "March", "4", "2", "1", "c", "2", "1", "a = g tan 52°"],
    ["9702", "2025", "March", "4", "2", "1", "c", "3", "1", "9.81 × tan 52° = v^2 / 0.15 leading to v = 1.4 m s^-1"],
    ["9702", "2025", "March", "4", "2", "1", "d", "1", "1", "v = rω or a = rω^2"],
    ["9702", "2025", "March", "4", "2", "1", "d", "2", "1", "ω = 1.4 / 0.15 or √(9.81 × tan 52° / 0.15) = 9.3 rad s^-1"],
    ["9702", "2025", "March", "4", "2", "1", "e", "1", "1", "same resultant force / same acceleration so v^2 is proportional to r (so if speed increases radius must also increase)"],
    
    # Q2
    ["9702", "2025", "March", "4", "2", "2", "a", "1", "1", "sketch: line from x = R to x = 4R entirely in the negative φ region"],
    ["9702", "2025", "March", "4", "2", "2", "a", "2", "1", "curve with continuously decreasing magnitude and with gradient of continuously decreasing magnitude, starting at (R, -φ)"],
    ["9702", "2025", "March", "4", "2", "2", "a", "3", "1", "line passing through (2R, -0.5φ) and (4R, -0.25φ)"],
    ["9702", "2025", "March", "4", "2", "2", "b", "1", "1", "horizontal straight line from t = 0 to t = 24 hours"],
    ["9702", "2025", "March", "4", "2", "2", "b", "2", "1", "line starting at (0, -φ)"],
    ["9702", "2025", "March", "4", "2", "2", "c", "1", "1", "straight line with non-zero gradient from 0 to d"],
    ["9702", "2025", "March", "4", "2", "2", "c", "2", "1", "line with negative gradient from (0, V) to (d, 0)"],

    # Q3
    ["9702", "2025", "March", "4", "2", "3", "a(i)", "1", "1", "(P and Q are at the) same temperature"],
    ["9702", "2025", "March", "4", "2", "3", "a(i)", "2", "1", "no net transfer of thermal energy (between P and Q)"],
    ["9702", "2025", "March", "4", "2", "3", "a(ii)", "1", "1", "Q = mcΔT"],
    ["9702", "2025", "March", "4", "2", "3", "a(ii)", "2", "1", "24 × 10^3 = (0.54 × 390 × ΔT) + (0.37 × 910 × ΔT)"],
    ["9702", "2025", "March", "4", "2", "3", "a(ii)", "3", "1", "ΔT = 44 K"],
    ["9702", "2025", "March", "4", "2", "3", "b(i)", "1", "1", "work done = pΔV"],
    ["9702", "2025", "March", "4", "2", "3", "b(i)", "2", "1", "= (1.6 × 10^5) × (0.18 - 0.32)"],
    ["9702", "2025", "March", "4", "2", "3", "b(i)", "3", "1", "= -2.2 × 10^4 J"],
    ["9702", "2025", "March", "4", "2", "3", "b(ii)", "1", "1", "pV = NkT"],
    ["9702", "2025", "March", "4", "2", "3", "b(ii)", "2", "1", "N = (1.6 × 10^5 × 0.18) / (1.38 × 10^-23 × 273) = 7.6 × 10^24"],
    ["9702", "2025", "March", "4", "2", "3", "b(iii)", "1", "1", "0.5m〈c^2〉 = (3/2)kT"],
    ["9702", "2025", "March", "4", "2", "3", "b(iii)", "2", "1", "r.m.s. speed = √[(3 × 1.38 × 10^-23 × (210 + 273) / (4.7 × 10^-26)] = 650 m s^-1"]
]

with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in q_rows:
        writer.writerow(row)

with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in ms_rows:
        writer.writerow(row)

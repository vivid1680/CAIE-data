import csv

# Metadata inserts
with open(r"data\papers.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "November", "2", "2"])

with open(r"data\grade_boundaries.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "November", "2", "2", "60", "43", "37", "31", "24", "16"])

ec_rows = [
    ["9702", "2025", "November", "2", "2", "NULL", "The paper tested a solid understanding of mechanics and electricity. Most candidates were able to correctly identify scalar and vector quantities, though derivation of formulae from first principles remains a challenge for some."],
    ["9702", "2025", "November", "2", "2", "1", "Candidates demonstrated the derivation of EK = 1/2mv^2. Successful responses used the work formula W=Fs and substituted v^2 = u^2 + 2as (where u=0) to reach the final expression."],
    ["9702", "2025", "November", "2", "2", "2", "This question required taking moments..."],
    ["9702", "2025", "November", "2", "2", "6", "Determining the resistance R required a clear understanding of potential dividers and parallel branches..."]
]

with open(r"data\examiner_comments.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ec_rows:
        writer.writerow(row)

# Q maps: (q_num, sub_q, max_mark, text, diagram_path)
qs = [
    (1, "a", 2, "Scientists are investigating the variation in air pressure at different locations on a mountain. The scientists take measurements... Complete Table 1.1 by stating the SI base unit for each quantity and identifying whether each quantity is a scalar or a vector.", "NULL"),
    (1, "b(i)", 2, "At one location, the density of the air is 1.1 kg m^-3. A spherical weather balloon is filled with a gas and released from rest. The balloon has radius 0.90 m. Calculate the upthrust acting on the balloon when it is released.", "NULL"),
    (1, "b(ii)", 2, "Explain why an upthrust acts on the balloon.", "NULL"),
    (1, "b(iii)", 3, "The balloon has weight 19 N. Calculate the magnitude of the initial acceleration of the balloon.", "NULL"),
    (1, "c", 2, "A quantity c relating to the motion of the balloon is calculated from three measured quantities k, F and v using the formula c = (2kF)/v^2. The percentage uncertainties in the measured quantities are k=5%, F=3%, v=4%. The calculated value of c is 1.8. Determine the absolute uncertainty in c.", "NULL"),
    
    (2, "a(i)", 2, "A spacecraft in deep space uses jets of hot gas from its thrusters to change its velocity.\nThruster A is a distance of 1.6 m leftwards from the centre of gravity. Thruster C is a distance of 0.40 m upwards. Thruster A produces a force of 60 N upwards. Thruster C produces a force of 220 N leftwards. Calculate the resultant moment due to these forces about the centre of gravity.\n[diagram]", "images/9702_w25_qp_22_fig2_1.png"),
    (2, "a(ii)", 1, "State and explain whether the forces from A and C are a couple.", "NULL"),
    (2, "b", 2, "Thrusters A and C are now switched off. Thruster B is activated at time t1, producing a constant force on the spacecraft until fuel runs out at t2. As fuel is used, the total mass decreases. On Fig 2.2, sketch the variation of speed of the spacecraft with time from t1 to t2.\n[diagram]", "images/9702_w25_qp_22_fig2_2.png"),
    (2, "c(i)", 2, "The spacecraft now splits apart into a carrier and a payload as shown in Fig 2.3. During the split, an average force of 5500 N acts on the payload for a time of 0.36 s. The velocity of the payload increases by 8.5 m s^-1 in the upwards direction. The combined mass is 2.5x10^3 kg. State the principle of conservation of momentum.\n[diagram]", "images/9702_w25_qp_22_fig2_3.png"),
    (2, "c(ii)", 2, "Show that the mass of the payload is 230 kg.", "NULL"),
    (2, "c(iii)", 3, "Calculate the magnitude of the change in velocity of the carrier.", "NULL"),

    (3, "a", 2, "A spring is fixed at one end and attached to the frame of a pulley at the other end. A cable is passed around the wheel of the pulley. The spring is stretched... The spring obeys Hooke's law and has a spring constant k of 250 N m^-1. A force F acts on the spring. The tension in the cable is T. The pulley is in equilibrium. On Fig 3.2, draw labelled arrows to show the directions of the forces acting on the pulley.\n[diagram]", "images/9702_w25_qp_22_fig3_1.png"),
    (3, "b(i)", 1, "The force F is 110 N. Determine T.", "NULL"),
    (3, "b(ii)", 2, "Calculate the extension of the spring.", "NULL"),
    (3, "c(i)", 2, "A second identical spring with the same spring constant of 250 N m^-1 is now also connected to the pulley, as shown in Fig. 3.3. The tension in the cable is kept the same. The pulley is again in equilibrium. Determine the extension of the springs.\n[diagram]", "images/9702_w25_qp_22_fig3_3.png"),
    (3, "c(ii)", 2, "The elastic potential energy stored in the spring in Fig 3.1 is E1. The total elastic potential energy stored in the two springs in Fig 3.3 is E2. Calculate the ratio E1/E2.", "NULL"),

    (4, "a", 3, "A laser emits visible light of a single frequency in a vacuum. The light is incident normally on a double slit and then forms a pattern of bright and dark fringes on a screen, as shown in Fig 4.1. The separation of the slits is 1.0x10^-3 m. The distance to the screen is 4.8 m. The distance between the centres of adjacent dark fringes is 3.3 mm. Explain how the pattern of bright and dark fringes is formed.\n[diagram]", "images/9702_w25_qp_22_fig4_1.png"),
    (4, "b", 4, "Calculate the frequency of the light emitted by the laser.", "NULL"),
    (4, "c", 1, "The double slit is removed. A second laser is placed beside the first laser. The second laser produces visible light of a different frequency. Explain why a steady pattern of bright and dark fringes is not formed.", "NULL"),

    (5, "a", 1, "Fig. 5.1 shows a circuit containing a battery, two fixed resistors X and Y, and a light-dependent resistor (LDR) Z. The battery has electromotive force 5.0 V and internal resistance 4.7 Ohms. The current in X is I1 and the current in Y is I2. The resistance of X is 100 Ohms. The resistance of Z varies with intensity of light as shown in Fig 5.2. State Kirchhoff's first law.\n[diagram]", "images/9702_w25_qp_22_fig5_1.png"),
    (5, "b(i)", 2, "The intensity of light incident on Z is 130 W m^-2. The current in the battery is 38 mA. Show that the terminal potential difference of the battery is 4.8 V.", "NULL"),
    (5, "b(ii)", 3, "Calculate the current I2 in Y.", "NULL"),
    (5, "b(iii)", 2, "Calculate the power dissipated in Y.", "NULL"),
    (5, "b(iv)", 3, "The intensity of the light incident on Z decreases. State and explain the effect on the terminal potential difference of the battery.", "NULL"),

    (6, "a", 1, "State what is meant by a fundamental particle.", "NULL"),
    (6, "b(i)", 2, "Particle Q is a meson with a charge of 0. Determine a possible quark composition for Q.", "NULL"),
    (6, "b(ii)", 3, "Particle Q has a mass of 0.67 u and a kinetic energy of 2.1x10^-16 J. Calculate the speed of particle Q.", "NULL"),
    (6, "c(i)", 1, "Radium-228 is a radioactive nuclide. State the number of electrons in a neutral atom of radium-228.", "NULL"),
    (6, "c(ii)", 2, "A nucleus of radium-228 undergoes a series of decays to form nucleus X. During the process, 5 alpha-particles and 4 beta- particles are emitted. Determine the number of protons and the number of neutrons in nucleus X.", "NULL"),
]

q_rows = []
for qn, sqn, mm, txt, img in qs:
    q_rows.append(["9702", "2025", "November", "2", "2", str(qn), sqn, str(mm), txt, img])

with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in q_rows:
        writer.writerow(row)

ms = [
    (1, "a", 1, 1, "air temperature: K and air pressure: kg m^-1 s^-2"),
    (1, "a", 2, 1, "scalar only ticked for both air temperature and air pressure"),
    
    (1, "b(i)", 1, 1, "upthrust = 1.1 x 9.81 x (4pi x 0.90^3 / 3)"),
    (1, "b(i)", 2, 1, "= 33 N"),

    (1, "b(ii)", 1, 1, "(due to difference in height / depth there is a) difference in pressure between top and bottom (of balloon)"),
    (1, "b(ii)", 2, 1, "(due to pressure difference, upwards) force on bottom of balloon is greater (than downwards force on top of balloon, so resultant force is upwards)"),

    (1, "b(iii)", 1, 1, "(Sum)F = 33 - 19 (= 14 N)"),
    (1, "b(iii)", 2, 1, "m = 19 / 9.81 (= 1.94 kg)"),
    (1, "b(iii)", 3, 1, "a = (33 - 19) / (19 / 9.81) = 7.2 m s^-2"),

    (1, "c", 1, 1, "(absolute percentage uncertainty) 5 + 3 + (2x4) = 16%"),
    (1, "c", 2, 1, "absolute uncertainty in c = 1.8 x 0.16 = (+-) 0.3"),

    (2, "a(i)", 1, 1, "60x1.6 = 96 Nm OR 220x0.4 = 88 Nm"),
    (2, "a(i)", 2, 1, "resultant moment = 96 - 88 = 8.0 Nm"),
    
    (2, "a(ii)", 1, 1, "the resultant force (of A and C) is not zero so (they are) not a couple"),

    (2, "b", 1, 1, "line with a positive gradient from (t1, 0) to t2"),
    (2, "b", 2, 1, "line with increasing positive gradient from t1 to t2"),

    (2, "c(i)", 1, 1, "sum / total momentum before = sum / total momentum after OR sum / total momentum (of a system of objects) is constant"),
    (2, "c(i)", 2, 1, "if no (resultant) external force / for an isolated system"),

    (2, "c(ii)", 1, 1, "(Delta)p = F(Delta)t"),
    (2, "c(ii)", 2, 1, "m = 5500 x 0.36 / 8.5 = 230 kg"),

    (2, "c(iii)", 1, 1, "(Delta)p = 5500 x 0.36 = 1980 N s"),
    (2, "c(iii)", 2, 1, "1980 = (2.5x10^3 - 230)(Delta)v"),
    (2, "c(iii)", 3, 1, "(Delta)v = 0.87 m s^-1"),

    (3, "a", 1, 1, "an arrow horizontally on the page to the left labelled F"),
    (3, "a", 2, 1, "two arrows horizontally on the page to the right each labelled T"),

    (3, "b(i)", 1, 1, "T = 110/2 = 55 N"),
    
    (3, "b(ii)", 1, 1, "x = F/k = 110/250"),
    (3, "b(ii)", 2, 1, "= 0.44 m"),

    (3, "c(i)", 1, 1, "extension = 55/250 OR 110/(2x250)"),
    (3, "c(i)", 2, 1, "extension = 0.22 m"),

    (3, "c(ii)", 1, 1, "E = 1/2 Fx OR E = 1/2 kx^2"),
    (3, "c(ii)", 2, 1, "E1/E2 = 2.0"),

    (4, "a", 1, 1, "light diffracts / spreads (at slit(s))"),
    (4, "a", 2, 1, "light (from each slit) superposes / interferes (at screen)"),
    (4, "a", 3, 1, "when phase difference is 0 / path difference is n(lambda) a bright fringe is formed OR when phase difference is 180 / path difference is (n+1/2)(lambda) a dark fringe is formed"),

    (4, "b", 1, 1, "(lambda) = ax / D"),
    (4, "b", 2, 1, "(lambda) = 1.0x10^-3 x 3.3x10^-3 / 4.8 (= 6.875x10^-7 m)"),
    (4, "b", 3, 1, "f = v / (lambda) = 3.0x10^8 / 6.875x10^-7"),
    (4, "b", 4, 1, "= 4.4 x 10^14 Hz"),

    (4, "c", 1, 1, "the light / beams (have different frequencies so) are not coherent / do not have constant phase difference"),

    (5, "a", 1, 1, "sum of current(s) into junction = sum of current(s) out junction OR (algebraic) sum of current(s) at a junction is zero"),

    (5, "b(i)", 1, 1, "V = E - Ir"),
    (5, "b(i)", 2, 1, "V = 5.0 - (38x10^-3 x 4.7) = 4.8 V"),

    (5, "b(ii)", 1, 1, "R(Z) = 120 Ohms"),
    (5, "b(ii)", 2, 1, "I2 = 38x10^-3 - (4.8 / (100 + 120))"),
    (5, "b(ii)", 3, 1, "I2 = 0.016 A"),

    (5, "b(iii)", 1, 1, "P = IV OR P = I^2 R OR P = V^2 / R"),
    (5, "b(iii)", 2, 1, "P = 0.016 x 4.8 = 0.077 W"),

    (5, "b(iv)", 1, 1, "resistance of the LDR / Z increases (as light intensity decreases)"),
    (5, "b(iv)", 2, 1, "total resistance (of the circuit) increases OR current in the battery decreases"),
    (5, "b(iv)", 3, 1, "(potential difference across the internal resistor decreases so) the terminal potential difference increases"),

    (6, "a", 1, 1, "(a particle that) cannot be divided / subdivided (into smaller particles)"),
    
    (6, "b(i)", 1, 1, "any combination of one quark and one antiquark"),
    (6, "b(i)", 2, 1, "up / charm / top and antiup / anticharm / antitop OR down / strange / bottom and antidown / antistrange / antibottom"),

    (6, "b(ii)", 1, 1, "E(K) = 1/2 mv^2"),
    (6, "b(ii)", 2, 1, "2.1x10^-16 = 1/2 x (0.67 x 1.66x10^-27) x v^2"),
    (6, "b(ii)", 3, 1, "v = 6.1 x 10^5 m s^-1"),

    (6, "c(i)", 1, 1, "number of electrons = 88"),
    
    (6, "c(ii)", 1, 1, "number of protons = 88 - (5x2) + 4 = 82"),
    (6, "c(ii)", 2, 1, "number of neutrons = (228 - 20) - 82 = 126")
]

ms_rows = []
for qn, sqn, mpn, mma, txt in ms:
    ms_rows.append(["9702", "2025", "November", "2", "2", str(qn), sqn, str(mpn), str(mma), txt])

with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in ms_rows:
        writer.writerow(row)

print("w25_22 insertions complete!")

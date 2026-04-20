import csv

qs = [
    # Q1
    ["9702", "2025", "June", "4", "2", "1", "a", "1", "Define the radian.", "NULL"],
    ["9702", "2025", "June", "4", "2", "1", "b(i)", "2", "The rear wheel and the pedals of a bicycle are connected by a chain that passes around two cogs (toothed wheels), as shown in Fig. 1.1.\n[diagram]\nThe small cog has a radius of 0.038 m and is fixed to the rear wheel so that it rotates with it.\nThe large cog has a radius of 0.15 m and is fixed to the pedals so that it rotates with them.\nThe rear wheel has a radius of 0.46 m.\nThe bicycle is being pedalled so that it moves in a straight line at a constant speed of 17 m s–1.\nCalculate the angular speed of the rear wheel.", "images/9702_s25_qp_42_fig1_1.png"],
    ["9702", "2025", "June", "4", "2", "1", "b(ii)", "2", "Calculate the period of rotation of the small cog.", "NULL"],
    ["9702", "2025", "June", "4", "2", "1", "b(iii)", "1", "Show that the distance moved by point X on the chain during one full rotation of the small cog is 0.24 m.", "NULL"],
    ["9702", "2025", "June", "4", "2", "1", "b(iv)", "2", "Use the information in (b)(iii) to determine the angle through which the large cog rotates during one full rotation of the small cog.", "NULL"],
    ["9702", "2025", "June", "4", "2", "1", "c", "2", "The chain of the bicycle in (b) is moved onto a smaller cog fixed to the rear wheel. The speed of the bicycle does not change.\nExplain, without calculation, the effect of this change on the angular speed of the pedals.", "NULL"],

    # Q2
    ["9702", "2025", "June", "4", "2", "2", "a(i)", "2", "State what is represented by a gravitational field line.", "NULL"],
    ["9702", "2025", "June", "4", "2", "2", "a(ii)", "2", "The Earth may be considered as a uniform sphere, as shown in Fig. 2.1.\n[diagram]\nOn Fig. 2.1, draw field lines to represent the Earth’s gravitational field outside the Earth.", "images/9702_s25_qp_42_fig2_1.png"],
    ["9702", "2025", "June", "4", "2", "2", "b(i)", "1", "The Earth’s magnetic field may be considered as being due to the Earth acting as a long solenoid, as shown in Fig. 2.2.\n[diagram]\nThe magnetic poles do not align with the geographic poles, which are on the axis of rotation.\nFig. 2.3 is a copy of Fig. 2.2 without the labels but with two magnetic field lines shown.\n[diagram]\nOn Fig. 2.3, label the magnetic poles with the letters N and S to indicate which one is the magnetic N pole and which one is the magnetic S pole.", "images/9702_s25_qp_42_fig2_2.png,images/9702_s25_qp_42_fig2_3.png"],
    ["9702", "2025", "June", "4", "2", "2", "b(ii)", "2", "On Fig. 2.3, draw field lines to represent the Earth’s magnetic field outside the Earth.", "NULL"],
    ["9702", "2025", "June", "4", "2", "2", "c(i)", "2", "An observer moves around the surface of the Earth.\nUse your answer in (a)(ii) to explain why the observed gravitational field of the Earth does not vary around the surface.", "NULL"],
    ["9702", "2025", "June", "4", "2", "2", "c(ii)", "3", "With reference to your answer in (b)(ii), describe how the observed magnetic field of the Earth varies around the surface.", "NULL"],

    # Q3
    ["9702", "2025", "June", "4", "2", "3", "a", "2", "Define specific heat capacity.", "NULL"],
    ["9702", "2025", "June", "4", "2", "3", "b(i)", "2", "A block of aluminium has a volume of 3.612 × 10–3 m3 at a temperature of 0 °C.\nAluminium has a density of 2.700 × 103 kg m–3 at 0 °C.\nIt has a density of 2.620 × 103 kg m–3 at 500 °C.\nThe block is heated so that its temperature increases from 0 °C to 500 °C at an atmospheric pressure of 1.01 × 105 Pa.\nThe increase in internal energy of the block is 4.38 MJ.\nCalculate the mass of the block.", "NULL"],
    ["9702", "2025", "June", "4", "2", "3", "b(ii)", "1", "Show that the volume of the block at a temperature of 500 °C is 3.722 × 10–3 m3.", "NULL"],
    ["9702", "2025", "June", "4", "2", "3", "b(iii)", "2", "Use the information in (b)(ii) to determine the magnitude of the work done on the block when its temperature is raised from 0 °C to 500 °C.", "NULL"],
    ["9702", "2025", "June", "4", "2", "3", "b(iv)", "2", "Explain whether the work done on the block is positive or negative.", "NULL"],
    ["9702", "2025", "June", "4", "2", "3", "b(v)", "3", "Use the first law of thermodynamics to determine, to three significant figures, a value for the specific heat capacity of aluminium. Explain your reasoning. Give a unit with your answer.", "NULL"],
    ["9702", "2025", "June", "4", "2", "3", "c", "1", "Without further calculation, suggest with a reason how doubling the pressure in (b) is likely to affect the answer in (b)(v).", "NULL"],

    # Q4
    ["9702", "2025", "June", "4", "2", "4", "a(i)", "1", "The equation of state for an ideal gas may be written as pVA = NBT. State the meaning, in the equation, of the symbol T.", "NULL"],
    ["9702", "2025", "June", "4", "2", "4", "a(ii)", "1", "Identify the constant B.", "NULL"],
    ["9702", "2025", "June", "4", "2", "4", "b(i)", "2", "The product pV for an ideal gas is also given by pV = 1/3 Nm 〈c2〉. State the meanings, in this equation, of the symbols m and 〈c2〉.", "NULL"],
    ["9702", "2025", "June", "4", "2", "4", "b(ii)", "2", "Use the equations in (a) and (b) to derive an expression, in terms of A, B and T, for the mean kinetic energy EK of a molecule of the gas.", "NULL"],
    ["9702", "2025", "June", "4", "2", "4", "c", "2", "On Fig. 4.1, sketch the variation with T of the root-mean-square (r.m.s.) speed of the molecules of an ideal gas.\n[diagram]", "images/9702_s25_qp_42_fig4_1.png"],

    # Q5
    ["9702", "2025", "June", "4", "2", "5", "a", "2", "State what is meant by simple harmonic motion.", "NULL"],
    ["9702", "2025", "June", "4", "2", "5", "b(i)", "1", "A block is suspended by a spring. The block oscillates vertically with simple harmonic motion.\nThe velocity v of the block varies with time t according to v = 0.56 cos(16t) where v is in m s–1 and t is in s.\nCalculate the period of the oscillation.", "NULL"],
    ["9702", "2025", "June", "4", "2", "5", "b(ii)", "2", "Determine the amplitude x0 of the oscillation.", "NULL"],
    ["9702", "2025", "June", "4", "2", "5", "b(iii)", "1", "Use your answer in (b)(ii) to determine the equation for v in terms of the displacement x of the block, where v is in m s–1 and x is in m.", "NULL"],
    ["9702", "2025", "June", "4", "2", "5", "b(iv)", "3", "On Fig. 5.1, sketch the variation of v with x.\n[diagram]", "images/9702_s25_qp_42_fig5_1.png"],

    # Q6
    ["9702", "2025", "June", "4", "2", "6", "a", "1", "Two parallel metal plates X and Y are separated by a distance of 0.041 m, as shown in Fig. 6.1.\n[diagram]\nThere is a vacuum between the plates. An electron is at rest at the centre of plate X.\nA potential difference (p.d.) of 58 kV is applied across the plates. This causes the electron to accelerate towards plate Y.\nOn Fig. 6.1, use the symbols + and – to indicate which of plates X and Y is the positive plate and which is the negative plate.", "images/9702_s25_qp_42_fig6_1.png"],
    ["9702", "2025", "June", "4", "2", "6", "b(i)", "2", "Calculate the electric field strength E between the plates. Give a unit with your answer.", "NULL"],
    ["9702", "2025", "June", "4", "2", "6", "b(ii)", "2", "Determine the acceleration of the electron.", "NULL"],
    ["9702", "2025", "June", "4", "2", "6", "c(i)", "3", "Many electrons are now accelerated from rest from plate X to plate Y in Fig. 6.1. When the electrons hit plate Y, the absorption of their kinetic energies results in the emission of electromagnetic waves.\nShow that the minimum wavelength of these electromagnetic waves is 21 pm.", "NULL"],
    ["9702", "2025", "June", "4", "2", "6", "c(ii)", "1", "State the region of the electromagnetic spectrum that contains these waves.", "NULL"],
    ["9702", "2025", "June", "4", "2", "6", "c(iii)", "2", "Explain how these electromagnetic waves may be used to form images of internal body structures.", "NULL"],

    # Q7
    ["9702", "2025", "June", "4", "2", "7", "a", "1", "Fig. 7.1 shows a circuit containing a capacitor of capacitance C and a resistor of resistance R.\n[diagram]\nInitially, the switch is open and the potential difference (p.d.) across the capacitor is 12 V.\nThe switch is closed at time t = 0 and the capacitor discharges through the resistor.\nFig. 7.2 shows the variation of the charge Q on the capacitor with the p.d. VC across the capacitor as the capacitor discharges. Fig. 7.3 shows the variation of the current I in the resistor with the p.d. VR across the resistor as the capacitor discharges.\n[diagram]\nState the relationship between VC and VR.", "images/9702_s25_qp_42_fig7_1.png,images/9702_s25_qp_42_fig7_2.png,images/9702_s25_qp_42_fig7_3.png"],
    ["9702", "2025", "June", "4", "2", "7", "b(i)", "2", "Determine the capacitance C, in μF.", "NULL"],
    ["9702", "2025", "June", "4", "2", "7", "b(ii)", "2", "Determine the resistance R, in kΩ.", "NULL"],
    ["9702", "2025", "June", "4", "2", "7", "b(iii)", "2", "Determine the time constant τ of the circuit.", "NULL"],
    ["9702", "2025", "June", "4", "2", "7", "c", "3", "Use Fig. 7.2, Fig. 7.3 and your answer in (a) to explain why the variation of Q with t is exponential in nature.", "NULL"],

    # Q8
    ["9702", "2025", "June", "4", "2", "8", "a(i)", "1", "Fig. 8.1 shows a circuit that produces rectification of an alternating input voltage.\n[diagram]\nThe input voltage VIN is sinusoidal. The rectified output voltage VOUT is applied across resistor R.\nThe variation of VIN with time t has amplitude V0 and period T, as shown in Fig. 8.2.\n[diagram]\nThe root-mean-square (r.m.s.) value of VIN is 6.0 V.\nState the type of rectification produced by the circuit of Fig. 8.1.", "images/9702_s25_qp_42_fig8_1.png,images/9702_s25_qp_42_fig8_2.png"],
    ["9702", "2025", "June", "4", "2", "8", "a(ii)", "1", "Calculate V0.", "NULL"],
    ["9702", "2025", "June", "4", "2", "8", "b(i)", "2", "Resistor R has resistance 45 Ω. Assume that there is no p.d. across the diode when it is conducting.\nDetermine the peak power P0 in the resistor.", "NULL"],
    ["9702", "2025", "June", "4", "2", "8", "b(ii)", "3", "On Fig. 8.3, sketch the variation of the power P in the resistor with t between t = 0 and t = 2T.\n[diagram]", "images/9702_s25_qp_42_fig8_3.png"],
    ["9702", "2025", "June", "4", "2", "8", "b(iii)", "2", "Use the answer in (b)(ii) to explain why the mean power in the resistor is 1/4(P0).", "NULL"],
    ["9702", "2025", "June", "4", "2", "8", "b(iv)", "1", "Use the information in (b)(iii) to determine the r.m.s. value of VOUT.", "NULL"],

    # Q9
    ["9702", "2025", "June", "4", "2", "9", "a", "2", "State what is meant by the photoelectric effect.", "NULL"],
    ["9702", "2025", "June", "4", "2", "9", "b(i)", "3", "The photoelectric effect is investigated in two stages using the circuit shown in Fig. 9.1.\n[diagram]\nThe polished metal plate Y is illuminated with electromagnetic radiation of frequency f and constant power.\nIn stage 1 of the investigation, frequency f is set to a constant value of 2.5 × 1015 Hz. The current I in the ammeter is varied by adjusting the potentiometer P. Fig. 9.2 shows the variation of I with the voltmeter reading V. There is a value VS of V at which the current just falls to zero.\nIn stage 2 of the investigation, stage 1 is repeated for different values of frequency. As frequency f is varied, the voltmeter reading VS at which the current just falls to zero is measured. Fig. 9.3 shows the variation of VS with f.\n[diagram]\nExplain, with reference to photons, why VS depends on the frequency of the incident electromagnetic radiation.", "images/9702_s25_qp_42_fig9_1.png,images/9702_s25_qp_42_fig9_2.png,images/9702_s25_qp_42_fig9_3.png"],
    ["9702", "2025", "June", "4", "2", "9", "b(ii)", "3", "State three quantitative conclusions that can be drawn from the results in Fig. 9.2 and Fig. 9.3.", "NULL"],

    # Q10
    ["9702", "2025", "June", "4", "2", "10", "a", "1", "Radioactive decay is a spontaneous process. State the meaning, in this context, of the term spontaneous.", "NULL"],
    ["9702", "2025", "June", "4", "2", "10", "b(i)", "3", "Two radioactive isotopes X and Y each decay to form a stable isotope.\nA sample initially contains only atoms of isotope X. At this time, its activity is 4A.\nAnother sample initially contains only atoms of Y. At this time, its activity is A.\nFig. 10.1 shows the variation of the activity of each sample with time t between t = 0 and t = 6T.\n[diagram]\nComplete Table 10.1 to give expressions, in terms of either or both of A and T, for the quantities indicated for each of the samples.", "images/9702_s25_qp_42_fig10_1.png"],
    ["9702", "2025", "June", "4", "2", "10", "b(ii)", "3", "Determine, in terms of T, the time at which the two samples will have equal activities.", "NULL"],
    ["9702", "2025", "June", "4", "2", "10", "c", "2", "A radiation detector is placed near to one of the samples in (b).\nExplain why the count rate measured by the detector is less than the activity of the sample.", "NULL"]
]

with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in qs:
        writer.writerow(row)

print("s25_qp42 added.")

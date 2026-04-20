import csv

ms = [
    # Q1
    ["9702", "2025", "June", "4", "2", "1", "a", "1", "1", "angle (subtended at centre of a circle) when arc (length) = radius"],
    ["9702", "2025", "June", "4", "2", "1", "b(i)", "1", "1", "v = rω"],
    ["9702", "2025", "June", "4", "2", "1", "b(i)", "2", "1", "ω = 17 / 0.46 = 37 rad s–1"],
    ["9702", "2025", "June", "4", "2", "1", "b(ii)", "1", "1", "T = 2πr / v or T = 2π / ω"],
    ["9702", "2025", "June", "4", "2", "1", "b(ii)", "2", "1", "= 2π × 0.46 / 17 or 2π / 37 = 0.17 s"],
    ["9702", "2025", "June", "4", "2", "1", "b(iii)", "1", "1", "distance = 2π × 0.038 = 0.24 m"],
    ["9702", "2025", "June", "4", "2", "1", "b(iv)", "1", "1", "angle = arc length / radius = 0.24 / 0.15"],
    ["9702", "2025", "June", "4", "2", "1", "b(iv)", "2", "1", "= 1.6 rad"],
    ["9702", "2025", "June", "4", "2", "1", "c", "1", "1", "point X moves through a smaller distance in the same time or (linear) speed of movement of point X / chain decreases"],
    ["9702", "2025", "June", "4", "2", "1", "c", "2", "1", "angular speed (of pedals) decreases"],

    # Q2
    ["9702", "2025", "June", "4", "2", "2", "a(i)", "1", "1", "direction of force"],
    ["9702", "2025", "June", "4", "2", "2", "a(i)", "2", "1", "force acting on a (test) mass"],
    ["9702", "2025", "June", "4", "2", "2", "a(ii)", "1", "1", "at least four radial lines from the Earth’s surface, equally spaced around the surface"],
    ["9702", "2025", "June", "4", "2", "2", "a(ii)", "2", "1", "arrows indicating direction towards Earth"],
    ["9702", "2025", "June", "4", "2", "2", "b(i)", "1", "1", "top pole labelled S and bottom pole labelled N"],
    ["9702", "2025", "June", "4", "2", "2", "b(ii)", "1", "1", "at least two field lines either side of both poles, leaving perpendicularly and curving away"],
    ["9702", "2025", "June", "4", "2", "2", "b(ii)", "2", "1", "at least one field line connecting two points on the surface via the magnetic equator, approximately parallel"],
    ["9702", "2025", "June", "4", "2", "2", "c(i)", "1", "1", "(around the surface) lines are evenly spaced"],
    ["9702", "2025", "June", "4", "2", "2", "c(i)", "2", "1", "all lines perpendicular to surface or pointing down towards surface (at all points)"],
    ["9702", "2025", "June", "4", "2", "2", "c(ii)", "1", "1", "strongest at the poles and weakest near the Equator"],
    ["9702", "2025", "June", "4", "2", "2", "c(ii)", "2", "1", "perpendicular to surface at the poles, parallel to surface near Equator"],
    ["9702", "2025", "June", "4", "2", "2", "c(ii)", "3", "1", "angle to surface increases from Equator to poles"],

    # Q3
    ["9702", "2025", "June", "4", "2", "3", "a", "1", "1", "(thermal) energy per unit mass (to cause temperature change)"],
    ["9702", "2025", "June", "4", "2", "3", "a", "2", "1", "(thermal) energy per unit change in temperature"],
    ["9702", "2025", "June", "4", "2", "3", "b(i)", "1", "1", "density = mass / volume so mass = 2.700 × 10^3 × 3.612 × 10^-3"],
    ["9702", "2025", "June", "4", "2", "3", "b(i)", "2", "1", "= 9.752 kg"],
    ["9702", "2025", "June", "4", "2", "3", "b(ii)", "1", "1", "volume = 9.752 / (2.620 × 10^3) = 3.722 × 10^-3 m^3"],
    ["9702", "2025", "June", "4", "2", "3", "b(iii)", "1", "1", "W = pΔV = 1.01 × 10^5 × (3.722 – 3.612) × 10^-3"],
    ["9702", "2025", "June", "4", "2", "3", "b(iii)", "2", "1", "= 11.1 J"],
    ["9702", "2025", "June", "4", "2", "3", "b(iv)", "1", "1", "volume (of block) increases"],
    ["9702", "2025", "June", "4", "2", "3", "b(iv)", "2", "1", "work is done against the atmosphere so work done (on block) is negative"],
    ["9702", "2025", "June", "4", "2", "3", "b(v)", "1", "1", "thermal energy = (4.38 × 10^6) + 11.1"],
    ["9702", "2025", "June", "4", "2", "3", "b(v)", "2", "1", "specific heat capacity = (4.38 × 10^6) / (9.75 × 500)"],
    ["9702", "2025", "June", "4", "2", "3", "b(v)", "3", "1", "= 898 J kg-1 °C-1"],
    ["9702", "2025", "June", "4", "2", "3", "c", "1", "1", "work done is negligible compared with (change in) internal energy so unchanged"],

    # Q4
    ["9702", "2025", "June", "4", "2", "4", "a(i)", "1", "1", "thermodynamic temperature"],
    ["9702", "2025", "June", "4", "2", "4", "a(ii)", "1", "1", "molar gas constant"],
    ["9702", "2025", "June", "4", "2", "4", "b(i)", "1", "1", "m: mass of one molecule (of the gas)"],
    ["9702", "2025", "June", "4", "2", "4", "b(i)", "2", "1", "〈c2〉: mean-square speed (of molecules)"],
    ["9702", "2025", "June", "4", "2", "4", "b(ii)", "1", "1", "NBT / A = 1/3 Nm〈c2〉"],
    ["9702", "2025", "June", "4", "2", "4", "b(ii)", "2", "1", "clear use of EK = 1/2 m〈c2〉 leading to EK = 3BT / 2A"],
    ["9702", "2025", "June", "4", "2", "4", "c", "1", "1", "line with positive gradient passing through the origin"],
    ["9702", "2025", "June", "4", "2", "4", "c", "2", "1", "smooth curve with decreasing positive gradient"],

    # Q5
    ["9702", "2025", "June", "4", "2", "5", "a", "1", "1", "(motion in which) acceleration is (directly) proportional to displacement"],
    ["9702", "2025", "June", "4", "2", "5", "a", "2", "1", "acceleration is (always) in the opposite direction to displacement / towards fixed point"],
    ["9702", "2025", "June", "4", "2", "5", "b(i)", "1", "1", "period = 2π / 16 = 0.39 s"],
    ["9702", "2025", "June", "4", "2", "5", "b(ii)", "1", "1", "v0 = ωx0 -> x0 = 0.56 / 16"],
    ["9702", "2025", "June", "4", "2", "5", "b(ii)", "2", "1", "= 0.035 m"],
    ["9702", "2025", "June", "4", "2", "5", "b(iii)", "1", "1", "v = ±16 √(0.035^2 - x^2)"],
    ["9702", "2025", "June", "4", "2", "5", "b(iv)", "1", "1", "closed loop surrounding the origin"],
    ["9702", "2025", "June", "4", "2", "5", "b(iv)", "2", "1", "loop crosses v = 0 at maximum values of x at ± 3.5 cm"],
    ["9702", "2025", "June", "4", "2", "5", "b(iv)", "3", "1", "loop crosses x = 0 at maximum values of v at ± 0.56 m s-1"],

    # Q6
    ["9702", "2025", "June", "4", "2", "6", "a", "1", "1", "plate X marked as negative and plate Y marked as positive"],
    ["9702", "2025", "June", "4", "2", "6", "b(i)", "1", "1", "E = V / x = (58 × 10^3) / 0.041"],
    ["9702", "2025", "June", "4", "2", "6", "b(i)", "2", "1", "= 1.4 × 10^6 N C-1"],
    ["9702", "2025", "June", "4", "2", "6", "b(ii)", "1", "1", "ma = eE -> a = (1.60 × 10^-19 × 1.41 × 10^6) / (9.11 × 10^-31)"],
    ["9702", "2025", "June", "4", "2", "6", "b(ii)", "2", "1", "= 2.5 × 10^17 m s-2"],
    ["9702", "2025", "June", "4", "2", "6", "c(i)", "1", "1", "eV = hc/λ or eV = hf and f = c/λ"],
    ["9702", "2025", "June", "4", "2", "6", "c(i)", "2", "1", "(1.60 × 10^-19 × 58 × 10^3) = (6.63 × 10^-34 × 3.00 × 10^8) / λ"],
    ["9702", "2025", "June", "4", "2", "6", "c(i)", "3", "1", "clear conversion from m to pm leading to λ = 21 pm"],
    ["9702", "2025", "June", "4", "2", "6", "c(ii)", "1", "1", "X-rays"],
    ["9702", "2025", "June", "4", "2", "6", "c(iii)", "1", "1", "waves are passed into structure and transmitted waves detected / different parts absorb different fractions"],
    ["9702", "2025", "June", "4", "2", "6", "c(iii)", "2", "1", "difference in detected/transmitted intensities used (to form image)"],

    # Q7
    ["9702", "2025", "June", "4", "2", "7", "a", "1", "1", "VC = VR"],
    ["9702", "2025", "June", "4", "2", "7", "b(i)", "1", "1", "C = Q / V = (7.2 × 10^-3) / 12"],
    ["9702", "2025", "June", "4", "2", "7", "b(i)", "2", "1", "= 600 μF"],
    ["9702", "2025", "June", "4", "2", "7", "b(ii)", "1", "1", "R = V / I = 12 / (1.5 × 10^-3)"],
    ["9702", "2025", "June", "4", "2", "7", "b(ii)", "2", "1", "= 8.0 kΩ"],
    ["9702", "2025", "June", "4", "2", "7", "b(iii)", "1", "1", "τ = RC = 8000 × 6.0 × 10^-4"],
    ["9702", "2025", "June", "4", "2", "7", "b(iii)", "2", "1", "= 4.8 s"],
    ["9702", "2025", "June", "4", "2", "7", "c", "1", "1", "charge and current both proportional to voltage, and current is rate of change of charge"],
    ["9702", "2025", "June", "4", "2", "7", "c", "2", "1", "charge is directly proportional to current"],
    ["9702", "2025", "June", "4", "2", "7", "c", "3", "1", "Q is proportional to the rate of change of Q (so exponential variation)"],

    # Q8
    ["9702", "2025", "June", "4", "2", "8", "a(i)", "1", "1", "half-wave (rectification)"],
    ["9702", "2025", "June", "4", "2", "8", "a(ii)", "1", "1", "V0 = 6.0 × √2 = 8.5 V"],
    ["9702", "2025", "June", "4", "2", "8", "b(i)", "1", "1", "P = V^2 / R so P0 = 8.5^2 / 45"],
    ["9702", "2025", "June", "4", "2", "8", "b(i)", "2", "1", "= 1.6 W"],
    ["9702", "2025", "June", "4", "2", "8", "b(ii)", "1", "1", "two humps of width 0.5T and two sections of zero power of width 0.5T"],
    ["9702", "2025", "June", "4", "2", "8", "b(ii)", "2", "1", "all humps drawn have width 0.5T, minima at P = 0 and peaks at P = P0"],
    ["9702", "2025", "June", "4", "2", "8", "b(ii)", "3", "1", "correct sinusoidal shape, smooth troughs sitting on t-axis"],
    ["9702", "2025", "June", "4", "2", "8", "b(iii)", "1", "1", "mean power within each hump is 1/2 P0 from symmetry of curve"],
    ["9702", "2025", "June", "4", "2", "8", "b(iii)", "2", "1", "additional half factor from removal of half of the power in each cycle"],
    ["9702", "2025", "June", "4", "2", "8", "b(iv)", "1", "1", "〈P〉 = Vr.m.s.^2 / R -> Vr.m.s. = √[(1.6 / 4) × 45] = 4.2 V"],

    # Q9
    ["9702", "2025", "June", "4", "2", "9", "a", "1", "1", "emission of electrons (from a metal surface)"],
    ["9702", "2025", "June", "4", "2", "9", "a", "2", "1", "when electromagnetic radiation is incident (on surface)"],
    ["9702", "2025", "June", "4", "2", "9", "b(i)", "1", "1", "current falls to zero when applied voltage equals energy per unit charge of emitted electrons"],
    ["9702", "2025", "June", "4", "2", "9", "b(i)", "2", "1", "energy of photon depends on frequency"],
    ["9702", "2025", "June", "4", "2", "9", "b(i)", "3", "1", "maximum energy of electron depends on energy of photon"],
    ["9702", "2025", "June", "4", "2", "9", "b(ii)", "1", "1", "threshold frequency = 1.5 × 10^15 Hz"],
    ["9702", "2025", "June", "4", "2", "9", "b(ii)", "2", "1", "threshold wavelength = 2.0 × 10^-7 m or work function = 6.2 eV"],
    ["9702", "2025", "June", "4", "2", "9", "b(ii)", "3", "1", "Planck constant = 6.6 × 10^-34 J s or number per unit time = 1.7 × 10^16 s^-1"],

    # Q10
    ["9702", "2025", "June", "4", "2", "10", "a", "1", "1", "(decay is) not affected by external / environmental factors"],
    ["9702", "2025", "June", "4", "2", "10", "b(i)", "1", "1", "half-life of X = 2T and half-life of Y = 3T"],
    ["9702", "2025", "June", "4", "2", "10", "b(i)", "2", "1", "both samples show decay constant equal to ln 2 / half-life (X = ln2/2T, Y = ln2/3T)"],
    ["9702", "2025", "June", "4", "2", "10", "b(i)", "3", "1", "both samples show N0 equal to initial activity / decay constant (N0 for X = 8AT/ln2, Y = 3AT/ln2)"],
    ["9702", "2025", "June", "4", "2", "10", "b(ii)", "1", "1", "correct substitution into A0 exp(–λt)"],
    ["9702", "2025", "June", "4", "2", "10", "b(ii)", "2", "1", "4A exp(–t ln 2 / 2T) = A exp(–t ln 2 / 3T)"],
    ["9702", "2025", "June", "4", "2", "10", "b(ii)", "3", "1", "t = 12T"],
    ["9702", "2025", "June", "4", "2", "10", "c", "1", "1", "(radiation) emitted in all directions, not just in direction of detector"],
    ["9702", "2025", "June", "4", "2", "10", "c", "2", "1", "some radiation absorbed by air/sample/window or some may not register even though it reaches detector"]
]

with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for m in ms:
        writer.writerow(m)

print("s25_ms42 added.")

import csv

q_rows = [
    # Question 7
    ["9702", "2025", "March", "4", "2", "7", "NULL", "9", "Electromagnetic Induction", "NULL"],
    ["9702", "2025", "March", "4", "2", "7", "a", "2", "State Faraday’s law of electromagnetic induction.", "NULL"],
    ["9702", "2025", "March", "4", "2", "7", "b(i)", "2", "A metal rod is accelerated uniformly from rest in a uniform magnetic field as shown in Fig. 7.1.\n[diagram]\nThe rod has length l and the flux density of the magnetic field is B.\nAn electromotive force (e.m.f.) is induced in the rod. The variation with time t of the induced e.m.f. E is shown in Fig. 7.2.\n[diagram]\nExplain how Fig. 7.2 shows that E is proportional to the velocity v of the rod.", "images/9702_m25_qp_42_fig7_1.png"],
    ["9702", "2025", "March", "4", "2", "7", "b(ii)", "3", "Use Faraday’s law to show that the variation of E with time t is given by E = Blat where a is the acceleration of the rod.", "NULL"],
    ["9702", "2025", "March", "4", "2", "7", "b(iii)", "2", "The length of the rod is 0.45 m. The acceleration a of the rod is 7.8 m s^-2.\nDetermine the value of B.", "NULL"],

    # Question 8
    ["9702", "2025", "March", "4", "2", "8", "NULL", "10", "Quantum Physics", "NULL"],
    ["9702", "2025", "March", "4", "2", "8", "a", "2", "State what is meant by a photon.", "NULL"],
    ["9702", "2025", "March", "4", "2", "8", "b(i)", "3", "A laser emits red light of a single wavelength. The light is produced when electrons move from a higher energy level to a lower energy level. The difference in energy between the two levels is 1.96 eV.\nCalculate the wavelength of the light.", "NULL"],
    ["9702", "2025", "March", "4", "2", "8", "b(ii)", "1", "The power of the beam emitted by the laser is 1.0 × 10^-2 W.\nCalculate the number of photons emitted per unit time by the laser.", "NULL"],
    ["9702", "2025", "March", "4", "2", "8", "b(iii)", "4", "The photons are incident normally on a surface. Half of the number of photons are absorbed by the surface, and half are reflected.\nDetermine the average force exerted by the beam of photons on the surface.", "NULL"],

    # Question 9
    ["9702", "2025", "March", "4", "2", "9", "NULL", "10", "Nuclear Physics", "NULL"],
    ["9702", "2025", "March", "4", "2", "9", "a(i)", "1", "Polonium-193 (193/84 Po) is an unstable nuclide. A nucleus of polonium-193 decays to a nucleus of lead-189 (189/82 Pb) by emitting an alpha-particle.\nRadioactive decay is both random and spontaneous.\nState what is meant by: random", "NULL"],
    ["9702", "2025", "March", "4", "2", "9", "a(ii)", "1", "State what is meant by: spontaneous.", "NULL"],
    ["9702", "2025", "March", "4", "2", "9", "b", "1", "Define half-life.", "NULL"],
    ["9702", "2025", "March", "4", "2", "9", "c", "2", "Data for the binding energy per nucleon of the particles involved in the decay of a nucleus of polonium-193 are given in Table 9.1.\n[diagram]\nDetermine the energy, in eV, released when a nucleus of polonium-193 decays into a nucleus of lead-189.", "images/9702_m25_qp_42_table9_1.png"],
    ["9702", "2025", "March", "4", "2", "9", "d(i)", "1", "A pure sample of polonium-193 contains N0 nuclei. After a time t the sample contains N nuclei of polonium-193. The variation of ln (N / N0) with t is shown in Fig. 9.1.\n[diagram]\nState the name of the quantity that is represented by the magnitude of the gradient of the line in Fig. 9.1.", "images/9702_m25_qp_42_fig9_1.png"],
    ["9702", "2025", "March", "4", "2", "9", "d(ii)", "2", "Use Fig. 9.1 to determine the half-life, in ms, of polonium-193.", "NULL"],
    ["9702", "2025", "March", "4", "2", "9", "e(i)", "1", "Positron emission tomography (PET scanning) uses a radioactive tracer.\nState what happens to the positrons emitted by the tracer.", "NULL"],
    ["9702", "2025", "March", "4", "2", "9", "e(ii)", "1", "Explain why a tracer with a half-life of approximately 2 hours is a suitable tracer to use.", "NULL"],

    # Question 10
    ["9702", "2025", "March", "4", "2", "10", "NULL", "11", "Astrophysics", "NULL"],
    ["9702", "2025", "March", "4", "2", "10", "a(i)", "1", "State what is meant by the luminosity of a star.", "NULL"],
    ["9702", "2025", "March", "4", "2", "10", "a(ii)", "3", "Explain how standard candles are used to determine the distance to a galaxy.", "NULL"],
    ["9702", "2025", "March", "4", "2", "10", "b(i)", "3", "The Sun rotates on its axis. Points X, Y and Z are on the equator of the Sun as shown in Fig. 10.1.\n[diagram]\nThe wavelengths of light from points X and Y are observed and recorded in Table 10.1.\n[diagram]\nThe Sun rotates with a period of 2.07 × 10^6 s.\nShow that the radius of the Sun is 6.93 × 10^8 m.", "images/9702_m25_qp_42_fig10_1.png"],
    ["9702", "2025", "March", "4", "2", "10", "b(ii)", "2", "State and explain how the expected wavelength of the light observed from Z compares with the emitted wavelength.", "NULL"],
    ["9702", "2025", "March", "4", "2", "10", "b(iii)", "2", "The luminosity of the Sun is 3.8 × 10^26 W.\nUse the information in (b)(i) to calculate the surface temperature of the Sun.", "NULL"]
]

ms_rows = [
    # Q7
    ["9702", "2025", "March", "4", "2", "7", "a", "1", "1", "(induced) e.m.f is proportional to"],
    ["9702", "2025", "March", "4", "2", "7", "a", "2", "1", "rate of change of (magnetic) flux (linkage)"],
    ["9702", "2025", "March", "4", "2", "7", "b(i)", "1", "1", "(line is straight so) E is proportional to t"],
    ["9702", "2025", "March", "4", "2", "7", "b(i)", "2", "1", "(uniform acceleration so v = at, meaning) v is proportional to t (so E proportional to v)"],
    ["9702", "2025", "March", "4", "2", "7", "b(ii)", "1", "1", "Δ(magnetic flux) = ΔA × B or B × l × Δs/Δt"],
    ["9702", "2025", "March", "4", "2", "7", "b(ii)", "2", "1", "E = rate of change of magnetic flux = (B × l × s)/t or = B × l × v"],
    ["9702", "2025", "March", "4", "2", "7", "b(ii)", "3", "1", "v = at so E = B × l × a × t"],
    ["9702", "2025", "March", "4", "2", "7", "b(iii)", "1", "1", "gradient is B × l × a"],
    ["9702", "2025", "March", "4", "2", "7", "b(iii)", "2", "1", "either: B = 100 × 10^-3 / (0.45 × 7.8) or: B = (100 × 10^-3 × 1) / (0.45 × 7.8 × 1) = 0.028 T (0.0285 T)"],

    # Q8
    ["9702", "2025", "March", "4", "2", "8", "a", "1", "1", "quantum / packet of energy"],
    ["9702", "2025", "March", "4", "2", "8", "a", "2", "1", "of electromagnetic radiation"],
    ["9702", "2025", "March", "4", "2", "8", "b(i)", "1", "1", "E = hc / λ or E = hf and c = fλ"],
    ["9702", "2025", "March", "4", "2", "8", "b(i)", "2", "1", "1.96 × 1.6 × 10^-19 = (6.63 × 10^-34 × 3.0 × 10^8) / λ"],
    ["9702", "2025", "March", "4", "2", "8", "b(i)", "3", "1", "λ = 6.3 × 10^-7 m"],
    ["9702", "2025", "March", "4", "2", "8", "b(ii)", "1", "1", "number = 1.0 × 10^-2 / (1.96 × 1.6 × 10^-19) = 3.2 × 10^16 s^-1"],
    ["9702", "2025", "March", "4", "2", "8", "b(iii)", "1", "1", "Δp = p (for absorbed photon) and Δp = 2p (for reflected photon)"],
    ["9702", "2025", "March", "4", "2", "8", "b(iii)", "2", "1", "(average) force = (0.5 N × p) + (0.5 N × 2p) = 1.5 Np"],
    ["9702", "2025", "March", "4", "2", "8", "b(iii)", "3", "1", "p = h/λ = 6.63 × 10^-34 / 6.3 × 10^-7 (= 1.05 × 10^-27)"],
    ["9702", "2025", "March", "4", "2", "8", "b(iii)", "4", "1", "force = 1.5 × 3.2 × 10^16 × 1.05 × 10^-27 = 5.0 × 10^-11 N"],

    # Q9
    ["9702", "2025", "March", "4", "2", "9", "a(i)", "1", "1", "cannot state when nucleus will decay or which nucleus will decay (next)"],
    ["9702", "2025", "March", "4", "2", "9", "a(ii)", "1", "1", "(decay is) unaffected by external (environmental) factors / constant probability of decay"],
    ["9702", "2025", "March", "4", "2", "9", "b", "1", "1", "time for number of atoms / nuclei / activity (of an isotope) to halve"],
    ["9702", "2025", "March", "4", "2", "9", "c", "1", "1", "energy = [(189 × 7.826) + (4 × 7.074)] - (193 × 7.774)"],
    ["9702", "2025", "March", "4", "2", "9", "c", "2", "1", "= 5.4 MeV = 5.4 × 10^6 eV"],
    ["9702", "2025", "March", "4", "2", "9", "d(i)", "1", "1", "decay constant"],
    ["9702", "2025", "March", "4", "2", "9", "d(ii)", "1", "1", "either: λ = (-)-0.6 / 0.5 (= 1.2 ms^-1) or: λ = (-)-1.2 / 1.0 (= 1.2 ms^-1)"],
    ["9702", "2025", "March", "4", "2", "9", "d(ii)", "2", "1", "half-life = ln(2) / 1.2 = 0.58 ms"],
    ["9702", "2025", "March", "4", "2", "9", "e(i)", "1", "1", "interact with electron and annihilate"],
    ["9702", "2025", "March", "4", "2", "9", "e(ii)", "1", "1", "long enough for tracer to be produced / travel to hospital / move through body AND short enough so limit exposure of patient"],

    # Q10
    ["9702", "2025", "March", "4", "2", "10", "a(i)", "1", "1", "total power of radiation emitted"],
    ["9702", "2025", "March", "4", "2", "10", "a(ii)", "1", "1", "standard candle is object of known luminosity"],
    ["9702", "2025", "March", "4", "2", "10", "a(ii)", "2", "1", "flux / intensity (from standard candle) assessed"],
    ["9702", "2025", "March", "4", "2", "10", "a(ii)", "3", "1", "either: use F = L / 4πd^2 where F is flux and L is luminosity or: use I = P / 4πd^2 where I is intensity and P is power"],
    ["9702", "2025", "March", "4", "2", "10", "b(i)", "1", "1", "v = c × (Δλ/λ)"],
    ["9702", "2025", "March", "4", "2", "10", "b(i)", "2", "1", "Δλ = [0.5 × (656.2877 - 656.2831)] or: Δλ = [656.2877 - 656.2854]"],
    ["9702", "2025", "March", "4", "2", "10", "b(i)", "3", "1", "either: v = 3.0 × 10^8 × (0.0023 / 656.285) = 1.05 × 10^3 m s^-1 and r = vT / 2π = ... = 6.91 × 10^8 m or: r = c × Δλ × T / (2π × λ) = 6.91 × 10^8 m"],
    ["9702", "2025", "March", "4", "2", "10", "b(ii)", "1", "1", "expected wavelength is 656.2854 nm (from (b)(i))"],
    ["9702", "2025", "March", "4", "2", "10", "b(ii)", "2", "1", "Z is moving perpendicularly to line of sight (so no Doppler effect)"],
    ["9702", "2025", "March", "4", "2", "10", "b(iii)", "1", "1", "L = 4π r^2 σ T^4"],
    ["9702", "2025", "March", "4", "2", "10", "b(iii)", "2", "1", "T = [3.8 × 10^26 / (4π × (6.93 × 10^8)^2 × 5.67 × 10^-8)]^0.25 = 5500 K"]
]

with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in q_rows:
        writer.writerow(row)

with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in ms_rows:
        writer.writerow(row)


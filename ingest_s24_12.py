import csv
import os

def append_row(filename, row):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# 1. papers.csv
# subject_code,year,session,paper_number,variant,duration,total_marks
append_row('data/papers.csv', ["9702", "2024", "Summer", "1", "2", "01:15", "40"])

# 2. grade_boundaries.csv
# Component 12 Max 40: A: 30, B: 26, C: 22, D: 19, E: 15
gb_data = [
    ["9702", "2024", "Summer", "1", "2", "A", "30"],
    ["9702", "2024", "Summer", "1", "2", "B", "26"],
    ["9702", "2024", "Summer", "1", "2", "C", "22"],
    ["9702", "2024", "Summer", "1", "2", "D", "19"],
    ["9702", "2024", "Summer", "1", "2", "E", "15"]
]
for row in gb_data:
    append_row('data/grade_boundaries.csv', row)

# 3. examiner_comments.csv
append_row('data/examiner_comments.csv', ["9702", "2024", "Summer", "1", "2", "NULL", "NULL", "The paper tested a representative range of the AS syllabus. Candidates demonstrated strong recall of fundamental definitions and proficiency in standard calculations. Performance was strongest on mechanics and circuit analysis."])

# 4. questions.csv & markpoints.csv
keys = [
    "C", "D", "A", "D", "B", 
    "B", "C", "A", "C", "A", 
    "B", "C", "D", "C", "D", 
    "A", "B", "C", "C", "D", 
    "C", "D", "B", "B", "C", 
    "A", "D", "D", "A", "C", 
    "D", "C", "B", "A", "D", 
    "A", "B", "D", "C", "C"
]

diagram_qs = [5, 6, 10, 11, 12, 15, 18, 19, 20, 21, 23, 26, 31, 35, 36]

questions_data = [
    "Which quantity is a scalar?",
    "Density of a solid sphere mass M and diameter d. Which expression is correct?",
    "Velocity vs time graph for falling object. Terminal velocity point?",
    "Percentage uncertainty in kinetic energy calculation.",
    "Ball falling with air resistance. Which statement about acceleration is correct?",
    "Force vs time graph for collision. Average force?",
    "Elastic collision between two spheres. Which property is conserved?",
    "Density calculation for a cube.",
    "Two forces in equilibrium. Resultant moment about point P?",
    "Beam in equilibrium on two supports. Force calculation.",
    "Diagram showing forces on a kite. Resultant force?",
    "Hydrostatic pressure calculation in two liquids.",
    "Efficiency calculation for a motor lifting a load.",
    "Work done per unit time definition?",
    "Mass-spring system extensions.",
    "Young modulus calculation for a wire.",
    "Stress-strain graph regions and Hooke's law.",
    "Progressive transverse wave. Phase difference between points?",
    "Sound wave intensity vs distance.",
    "Doppler effect calculation for a moving source.",
    "Electromagnetic wave spectrum regions.",
    "Polarisation of electromagnetic waves.",
    "Stationary wave on a string. Node positions?",
    "Diffraction of waves through a slit.",
    "Interference pattern from two sources.",
    "Diffraction grating wavelength calculation.",
    "Cathode-ray oscilloscope settings.",
    "What is the definition of current?",
    "Charge carrier drift speed in a wire.",
    "Potential difference across a parallel combination of resistors.",
    "Kirchhoff's first law application to a junction.",
    "Resistance of a thermistor from graph.",
    "Internal resistance of a battery.",
    "Potentiometer circuit balance length.",
    "Combined resistance of three resistors.",
    "Electricity circuit Kirchhoff's second law loop.",
    "Which particle is a baryon?",
    "Quark composition of a neutron.",
    "Weak interaction decay particle emitted.",
    "Beta-minus decay nucleus change."
]

for i in range(40):
    q_num = i + 1
    diag = f"images/9702_s24_12_qp_fig{q_num}.png" if q_num in diagram_qs else "NULL"
    text = questions_data[i]
    key = keys[i]
    
    append_row('data/questions.csv', ["9702", "2024", "Summer", "1", "2", str(q_num), "NULL", "1", text, diag])
    append_row('data/markpoints.csv', ["9702", "2024", "Summer", "1", "2", str(q_num), "NULL", "1", key, "1", "A"])

print(f"Ingested 40 MCQs for s24 12.")

import csv

# Add to papers.csv
with open(r"data\papers.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "June", "4", "2"])

# Add to grade_boundaries.csv
with open(r"data\grade_boundaries.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 60 50 41 32 22
    writer.writerow(["9702", "2025", "June", "4", "2", "100", "60", "50", "41", "32", "22"])

# Examiner Comments from s25_er.txt
ec_rows = [
    ["9702", "2025", "June", "4", "2", "NULL", "This paper tested complex A Level topics including Simple Harmonic Motion and Quantum Physics. Calculations involving astronomical units and nuclear decay ratios were generally well-executed, though drawing field lines for Earth’s magnetic field required more precision."],
    ["9702", "2025", "June", "4", "2", "1", "Candidates calculated the angular speed of the rear wheel as 37 rad s-1. For the large cog, the distance moved by the chain provided the arc length (0.24 m), leading to an angle of 1.6 rad."],
    ["9702", "2025", "June", "4", "2", "3", "Explaining the sign of work done was key. As the volume increased, work was done against the atmosphere, making it negative. The final specific heat capacity of aluminium was determined to be 898 J kg-1 °C-1."],
    ["9702", "2025", "June", "4", "2", "9", "From the VS against f graph, candidates extracted values for the threshold frequency (1.5×10^15 Hz) and calculated the work function (6.2 eV)."],
    ["9702", "2025", "June", "4", "2", "10", "Candidates used the activities AX = 4A e^−λXt and AY = A e^−λYt with their respective half-lives (2T and 3T). Setting the expressions equal and solving for t yielded 12T."]
]

with open(r"data\examiner_comments.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ec_rows:
        writer.writerow(row)

print("GT and EC added for P42.")

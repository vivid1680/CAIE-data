import csv

# Add to papers.csv
with open(r"data\papers.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "June", "2", "2"])

# Add to grade_boundaries.csv
with open(r"data\grade_boundaries.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # A=43, B=37, C=30, D=24, E=16
    writer.writerow(["9702", "2025", "June", "2", "2", "60", "43", "37", "30", "24", "16"])

# Examiner Comments from s25_er.txt
ec_rows = [
    ["9702", "2025", "June", "2", "2", "NULL", "The paper provided a balanced mix of descriptive and calculative tasks. Most candidates showed a good grasp of Kirchhoff’s laws and vector representations. Performance was lower in questions requiring the formal derivation of the kinetic energy formula."],
    ["9702", "2025", "June", "2", "2", "1", "Candidates were required to show EK = 1/2 mv2 using work done. Stronger responses correctly started with W=Fs and substituted F=ma and v2 = u2 + 2as."],
    ["9702", "2025", "June", "2", "2", "4", "In calculating the change in momentum for a bouncing ball, many candidates forgot that momentum is a vector. The change is m(v−(−u)), leading to 2.2 kg m s-1."],
    ["9702", "2025", "June", "2", "2", "6", "This was a demanding task involving a potential divider with a parallel branch. Successful candidates calculated the current in the top branch (0.018 A) and used the remaining potential difference to find R = 230 Ω."]
]

with open(r"data\examiner_comments.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ec_rows:
        writer.writerow(row)

print("GT and EC added.")

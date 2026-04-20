import csv

ec_rows = [
    ["9702", "2025", "June", "1", "2", "NULL", "The paper tested a wide range of AS topics. Candidates performed well on standard kinetic and energy calculations, though unit conversions in multi-prefix quantities and specific interpretations of wave graphs proved more challenging."],
    ["9702", "2025", "June", "1", "2", "2", "Candidates had to convert 0.25 kN mm^-2 to N m^-2. Many failed to account for the squared millimeter conversion (1 mm^2 = 10^-6 m^2), which led to the selection of C instead of the correct answer D (2.5 × 10^8 N m^-2)."],
    ["9702", "2025", "June", "1", "2", "6", "This question required interpreting a velocity-time graph. Correct analysis of the area under the graph for the first 4 seconds (12×2 + 0.5×12×2 = 36 m) identified C as the correct statement."],
    ["9702", "2025", "June", "1", "2", "24", "Candidates were asked for the frequency of microwaves based on melted chocolate spots at antinodes. Recognizing that the distance between two adjacent antinodes is λ/2 (6.0 cm) was essential. Using v=fλ, the frequency was calculated as 2.5 GHz (Key C)."]
]

with open(r"data\examiner_comments.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ec_rows:
        writer.writerow(row)

print("Examiner comments added.")

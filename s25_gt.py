import csv

# Add to papers.csv
with open(r"data\papers.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "June", "1", "2"])

# Add to grade_boundaries.csv
with open(r"data\grade_boundaries.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "June", "1", "2", "40", "30", "26", "22", "18", "15"])

print("GT and Paper metadata added.")

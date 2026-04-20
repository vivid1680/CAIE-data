import csv
import os

answers = [
    "D", "D", "C", "A", "A", "C", "B", "B", "A", "A",
    "C", "D", "D", "A", "B", "A", "B", "A", "D", "D",
    "B", "A", "D", "C", "B", "A", "C", "C", "C", "D",
    "C", "A", "C", "B", "C", "B", "B", "B", "D", "D"
]

ms_path = r"data\markpoints.csv"
with open(ms_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for i, ans in enumerate(answers):
        # subject_code,year,session,paper_number,variant,question_number,label,point_number,description,marks,type
        writer.writerow(["9702", "2025", "March", "1", "2", str(i+1), "NULL", "1", ans, "1", "Answer"])

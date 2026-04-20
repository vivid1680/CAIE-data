import csv
import re
import os

# Metadata Arrays
diagram_qs = [2, 3, 6, 8, 12, 13, 14, 17, 18, 23, 25, 29, 31, 33, 35, 38]

border_rows = [
    ["9702", "2024", "March", "1", "2"]
]

bounds_rows = [
    ["9702", "2024", "March", "1", "2", "40", "32", "29", "25", "21", "18"]
]

ec_rows = [
    ["9702", "2024", "March", "1", "2", "NULL", "In general, candidates scored well on definitions, but struggled with graphical kinematics and circuit ratio calculations."],
    ["9702", "2024", "March", "1", "2", "4", "Most candidates analyzed the resultant force correctly."],
    ["9702", "2024", "March", "1", "2", "6", "Many candidates confused total displacement with distance travelled on the velocity-time graph."],
    ["9702", "2024", "March", "1", "2", "7", "This definition was well known by almost all candidates."],
    ["9702", "2024", "March", "1", "2", "9", "A common error was forgetting to take the square root when using the kinetic energy equation."],
    ["9702", "2024", "March", "1", "2", "10", "The relationship between upthrust, drag force, and weight in fluid mechanics proved challenging to some."],
    ["9702", "2024", "March", "1", "2", "40", "Candidates demonstrated strong understanding of quark composition changes during beta decay."]
]

def append_to_csv(filepath, rows):
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

# 1. Write Metadata
append_to_csv(r"data\papers.csv", border_rows)
append_to_csv(r"data\grade_boundaries.csv", bounds_rows)
append_to_csv(r"data\examiner_comments.csv", ec_rows)

# 2. Extract Questions
with open("m24_qp12.txt", "r", encoding="utf-8") as f:
    raw_qp = f.read()

# Filter out headers/footers
raw_qp = re.sub(r'---PAGE \d+---', '', raw_qp)
raw_qp = re.sub(r'© UCLES 2024.*?(?=\n)', '', raw_qp)
raw_qp = re.sub(r'9702/12/F/M/24', '', raw_qp)
raw_qp = re.sub(r'\[Turn over', '', raw_qp)

lines = [l.strip() for l in raw_qp.split('\n') if l.strip() != ""]
full_text = "\n" + "\n".join(lines)

q_texts = []
last_idx = full_text.find("\n1 ")
for i in range(1, 41):
    search_str = f"\n{i+1} "
    if i == 40:
        idx = len(full_text)
    else:
        idx = full_text.find(search_str, last_idx + 1)
        if idx == -1:
            idx = full_text.find(f" {i+1} ", last_idx + 1)
            
    q_text = full_text[last_idx:idx].strip()
    q_text = re.sub(r'^\d+\s', '', q_text).strip()
    q_texts.append(q_text)
    last_idx = idx

q_rows = []
for i, text in enumerate(q_texts):
    q_num = i + 1
    has_diagram = q_num in diagram_qs
    image_path = f"images/9702_m24_qp_12_q{q_num}.png" if has_diagram else "NULL"
    
    if has_diagram:
        text = text + "\n[diagram]"
        
    q_rows.append(["9702", "2024", "March", "1", "2", str(q_num), "NULL", "1", text, image_path])

append_to_csv(r"data\questions.csv", q_rows)

# 3. Extract MS
with open("m24_ms12.txt", "r", encoding="utf-8") as f:
    ms_lines = f.readlines()

ans_map = {}
for l in ms_lines:
    l = l.strip()
    m = re.match(r'^(\d+)\s+([A-D])\s+1$', l)
    if m:
        ans_map[int(m.group(1))] = m.group(2)

ms_rows = []
for i in range(1, 41):
    ans = ans_map.get(i, "X")
    ms_rows.append(["9702", "2024", "March", "1", "2", str(i), "NULL", "1", "1", ans])

append_to_csv(r"data\markpoints.csv", ms_rows)

print(f"Successfully appended {len(q_rows)} Questions and {len(ms_rows)} MS points for m24_12 dataset!")

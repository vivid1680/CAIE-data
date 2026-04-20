import csv
import re

# 1. Metadata
with open(r"data\papers.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "November", "1", "2"])

with open(r"data\grade_boundaries.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["9702", "2025", "November", "1", "2", "40", "32", "27", "23", "20", "17"])

ec_rows = [
    ["9702", "2025", "November", "1", "2", "NULL", "Candidates showed proficiency in standard physical definitions and basic algebraic manipulation. Areas requiring improvement included the application of ratios in wave intensity and the correct use of unit prefixes when squared or cubed."],
    ["9702", "2025", "November", "1", "2", "2", "This question required converting 0.25kN mm^-2 to N m^-2. The most common error was incorrect conversion of the denominator."],
    ["9702", "2025", "November", "1", "2", "4", "Candidates analyzed the homogeneity of the pendulum equation. By equating units, it was clear that n must be 1/2."],
    ["9702", "2025", "November", "1", "2", "13", "This problem involved a rock dropped into a moving cart. While horizontal momentum is conserved, the increase in mass with no external horizontal force results in a decrease in velocity, thus reducing the total kinetic energy."]
]

with open(r"data\examiner_comments.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ec_rows:
        writer.writerow(row)

# 2. Extract Questions
with open("w25_qp12.txt", "r", encoding="utf-8") as f:
    raw = f.read()

# Clean
raw = re.sub(r'---PAGE \d+---', '', raw)
raw = re.sub(r'© UCLES 2025.*?(?=\n)', '', raw)
raw = re.sub(r'9702/12/O/N/25', '', raw)
raw = re.sub(r'\[Turn over', '', raw)

lines = raw.split('\n')
cleaned = []
for l in lines:
    if l.strip() != "":
        cleaned.append(l.strip())
        
full_text = "\n" + "\n".join(cleaned)

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

# 3. Diagram Logic
diagram_qs = [7, 10, 11, 12, 13, 14, 19, 21, 23, 25, 26, 31, 35, 36]

q_rows = []
for i, t in enumerate(q_texts):
    q_num = i + 1
    has_diagram = q_num in diagram_qs
    image_path = f"images/9702_w25_qp_12_q{q_num}.png" if has_diagram else "NULL"
    if has_diagram:
         t = t + "\n[diagram]"
    row = ["9702", "2025", "November", "1", "2", str(q_num), "NULL", "1", t, image_path]
    q_rows.append(row)

with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in q_rows:
        writer.writerow(row)

# 4. Extract MS
with open("w25_ms12.txt", "r", encoding="utf-8") as f:
    raw_ms = f.read()

ms_lines = raw_ms.split('\n')
ans_map = {}
for l in ms_lines:
    l = l.strip()
    m = re.match(r'^(\d+)\s+([A-D])\s+1$', l)
    if m:
        ans_map[int(m.group(1))] = m.group(2)

ms_rows = []
for i in range(1, 41):
    ans = ans_map.get(i, "X")
    row = ["9702", "2025", "November", "1", "2", str(i), "NULL", "1", "1", ans]
    ms_rows.append(row)

with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in ms_rows:
        writer.writerow(row)

print(f"Processed {len(q_rows)} Questions and {len(ms_rows)} Mark points for w25_12.")

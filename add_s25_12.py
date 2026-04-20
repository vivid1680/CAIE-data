import re
import csv

def process_qp(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()

    # Clean headers/footers
    raw = re.sub(r'---PAGE \d+---', '', raw)
    raw = re.sub(r'© UCLES 2025.*?(?=\n)', '', raw)
    raw = re.sub(r'9702/12/M/J/25', '', raw)
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
                # fallback
                idx = full_text.find(f" {i+1} ", last_idx + 1)
                
        q_text = full_text[last_idx:idx].strip()
        # Clean the q_text
        q_text = re.sub(r'^\d+\s', '', q_text).strip()
        q_texts.append(q_text)
        last_idx = idx

    print(f"Extracted {len(q_texts)} questions.")
    
    # Diagram configuration
    diagram_qs = [6, 8, 12, 13, 14, 15, 16, 17, 19, 22, 24, 25, 26, 27, 29, 33, 35, 36]

    q_rows = []
    for i, t in enumerate(q_texts):
        q_num = i + 1
        has_diagram = q_num in diagram_qs
        image_path = f"images/9702_s25_qp_12_q{q_num}.png" if has_diagram else "NULL"
        if has_diagram:
             t = t + "\n[diagram]"
        
        # Determine topic placeholder (using generic length of syllabus)
        topic = "NULL"  # Topic insertion strategy deferred

        row = ["9702", "2025", "June", "1", "2", str(q_num), "NULL", "1", topic, image_path, t, "NULL"]
        # Schema actually is:
        # subject_id, year, month, paper_number, variant_number, question_number, sub_question, maximum_marks, topic_name, diagram, text_statement, question_source_id (if relevant)
        # As per structures.md earlier:
        # Subject_Id, Year, Month, Paper_Number, Variant, Question_Number, Sub_Question, Max_Marks, Text_Statement, Image_Path
        row = ["9702", "2025", "June", "1", "2", str(q_num), "NULL", "1", t, image_path]
        q_rows.append(row)

    with open(r"data\questions.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in q_rows:
            writer.writerow(row)
            
    print("QP added.")


def process_ms(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()

    lines = raw.split('\n')
    ans_map = {}
    
    for l in lines:
        l = l.strip()
        m = re.match(r'^(\d+)\s+([A-D])\s+1$', l)
        if m:
            ans_map[int(m.group(1))] = m.group(2)
            
    print(f"Extracted {len(ans_map)} answers.")
    
    ms_rows = []
    for i in range(1, 41):
        ans = ans_map.get(i, "X")
        # schema for MS:
        # SubjectId, Year, Month, Paper_Number, Variant, Question_Number, Sub_Question, Markpoint_Number, Marks_Available, Text_Statement
        row = ["9702", "2025", "June", "1", "2", str(i), "NULL", "1", "1", ans]
        ms_rows.append(row)

    with open(r"data\markpoints.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in ms_rows:
            writer.writerow(row)
            
    print("MS added.")

process_qp("s25_qp12.txt")
process_ms("s25_ms12.txt")

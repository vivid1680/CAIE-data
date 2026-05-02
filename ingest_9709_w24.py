import csv
import os
import re

def append_to_csv(filepath, row):
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def ingest_metadata():
    print("Ingesting Metadata (Papers & Grade Boundaries)...")
    # papers.csv: subject_code,year,session,paper_number,variant,num_questions,total_marks,duration_mins
    papers = [
        ['9709', '2024', 'November', '1', '1', '11', '75', '110'],
        ['9709', '2024', 'November', '3', '1', '10', '75', '110'],
        ['9709', '2024', 'November', '5', '1', '7', '50', '75'],
        ['9709', '2024', 'November', '1', '2', '11', '75', '110'],
        ['9709', '2024', 'November', '3', '2', '11', '75', '110'],
        ['9709', '2024', 'November', '5', '2', '7', '50', '75'],
        ['9709', '2024', 'November', '1', '3', '11', '75', '110'],
        ['9709', '2024', 'November', '3', '3', '10', '75', '110'],
        ['9709', '2024', 'November', '5', '3', '7', '50', '75'],
    ]
    for p in papers:
        append_to_csv('data/papers.csv', p)
        
    # grade_boundaries.csv: subject_code,year,session,paper_number,variant,grade,threshold
    boundaries = [
        ['9709', '2024', 'November', '1', '1', 'A', '52'],
        ['9709', '2024', 'November', '1', '1', 'B', '44'],
        ['9709', '2024', 'November', '1', '1', 'C', '34'],
        ['9709', '2024', 'November', '1', '1', 'D', '25'],
        ['9709', '2024', 'November', '1', '1', 'E', '16'],
        
        ['9709', '2024', 'November', '3', '1', 'A', '54'],
        ['9709', '2024', 'November', '3', '1', 'B', '45'],
        ['9709', '2024', 'November', '3', '1', 'C', '37'],
        ['9709', '2024', 'November', '3', '1', 'D', '29'],
        ['9709', '2024', 'November', '3', '1', 'E', '21'],
        
        ['9709', '2024', 'November', '5', '1', 'A', '40'],
        ['9709', '2024', 'November', '5', '1', 'B', '36'],
        ['9709', '2024', 'November', '5', '1', 'C', '29'],
        ['9709', '2024', 'November', '5', '1', 'D', '22'],
        ['9709', '2024', 'November', '5', '1', 'E', '15'],

        ['9709', '2024', 'November', '1', '2', 'A', '52'],
        ['9709', '2024', 'November', '1', '2', 'B', '44'],
        ['9709', '2024', 'November', '1', '2', 'C', '34'],
        ['9709', '2024', 'November', '1', '2', 'D', '24'],
        ['9709', '2024', 'November', '1', '2', 'E', '15'],

        ['9709', '2024', 'November', '3', '2', 'A', '51'],
        ['9709', '2024', 'November', '3', '2', 'B', '42'],
        ['9709', '2024', 'November', '3', '2', 'C', '35'],
        ['9709', '2024', 'November', '3', '2', 'D', '27'],
        ['9709', '2024', 'November', '3', '2', 'E', '20'],

        ['9709', '2024', 'November', '5', '2', 'A', '40'],
        ['9709', '2024', 'November', '5', '2', 'B', '36'],
        ['9709', '2024', 'November', '5', '2', 'C', '29'],
        ['9709', '2024', 'November', '5', '2', 'D', '22'],
        ['9709', '2024', 'November', '5', '2', 'E', '15'],

        ['9709', '2024', 'November', '1', '3', 'A', '55'],
        ['9709', '2024', 'November', '1', '3', 'B', '47'],
        ['9709', '2024', 'November', '1', '3', 'C', '37'],
        ['9709', '2024', 'November', '1', '3', 'D', '27'],
        ['9709', '2024', 'November', '1', '3', 'E', '18'],

        ['9709', '2024', 'November', '3', '3', 'A', '55'],
        ['9709', '2024', 'November', '3', '3', 'B', '45'],
        ['9709', '2024', 'November', '3', '3', 'C', '37'],
        ['9709', '2024', 'November', '3', '3', 'D', '29'],
        ['9709', '2024', 'November', '3', '3', 'E', '21'],

        ['9709', '2024', 'November', '5', '3', 'A', '40'],
        ['9709', '2024', 'November', '5', '3', 'B', '34'],
        ['9709', '2024', 'November', '5', '3', 'C', '28'],
        ['9709', '2024', 'November', '5', '3', 'D', '22'],
        ['9709', '2024', 'November', '5', '3', 'E', '16'],
    ]
    for b in boundaries:
        append_to_csv('data/grade_boundaries.csv', b)

def parse_qp(file_path, subject, year, session, paper, variant):
    print(f"Parsing QP: {file_path}")
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pages = content.split('---PAGE')
    questions = []
    current_q = None
    for page in pages:
        lines = page.split('\n')
        for line in lines:
            line = line.strip()
            if not line: continue
            q_match = re.match(r'^(\d+)\s*$', line)
            if q_match:
                current_q = q_match.group(1)
                continue
            p_match = re.match(r'^\((\w+)\)\s*(.*)', line)
            if current_q and p_match:
                part_label = p_match.group(1)
                text = p_match.group(2)
                marks = "NULL"
                m_match = re.search(r'\[(\d+)\]', line)
                if m_match: marks = m_match.group(1)
                image_path = f"images/{subject}_w24_{paper}{variant}_q{current_q}.png"
                if not os.path.exists(os.path.join("data", image_path)): image_path = "NULL"
                questions.append([subject, year, session, paper, variant, current_q, part_label, marks, text, image_path])
                continue
            m_match = re.search(r'\[(\d+)\]', line)
            if current_q and m_match and not any(q[5] == current_q and q[6] != "NULL" for q in questions):
                marks = m_match.group(1)
                image_path = f"images/{subject}_w24_{paper}{variant}_q{current_q}.png"
                if not os.path.exists(os.path.join("data", image_path)): image_path = "NULL"
                questions.append([subject, year, session, paper, variant, current_q, "NULL", marks, "Question Statement", image_path])
    for q in questions:
        append_to_csv('data/questions.csv', q)

def parse_ms(file_path, subject, year, session, paper, variant):
    print(f"Parsing MS: {file_path}")
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    current_q = None
    current_part = None
    for line in lines:
        line = line.strip()
        match = re.match(r'^(\d+)(\((\w+)\))?$', line)
        if match:
            current_q = match.group(1)
            current_part = match.group(3) if match.group(3) else "NULL"
            continue
        m_match = re.search(r'^(\*?[MAB]\d+)\s*(.*)', line)
        if current_q and m_match:
            mark_type = m_match.group(1)
            desc = m_match.group(2)
            append_to_csv('data/markpoints.csv', [subject, year, session, paper, variant, current_q, current_part, '1', mark_type, '1', desc])

if __name__ == "__main__":
    ingest_metadata()
    parse_qp('9709_w24_qp11.txt', '9709', '2024', 'November', '1', '1')
    parse_qp('9709_w24_qp12.txt', '9709', '2024', 'November', '1', '2')
    parse_qp('9709_w24_qp13.txt', '9709', '2024', 'November', '1', '3')
    parse_qp('9709_w24_qp31.txt', '9709', '2024', 'November', '3', '1')
    parse_qp('9709_w24_qp32.txt', '9709', '2024', 'November', '3', '2')
    parse_qp('9709_w24_qp33.txt', '9709', '2024', 'November', '3', '3')
    parse_qp('9709_w24_qp51.txt', '9709', '2024', 'November', '5', '1')
    parse_qp('9709_w24_qp52.txt', '9709', '2024', 'November', '5', '2')
    parse_qp('9709_w24_qp53.txt', '9709', '2024', 'November', '5', '3')
    parse_ms('9709_w24_ms11.txt', '9709', '2024', 'November', '1', '1')
    parse_ms('9709_w24_ms12.txt', '9709', '2024', 'November', '1', '2')
    parse_ms('9709_w24_ms13.txt', '9709', '2024', 'November', '1', '3')
    parse_ms('9709_w24_ms31.txt', '9709', '2024', 'November', '3', '1')
    parse_ms('9709_w24_ms32.txt', '9709', '2024', 'November', '3', '2')
    parse_ms('9709_w24_ms33.txt', '9709', '2024', 'November', '3', '3')
    parse_ms('9709_w24_ms51.txt', '9709', '2024', 'November', '5', '1')
    parse_ms('9709_w24_ms52.txt', '9709', '2024', 'November', '5', '2')
    parse_ms('9709_w24_ms53.txt', '9709', '2024', 'November', '5', '3')

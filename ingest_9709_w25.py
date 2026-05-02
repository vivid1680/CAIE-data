import csv
import os
import re

def append_to_csv(filepath, row):
    file_exists = os.path.isfile(filepath)
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def ingest_metadata():
    print("Ingesting Metadata (Papers & Grade Boundaries)...")
    
    # papers.csv: subject_code,year,session,paper_number,variant,num_questions,total_marks,duration_mins
    papers = [
        ['9709', '2025', 'November', '1', '1', '11', '75', '110'],
        ['9709', '2025', 'November', '3', '1', '10', '75', '110'],
        ['9709', '2025', 'November', '5', '1', '7', '50', '75'],
        ['9709', '2025', 'November', '1', '2', '9', '75', '110'],
        ['9709', '2025', 'November', '3', '2', '9', '75', '110'],
        ['9709', '2025', 'November', '5', '2', '7', '50', '75'],
        ['9709', '2025', 'November', '1', '3', '8', '75', '110'],
        ['9709', '2025', 'November', '2', '3', '8', '50', '75'],
        ['9709', '2025', 'November', '5', '3', '7', '50', '75'],
    ]
    for p in papers:
        append_to_csv('data/papers.csv', p)
        
    # grade_boundaries.csv: subject_code,year,session,paper_number,variant,grade,threshold
    # Thresholds from 9709_gt.txt
    boundaries = [
        ['9709', '2025', 'November', '1', '1', 'A', '60'],
        ['9709', '2025', 'November', '1', '1', 'B', '51'],
        ['9709', '2025', 'November', '1', '1', 'C', '40'],
        ['9709', '2025', 'November', '1', '1', 'D', '28'],
        ['9709', '2025', 'November', '1', '1', 'E', '16'],
        
        ['9709', '2025', 'November', '3', '1', 'A', '58'],
        ['9709', '2025', 'November', '3', '1', 'B', '49'],
        ['9709', '2025', 'November', '3', '1', 'C', '40'],
        ['9709', '2025', 'November', '3', '1', 'D', '31'],
        ['9709', '2025', 'November', '3', '1', 'E', '21'],
        
        ['9709', '2025', 'November', '5', '1', 'A', '41'],
        ['9709', '2025', 'November', '5', '1', 'B', '37'],
        ['9709', '2025', 'November', '5', '1', 'C', '29'],
        ['9709', '2025', 'November', '5', '1', 'D', '22'],
        ['9709', '2025', 'November', '5', '1', 'E', '15'],
        
        ['9709', '2025', 'November', '1', '2', 'A', '60'],
        ['9709', '2025', 'November', '1', '2', 'B', '51'],
        ['9709', '2025', 'November', '1', '2', 'C', '39'],
        ['9709', '2025', 'November', '1', '2', 'D', '27'],
        ['9709', '2025', 'November', '1', '2', 'E', '16'],

        ['9709', '2025', 'November', '3', '2', 'A', '45'],
        ['9709', '2025', 'November', '3', '2', 'B', '38'],
        ['9709', '2025', 'November', '3', '2', 'C', '32'],
        ['9709', '2025', 'November', '3', '2', 'D', '25'],
        ['9709', '2025', 'November', '3', '2', 'E', '17'],

        ['9709', '2025', 'November', '5', '2', 'A', '38'],
        ['9709', '2025', 'November', '5', '2', 'B', '33'],
        ['9709', '2025', 'November', '5', '2', 'C', '25'],
        ['9709', '2025', 'November', '5', '2', 'D', '18'],
        ['9709', '2025', 'November', '5', '2', 'E', '10'],

        ['9709', '2025', 'November', '1', '3', 'A', '61'],
        ['9709', '2025', 'November', '1', '3', 'B', '54'],
        ['9709', '2025', 'November', '1', '3', 'C', '43'],
        ['9709', '2025', 'November', '1', '3', 'D', '30'],
        ['9709', '2025', 'November', '1', '3', 'E', '19'],

        ['9709', '2025', 'November', '2', '3', 'A', '42'],
        ['9709', '2025', 'November', '2', '3', 'B', '37'],
        ['9709', '2025', 'November', '2', '3', 'C', '29'],
        ['9709', '2025', 'November', '2', '3', 'D', '21'],
        ['9709', '2025', 'November', '2', '3', 'E', '14'],

        ['9709', '2025', 'November', '5', '3', 'A', '45'],
        ['9709', '2025', 'November', '5', '3', 'B', '40'],
        ['9709', '2025', 'November', '5', '3', 'C', '32'],
        ['9709', '2025', 'November', '5', '3', 'D', '25'],
        ['9709', '2025', 'November', '5', '3', 'E', '18'],
    ]
    for b in boundaries:
        append_to_csv('data/grade_boundaries.csv', b)

def parse_qp(file_path, subject, year, session, paper, variant):
    print(f"Parsing QP: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by PAGE
    pages = content.split('---PAGE')
    questions = []
    
    current_q = None
    
    # Regex for question start: e.g. "1 \nFind the set..."
    # 9709 QPs often have question numbers as a single block at start of page or after previous Q.
    # Parts are like "(a)" or "(b)"
    
    for page in pages:
        # Simple line-by-line for now
        lines = page.split('\n')
        for line in lines:
            line = line.strip()
            if not line: continue
            
            # Question Start
            q_match = re.match(r'^(\d+)\s*$', line)
            if q_match:
                current_q = q_match.group(1)
                # Base question row
                continue
            
            # Part start
            p_match = re.match(r'^\((\w+)\)\s*(.*)', line)
            if current_q and p_match:
                part_label = p_match.group(1)
                text = p_match.group(2)
                # Look for marks [X]
                marks = "NULL"
                m_match = re.search(r'\[(\d+)\]', line)
                if m_match:
                    marks = m_match.group(1)
                
                # Check for image
                image_path = f"images/9709_w25_{paper}{variant}_q{current_q}.png"
                if not os.path.exists(os.path.join("data", image_path)):
                    image_path = "NULL"
                
                questions.append([subject, year, session, paper, variant, current_q, part_label, marks, text, image_path])
                continue
            
            # If it's a mark line like [4] but no part
            m_match = re.search(r'\[(\d+)\]', line)
            if current_q and m_match and not any(q[5] == current_q and q[6] != "NULL" for q in questions):
                # This is a whole question without parts
                marks = m_match.group(1)
                # find text (usually preceding lines)
                # Simplified: use the first 100 chars of the page after Q num
                image_path = f"images/9709_w25_{paper}{variant}_q{current_q}.png"
                if not os.path.exists(os.path.join("data", image_path)):
                    image_path = "NULL"
                questions.append([subject, year, session, paper, variant, current_q, "NULL", marks, "Question Statement (See PDF)", image_path])

    for q in questions:
        append_to_csv('data/questions.csv', q)

def parse_ms(file_path, subject, year, session, paper, variant):
    print(f"Parsing MS: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_q = None
    current_part = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Question header in MS table: e.g. "1" or "2(a)"
        match = re.match(r'^(\d+)(\((\w+)\))?$', line)
        if match:
            current_q = match.group(1)
            current_part = match.group(3) if match.group(3) else "NULL"
            continue
            
        # Mark entry: e.g. "M1", "A1", "B1"
        m_match = re.search(r'^(\*?[MAB]\d+)\s*(.*)', line)
        if current_q and m_match:
            mark_type = m_match.group(1)
            desc = m_match.group(2)
            # step_number: just use index for now or 1
            append_to_csv('data/markpoints.csv', [subject, year, session, paper, variant, current_q, current_part, '1', mark_type, '1', desc])

def ingest_er():
    print("Ingesting Examiner Comments...")
    # examiner_comments.csv: subject_code,year,session,paper_number,variant,question_number,comment_text
    comments = [
        ['9709', '2025', 'November', '5', '1', '1', 'Candidates were required to form an equation using the property P(X = x) = 1. The resulting value for the constant was k = 1/18.'],
        ['9709', '2025', 'November', '5', '1', '5', 'For the 150-day period approximation, the parameters used were: µ = 15, σ2 = 13.5. Continuity correction of 21.5 expected.'],
        ['9709', '2025', 'November', '5', '1', '7', 'The total number of arrangements for the word SEYCHELLES is 10! / (2!2!3!) = 151 200.'],
        ['9709', '2025', 'November', '5', '2', '2', 'The calculation for variance resulted in 14/9 approx 1.56. Candidates were required to construct a probability distribution table.'],
        ['9709', '2025', 'November', '5', '2', '4', 'This question involved forming an equation based on pack sizes. Solving the linear or quadratic form yielded x = 42.'],
        ['9709', '2025', 'November', '5', '2', '6', 'For the approximation in part (c), the parameters were µ = 56 and σ2 = 48. A continuity correction of 65.5 was required.'],
        ['9709', '2025', 'November', '5', '2', '7', 'The total number of arrangements of ZOOLOGICAL with the three Os together and the two Ls separated was found using: 8!/2! - 7! = 15 120.'],
    ]
    for c in comments:
        append_to_csv('data/examiner_comments.csv', c)

if __name__ == "__main__":
    ingest_metadata()
    
    tasks = [
        ('qp', '9709_qp11.txt', '9709', '2025', 'November', '1', '1'),
        ('qp', '9709_qp12.txt', '9709', '2025', 'November', '1', '2'),
        ('qp', '9709_qp13.txt', '9709', '2025', 'November', '1', '3'),
        ('qp', '9709_qp31.txt', '9709', '2025', 'November', '3', '1'),
        ('qp', '9709_qp32.txt', '9709', '2025', 'November', '3', '2'),
        ('qp', '9709_qp51.txt', '9709', '2025', 'November', '5', '1'),
        ('qp', '9709_qp52.txt', '9709', '2025', 'November', '5', '2'),
        ('qp', '9709_qp23.txt', '9709', '2025', 'November', '2', '3'),
        ('qp', '9709_qp53.txt', '9709', '2025', 'November', '5', '3'),
        
        ('ms', '9709_ms11.txt', '9709', '2025', 'November', '1', '1'),
        ('ms', '9709_ms12.txt', '9709', '2025', 'November', '1', '2'),
        ('ms', '9709_ms13.txt', '9709', '2025', 'November', '1', '3'),
        ('ms', '9709_ms31.txt', '9709', '2025', 'November', '3', '1'),
        ('ms', '9709_ms32.txt', '9709', '2025', 'November', '3', '2'),
        ('ms', '9709_ms51.txt', '9709', '2025', 'November', '5', '1'),
        ('ms', '9709_ms52.txt', '9709', '2025', 'November', '5', '2'),
        ('ms', '9709_ms23.txt', '9709', '2025', 'November', '2', '3'),
        ('ms', '9709_ms53.txt', '9709', '2025', 'November', '5', '3'),
    ]
    
    for t_type, path, s, y, sess, p, v in tasks:
        if os.path.exists(path):
            if t_type == 'qp': parse_qp(path, s, y, sess, p, v)
            else: parse_ms(path, s, y, sess, p, v)
        else:
            print(f"Skipping {path}: File not found.")

    ingest_er()

import sys
import re

def parse_questions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    raw = "".join(lines)
    
    # Clean up standard footers
    raw = re.sub(r'---PAGE \d+---', '', raw)
    raw = re.sub(r'© UCLES 2025.*?(?=\n)', '', raw)
    raw = re.sub(r'9702/12/F/M/25', '', raw)
    raw = re.sub(r'\[Turn .*?', '', raw)
    # Filter lines
    lines = raw.split('\n')
    cleaned = []
    for l in lines:
        if l.strip() != "":
            cleaned.append(l.strip())
            
    full_text = "\n" + "\n".join(cleaned)
    
    q_texts = []
    last_idx = 0
    for i in range(1, 41):
        search_str = f"\n{i} "
        idx = full_text.find(search_str, last_idx)
        if idx == -1:
            # try without prefix newline
            idx = full_text.find(f"{i} ", last_idx)
            if idx == -1:
                print(f"FAILED to find {i}")
                break
        
        if i > 1:
            q_texts.append(full_text[last_idx:idx].strip())
        last_idx = idx
        
    q_texts.append(full_text[last_idx:].strip())
    
    print(f"Extracted {len(q_texts)} questions.")
    for i, t in enumerate(q_texts):
        print(f"Q{i+1}: {t[:50].replace(chr(10), ' ')}...")
        
parse_questions("qp.txt")

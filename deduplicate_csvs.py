import csv
import os

def deduplicate(filename):
    if not os.path.exists(filename): return
    print(f"Deduplicating {filename}...")
    seen = set()
    rows = []
    header = None
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return
        for row in reader:
            if not row: continue
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                rows.append(row)
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

if __name__ == "__main__":
    csvs = [
        'data/papers.csv',
        'data/grade_boundaries.csv',
        'data/questions.csv',
        'data/markpoints.csv',
        'data/topics.csv',
        'data/question_topics.csv',
        'data/examiner_comments.csv'
    ]
    for c in csvs:
        deduplicate(c)

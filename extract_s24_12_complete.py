import os
import fitz
import re

def extract_mcq_diagrams(pdf_path, paper_code, target_questions):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    extracted_count = 0
    seen_questions = set()
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        words = page.get_text("words")
        
        for w in words:
            text = w[4].strip()
            if text.isdigit():
                q_num = int(text)
                if q_num in target_questions and q_num not in seen_questions:
                    # Near left margin check
                    if w[0] < 100:
                        print(f"Found Q{q_num} on Page {page_num+1} at Y={w[1]:.1f}")
                        seen_questions.add(q_num)
                        
                        q_y1 = w[3]
                        bottom_y = 0
                        
                        # Find boundary
                        for w_next in words:
                            if w_next[1] > q_y1:
                                if w_next[4].strip().isdigit() and int(w_next[4].strip()) == q_num + 1 and w_next[0] < 100:
                                    bottom_y = w_next[1]
                                    break
                                if w_next[4].strip() in ["A", "B", "C", "D"] and w_next[0] < 100:
                                    if w_next[1] - q_y1 > 20: 
                                        bottom_y = w_next[1]
                                        break
                        
                        if bottom_y == 0 or (bottom_y - q_y1) > 400:
                            bottom_y = q_y1 + 250
                        
                        if (bottom_y - q_y1) < 40:
                            bottom_y = q_y1 + 150
                            
                        crop_rect = fitz.Rect(20, q_y1 - 2, page.rect.width - 20, bottom_y + 2)
                        
                        filename = f"9702_{paper_code}_qp_fig{q_num}.png"
                        filepath = os.path.join(output_dir, filename)
                        pix = page.get_pixmap(clip=crop_rect, dpi=200)
                        pix.save(filepath)
                        print(f"  -> Extracted Q{q_num}: Y={q_y1:.1f} to {bottom_y:.1f}")
                        extracted_count += 1
                        
    print(f"Total extracted: {extracted_count}")
    print(f"Questions found: {sorted(list(seen_questions))}")

if __name__ == "__main__":
    targets = [5, 6, 10, 11, 12, 15, 18, 19, 20, 21, 23, 26, 31, 35, 36]
    extract_mcq_diagrams("9702_s24_qp_12.pdf", "s24_12", targets)

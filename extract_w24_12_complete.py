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
        
        # Get individual words to find precise coordinates of question numbers
        words = page.get_text("words")
        # word: (x0, y0, x1, y1, "text", block_no, line_no, word_no)
        
        for w in words:
            text = w[4].strip()
            # Look for integers that are likely question numbers
            if text.isdigit():
                q_num = int(text)
                if q_num in target_questions and q_num not in seen_questions:
                    # Check if it's likely a question start (near left margin)
                    if w[0] < 100:
                        print(f"Found Q{q_num} on Page {page_num+1} at Y={w[1]:.1f}")
                        
                        seen_questions.add(q_num)
                        
                        # Top of crop: bottom of the number or start of question line
                        q_y1 = w[3]
                        
                        # Find bottom boundary: Either the next question number or options
                        bottom_y = 0
                        # Look for words further down
                        for w_next in words:
                            if w_next[1] > q_y1:
                                # Next question number
                                if w_next[4].strip().isdigit() and int(w_next[4].strip()) == q_num + 1 and w_next[0] < 100:
                                    bottom_y = w_next[1]
                                    break
                                # Options A B C D (usually single chars at start of line)
                                if w_next[4].strip() in ["A", "B", "C", "D"] and w_next[0] < 100:
                                    # We skip if it's too close to q_y1 (probably just part of some text)
                                    if w_next[1] - q_y1 > 20: 
                                        bottom_y = w_next[1]
                                        break
                        
                        if bottom_y == 0 or (bottom_y - q_y1) > 400:
                            bottom_y = q_y1 + 250
                            
                        # Ensure we don't crop too small
                        if (bottom_y - q_y1) < 30:
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
    targets = [4, 8, 10, 12, 13, 18, 20, 22, 24, 30, 31, 33, 35]
    extract_mcq_diagrams("9702_w24_qp_12.pdf", "w24_12", targets)

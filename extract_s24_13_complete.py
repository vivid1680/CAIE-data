import fitz
import os

def extract_mcq_diagrams(pdf_path, paper_code, diag_questions):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        words = page.get_text("words")  # (x0, y0, x1, y1, word, block_no, line_no, word_no)
        
        for q_num in diag_questions:
            q_str = str(q_num)
            
            # Find the question number
            q_found = False
            q_rect = None
            for i, w in enumerate(words):
                if w[4] == q_str:
                    # Double check if it's at the start of a line and followed by text
                    if w[0] < 100:
                        q_rect = fitz.Rect(w[:4])
                        q_found = True
                        break
            
            if q_found:
                # Find the next question or Option A
                next_marker_y = page.rect.height
                for i, w in enumerate(words):
                    # Check for "A" (Option marker) below the question number
                    if w[4] == "A" and w[1] > q_rect.y1 and w[0] < 100:
                        next_marker_y = w[1]
                        break
                    # Check for next question number
                    if w[4] == str(q_num + 1) and w[1] > q_rect.y1 and w[0] < 100:
                        next_marker_y = w[1]
                        break
                
                # Check for "Page" or "BLANK"
                for i, w in enumerate(words):
                    if ("[Turn" in w[4] or "BLANK" in w[4]) and w[1] > q_rect.y1:
                        next_marker_y = min(next_marker_y, w[1])

                crop_rect = fitz.Rect(20, q_rect.y1 + 2, page.rect.width - 20, next_marker_y - 2)
                
                if crop_rect.height > 20: # Only extract if there's space for a diagram
                    filename = f"9702_{paper_code}_qp_fig{q_num}.png"
                    filepath = os.path.join(output_dir, filename)
                    pix = page.get_pixmap(clip=crop_rect, dpi=200)
                    pix.save(filepath)
                    print(f"Extracted Question {q_num} diagram from Page {page_num+1}")

if __name__ == "__main__":
    diag_qs = [5,6,8,10,11,13,14,17,18,19,20,22,26,28,29,32,33,34,35,36,37,38,39]
    extract_mcq_diagrams("9702_s24_qp_13.pdf", "s24_13", diag_qs)

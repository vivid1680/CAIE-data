import os
import fitz

def extract_specific_mcq_diagrams(pdf_path, paper_code):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    diagram_qs = [2, 3, 6, 8, 12, 13, 14, 17, 18, 23, 25, 29, 31, 33, 35, 38]
    
    extracted_questions = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0]
        text_blocks.sort(key=lambda x: x[1]) # sort vertically
        
        q_map = {}
        # Map blocks to questions
        for block in text_blocks:
            text = block[4].strip()
            # Does block start with a question number? e.g. "3 "
            # Or does it contain just the question number?
            parts = text.split(" ")
            
            # For robustness, we check if the first part is a number and it's within 1-40
            if len(parts) > 0 and parts[0].isdigit():
                q_num = int(parts[0])
                if 1 <= q_num <= 40 and str(q_num) == parts[0]:
                    if q_num not in q_map:
                        q_map[q_num] = []
            
            if q_map:
                latest_q = list(q_map.keys())[-1]
                q_map[latest_q].append(block)
                
        # Now for each question dynamically
        for q_num, q_blocks in q_map.items():
            if q_num in diagram_qs:
                # We know there is a diagram. We need to find the largest vertical gap
                # between any two text blocks inside this question's space.
                # If there are diagram labels, the gap might not be huge, but it's usually 
                # the largest gap between the question text and the answers (A/B/C/D).
                
                max_gap = 0
                best_crop = None
                
                for i in range(len(q_blocks) - 1):
                    b1 = q_blocks[i]
                    b2 = q_blocks[i+1]
                    
                    gap = b2[1] - b1[3]
                    
                    # Exclude gaps that are actually tiny spacing
                    if gap > max_gap and gap > 15:
                        max_gap = gap
                        
                        # Set crop bounds from bottom of b1 to top of b2
                        # We use wide margins for X to get the full diagram
                        pad = 10
                        if gap > 300: # clamp huge gaps
                            gap = 300
                            
                        best_crop = fitz.Rect(40, max(0, b1[3] - pad), page.rect.width - 40, min(page.rect.height, b2[1] + pad))
                
                if best_crop:
                    filename = f"9702_{paper_code}_q{q_num}.png"
                    filepath = os.path.join(output_dir, filename)
                    pix = page.get_pixmap(clip=best_crop, dpi=200)
                    pix.save(filepath)
                    extracted_questions.append(q_num)
                    print(f"Extracted graphical gap for Q{q_num} -> {filename}")
                else:
                    print(f"FAILED to find gap for Q{q_num}")

    print("Successfully Extracted list: ", sorted(list(set(extracted_questions))))
    print("Missed: ", set(diagram_qs) - set(extracted_questions))

if __name__ == "__main__":
    extract_specific_mcq_diagrams("9702_m24_qp_12.pdf", "m24_qp_12")

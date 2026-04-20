import os
import fitz

def extract_entire_mcq_question(pdf_path, paper_code):
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
        for block in text_blocks:
            text = block[4].strip()
            
            # Skip page headers and footers mathematically
            if block[1] < 60 or block[1] > page.rect.height - 60:
                continue
                
            parts = text.split(" ")
            if len(parts) > 0 and parts[0].isdigit():
                q_num = int(parts[0])
                if 1 <= q_num <= 40 and str(q_num) == parts[0]:
                    if q_num not in q_map:
                        q_map[q_num] = []
            if q_map:
                latest_q = list(q_map.keys())[-1]
                q_map[latest_q].append(block)
                
        # To get the y-bounds, we will bound from the top of the question's first block
        # to the top of the next question's first block (or the bottom of the page).
        sorted_qs = sorted(q_map.keys())
        
        for i, q_num in enumerate(sorted_qs):
            if q_num in diagram_qs:
                y0 = q_map[q_num][0][1] # Top coordinate of the question text
                
                if i + 1 < len(sorted_qs):
                    y1 = q_map[sorted_qs[i+1]][0][1] # Top coordinate of the NEXT question
                else:
                    y1 = page.rect.height - 40 # Bottom of the page (ignoring footer)
                
                # Crop horizontally across the full page, adjusting for margins
                crop_rect = fitz.Rect(30, max(0, y0 - 15), page.rect.width - 30, min(page.rect.height, y1))
                
                filename = f"9702_{paper_code}_q{q_num}.png"
                filepath = os.path.join(output_dir, filename)
                
                pix = page.get_pixmap(clip=crop_rect, dpi=200)
                pix.save(filepath)
                extracted_questions.append(q_num)
                print(f"Captured Entire Question Block for Q{q_num} -> {filename}")

if __name__ == "__main__":
    extract_entire_mcq_question("9702_m24_qp_12.pdf", "m24_qp_12")

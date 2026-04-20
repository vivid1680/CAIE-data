import os
import fitz

def extract_mcq_figures_robust(pdf_path, paper_code):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    extracted_questions = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        blocks = page.get_text("blocks")
        # Text blocks
        text_blocks = [b for b in blocks if b[6] == 0]
        text_blocks.sort(key=lambda x: x[1]) # sort by y0
        
        q_map = {}
        # Identify when a block starts with a number 1-40
        for block in text_blocks:
            text = block[4].strip()
            parts = text.split(" ")
            if len(parts) > 0 and parts[0].isdigit():
                q_num = int(parts[0])
                if 1 <= q_num <= 40:
                    if q_num not in q_map:
                        q_map[q_num] = []
            
            # append block to the latest active question on this page
            if q_map:
                latest_q = list(q_map.keys())[-1]
                q_map[latest_q].append(block)
                
        # Now analyze gaps within each question's blocks
        for q_num, q_blocks in q_map.items():
            max_gap = 0
            best_crop = None
            
            for i in range(len(q_blocks) - 1):
                b1 = q_blocks[i]
                b2 = q_blocks[i+1]
                
                # vertical gap from bottom of b1 to top of b2
                gap = b2[1] - b1[3]
                
                # Check if it's a large purely empty gap indicating a graphics region
                if gap > 35: 
                    if gap > max_gap:
                        max_gap = gap
                        # crop bounds: Left to Right across page, from bottom of b1 to top of b2
                        pad = 10
                        best_crop = fitz.Rect(40, max(0, b1[3] - pad), page.rect.width - 40, min(page.rect.height, b2[1] + pad))
                        
            # If we found a significant visual gap, we crop it
            # Or if it's a known missing diagram bounding box!
            if best_crop and max_gap > 35:
                # generate image
                filename = f"9702_{paper_code}_q{q_num}.png"
                filepath = os.path.join(output_dir, filename)
                pix = page.get_pixmap(clip=best_crop, dpi=200)
                pix.save(filepath)
                extracted_questions.append(q_num)
                print(f"Extracted graphical gap for Q{q_num} -> {filename}")

    print("Extraction list: ", sorted(list(set(extracted_questions))))

if __name__ == "__main__":
    extract_mcq_figures_robust("9702_m24_qp_12.pdf", "m24_qp_12")

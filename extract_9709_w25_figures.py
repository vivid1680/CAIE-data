import os
import fitz
import re

def extract_9709_figures(pdf_path, paper_code):
    if not os.path.exists(pdf_path):
        print(f"Skipping {pdf_path}: File not found.")
        return
    print(f"\nExtracting Figures from {pdf_path}")
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    extracted_count = 0
    mat = fitz.Matrix(3, 3) # Vector scaling
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0]
        
        # Detect Question starts (number at start of block)
        question_bounds = {}
        for block in text_blocks:
            text = block[4].strip()
            # 9709 Q numbers are usually "1 ", "2 " etc at start of a line
            match = re.match(r"^(\d+)\s", text)
            if match:
                q_num = int(match.group(1))
                if 1 <= q_num <= 15: # Maths papers usually have ~10-12 questions
                    question_bounds[q_num] = block[1]
        
        if not question_bounds:
            continue
            
        sorted_qs = sorted(question_bounds.keys())
        drawings = page.get_drawings()
        
        for i, q_num in enumerate(sorted_qs):
            y_start = question_bounds[q_num]
            y_end = question_bounds[sorted_qs[i+1]] if i+1 < len(sorted_qs) else page.rect.height
            
            has_graphics = False
            crop_rect = fitz.Rect()
            
            # Scan for drawings in this question's vertical range
            for path in drawings:
                b = path['rect']
                if b.is_empty: continue
                # In Maths, diagrams are often between the question number and the first part (a)
                # or just generally within the question block.
                if b.y0 >= y_start - 20 and b.y1 <= y_end + 20:
                    if not has_graphics:
                        crop_rect = b
                        has_graphics = True
                    else:
                        crop_rect |= b
            
            # Scan for images
            for img in page.get_image_info():
                b = fitz.Rect(img['bbox'])
                if b.y0 >= y_start - 20 and b.y1 <= y_end + 20:
                    if not has_graphics:
                        crop_rect = b
                        has_graphics = True
                    else:
                        crop_rect |= b
            
            if has_graphics:
                # Add padding
                crop_rect = fitz.Rect(max(0, crop_rect.x0 - 15), max(0, crop_rect.y0 - 15), 
                                      min(page.rect.width, crop_rect.x1 + 15), min(page.rect.height, crop_rect.y1 + 15))
                
                if crop_rect.width > 30 and crop_rect.height > 30:
                    filename = f"9709_{paper_code}_q{q_num}.png"
                    filepath = os.path.join(output_dir, filename)
                    pix = page.get_pixmap(matrix=mat, clip=crop_rect)
                    pix.save(filepath)
                    print(f"  -> Extracted diagram for Q{q_num} ({filename})")
                    extracted_count += 1

    print(f"Total extracted for {paper_code}: {extracted_count}")

if __name__ == "__main__":
    extract_9709_figures("9709_w25_qp_11.pdf", "w25_11")
    extract_9709_figures("9709_w25_qp_12.pdf", "w25_12")
    extract_9709_figures("9709_w25_qp_31.pdf", "w25_31")
    extract_9709_figures("9709_w25_qp_32.pdf", "w25_32")
    extract_9709_figures("9709_s25_qp_11.pdf", "s25_11")
    extract_9709_figures("9709_s25_qp_12.pdf", "s25_12")
    extract_9709_figures("9709_s25_qp_13.pdf", "s25_13")
    extract_9709_figures("9709_s25_qp_31.pdf", "s25_31")
    extract_9709_figures("9709_s25_qp_32.pdf", "s25_32")
    extract_9709_figures("9709_s25_qp_33.pdf", "s25_33")
    extract_9709_figures("9709_s25_qp_51.pdf", "s25_51")
    extract_9709_figures("9709_s25_qp_52.pdf", "s25_52")
    extract_9709_figures("9709_s25_qp_53.pdf", "s25_53")
    extract_9709_figures("9709_m25_qp_12.pdf", "m25_12")
    extract_9709_figures("9709_m25_qp_32.pdf", "m25_32")
    extract_9709_figures("9709_m25_qp_52.pdf", "m25_52")
    extract_9709_figures("9709_w24_qp_11.pdf", "w24_11")
    extract_9709_figures("9709_w24_qp_31.pdf", "w24_31")
    extract_9709_figures("9709_w24_qp_51.pdf", "w24_51")
    extract_9709_figures("9709_w24_qp_12.pdf", "w24_12")
    extract_9709_figures("9709_w24_qp_32.pdf", "w24_32")
    extract_9709_figures("9709_w24_qp_52.pdf", "w24_52")
    extract_9709_figures("9709_w24_qp_13.pdf", "w24_13")
    extract_9709_figures("9709_w24_qp_33.pdf", "w24_33")
    extract_9709_figures("9709_w24_qp_53.pdf", "w24_53")
    extract_9709_figures("9709_s24_qp_11.pdf", "s24_11")
    extract_9709_figures("9709_s24_qp_31.pdf", "s24_31")
    extract_9709_figures("9709_s24_qp_51.pdf", "s24_51")
    extract_9709_figures("9709_s24_qp_12.pdf", "s24_12")
    extract_9709_figures("9709_s24_qp_32.pdf", "s24_32")
    extract_9709_figures("9709_s24_qp_52.pdf", "s24_52")
    extract_9709_figures("9709_s24_qp_13.pdf", "s24_13")
    extract_9709_figures("9709_s24_qp_33.pdf", "s24_33")
    extract_9709_figures("9709_s24_qp_53.pdf", "s24_53")
    extract_9709_figures("9709_m24_qp_12.pdf", "m24_12")
    extract_9709_figures("9709_m24_qp_32.pdf", "m24_32")
    extract_9709_figures("9709_m24_qp_52.pdf", "m24_52")

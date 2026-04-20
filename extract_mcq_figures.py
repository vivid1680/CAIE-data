import os
import fitz

def extract_mcq_figures(pdf_path, paper_code):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    extracted_questions = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0]
        
        # Determine the y0 bounds for all Question numbers
        # Format: "X " where X is the question number
        question_bounds = {}
        for block in text_blocks:
            text = block[4].strip()
            # Often MCQ starts with "1 ", "24 ", etc
            parts = text.split(" ")
            if len(parts) > 0 and parts[0].isdigit():
                q_num = int(parts[0])
                if 1 <= q_num <= 40:
                    question_bounds[q_num] = block[1] # y0 of the question text
                    
        if not question_bounds:
            continue
            
        sorted_qs = sorted(question_bounds.keys())
        
        # Get graphical bounds
        drawings = page.get_drawings()
        images = page.get_images()
        
        # Compute combined bounding box for graphics in different vertical regions
        for i, q_num in enumerate(sorted_qs):
            y_start = question_bounds[q_num]
            # y_end is either start of next question, or bottom of page
            y_end = question_bounds[sorted_qs[i+1]] if i+1 < len(sorted_qs) else page.rect.height
            
            # Find any graphical elements in this range
            has_graphics = False
            crop_rect = fitz.Rect()
            
            for path in drawings:
                b = path['rect']
                if b.is_empty: continue
                # if the drawing resides mostly inside this question vertically
                if b.y0 >= y_start and b.y1 <= y_end:
                    if not has_graphics:
                        crop_rect = b
                        has_graphics = True
                    else:
                        crop_rect |= b # merge rects
            
            # Check for actual images (like JPEGs)
            for img in page.get_image_info():
                b = fitz.Rect(img['bbox'])
                if b.y0 >= y_start and b.y1 <= y_end:
                    if not has_graphics:
                        crop_rect = b
                        has_graphics = True
                    else:
                        crop_rect |= b
                        
            # Many MCQ questions have large gaps containing purely text boxes inside the diagram.
            # Thus, we should scan text blocks that are between y_start and y_end, and if they 
            # don't seem like standard question prose (or if a graphic was detected), we optionally expand our crop.
            
            # For pure stability, if there is a gap > 100 points between text blocks inside this question,
            # or if drawings exist, let's just physically crop the bounds of the graphics with a small padding!
            if has_graphics:
                # Add slight padding
                crop_rect = fitz.Rect(max(0, crop_rect.x0 - 10), max(0, crop_rect.y0 - 10), 
                                      min(page.rect.width, crop_rect.x1 + 10), min(page.rect.height, crop_rect.y1 + 10))
                
                # Filter out false positives (tiny dots/lines)
                if crop_rect.width > 20 and crop_rect.height > 20:
                    filename = f"9702_{paper_code}_q{q_num}.png"
                    filepath = os.path.join(output_dir, filename)
                    pix = page.get_pixmap(clip=crop_rect, dpi=200)
                    pix.save(filepath)
                    print(f"Extracted graphical diagram for Q{q_num} -> {filename}")
                    extracted_questions.append(q_num)

    print("Extraction list: ", extracted_questions)

if __name__ == "__main__":
    extract_mcq_figures("9702_m24_qp_12.pdf", "m24_qp_12")

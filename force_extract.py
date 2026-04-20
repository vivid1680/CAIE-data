import os
import fitz

def force_extract(pdf_path, paper_code):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    diagram_qs = [3, 6, 12, 18, 25, 29, 35, 38]
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0]
        text_blocks.sort(key=lambda x: x[1])
        
        q_map = {}
        for block in text_blocks:
            text = block[4].strip()
            parts = text.split(" ")
            if len(parts) > 0 and parts[0].isdigit():
                q_num = int(parts[0])
                if 1 <= q_num <= 40 and str(q_num) == parts[0]:
                    if q_num not in q_map:
                        q_map[q_num] = []
            if q_map:
                latest_q = list(q_map.keys())[-1]
                q_map[latest_q].append(block)
                
        for q_num, q_blocks in q_map.items():
            if q_num in diagram_qs:
                # Force crop from the start of the 2nd block to the start of the 2nd to last block 
                # (which usually chops off the question text and the bottom options)
                if len(q_blocks) > 3:
                    y0 = q_blocks[1][3] # bottom of the question text
                    y1 = q_blocks[-1][1] # top of the very last block (e.g. D option)
                    
                    # Ensure minimum height
                    if y1 - y0 < 40:
                        y0 = q_blocks[0][3]
                    
                    crop_rect = fitz.Rect(30, max(0, y0 - 10), page.rect.width - 30, min(page.rect.height, y1 + 10))
                    
                    filename = f"9702_{paper_code}_q{q_num}.png"
                    filepath = os.path.join(output_dir, filename)
                    pix = page.get_pixmap(clip=crop_rect, dpi=200)
                    pix.save(filepath)
                    print(f"Force Extracted Q{q_num} -> {filename}")

if __name__ == "__main__":
    force_extract("9702_m24_qp_12.pdf", "m24_qp_12")

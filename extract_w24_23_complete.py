import os
import fitz
import re

def extract_complete_figures(pdf_path, paper_code):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    extracted_count = 0
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0]
        text_blocks.sort(key=lambda x: x[1])
        
        for i, block in enumerate(text_blocks):
            text = block[4].strip()
            # Match "Fig. X.Y"
            if re.match(r"Fig\.\s*(\d+)\.(\d+)", text) and len(text) < 100:
                fig_match = re.search(r"Fig\.\s*(\d+)\.(\d+)", text)
                fig_num = f"{fig_match.group(1)}_{fig_match.group(2)}"
                print(f"Processing Fig.{fig_num} on Page {page_num+1}...")
                
                caption_y0 = block[1]
                
                # Context Finding logic
                top_y = 0
                for j in range(i-1, -1, -1):
                    b_text = text_blocks[j][4].strip()
                    b_rect = fitz.Rect(text_blocks[j][:4])
                    
                    if (re.match(r"^\(\w\)", b_text) or 
                        re.match(r"^\d+\s+[A-Z]", b_text) or
                        "shown in Fig." in b_text or
                        "illustrated in Fig." in b_text or
                        "Determine" in b_text or
                        "Calculate" in b_text or
                        "sketch the variation" in b_text or
                        "State" in b_text):
                        
                        top_y = b_rect.y1
                        if caption_y0 - top_y > 40:
                            print(f"  Found boundary text at Y1={top_y:.1f}")
                            break
                        else:
                            top_y = 0

                if top_y == 0 or (caption_y0 - top_y) > 650:
                    top_y = max(0, caption_y0 - 350)
                
                # Vertical Slice Crop
                crop_rect = fitz.Rect(20, top_y - 8, page.rect.width - 20, caption_y0 + 2)
                
                filename = f"9702_{paper_code}_qp_fig{fig_num}.png"
                filepath = os.path.join(output_dir, filename)
                pix = page.get_pixmap(clip=crop_rect, dpi=200)
                pix.save(filepath)
                print(f"  -> Extracted Fig.{fig_num}: Y={top_y:.1f} to {caption_y0:.1f}")
                extracted_count += 1

    print(f"Total extracted: {extracted_count}")

if __name__ == "__main__":
    extract_complete_figures("data/9702_w24_qp_23.pdf", "w24_23")

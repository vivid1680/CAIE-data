import fitz
import re

def diagnose_figs(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0]
        text_blocks.sort(key=lambda x: x[1])
        
        drawings = page.get_drawings()
        
        for i, block in enumerate(text_blocks):
            text = block[4].strip()
            if re.match(r"Fig\.\s*\d+\.\d+", text) and len(text) < 50:
                print(f"\n--- Page {page_num+1} | Caption: {text} ---")
                caption_y0 = block[1]
                
                # Look for the last "major" text block above this caption
                # A major block usually starts with a question number or part (a), (b) etc.
                top_y = 0
                for j in range(i-1, -1, -1):
                    t = text_blocks[j][4].strip()
                    # Pattern for question parts: (a), (b), (i), (ii) or start of paper
                    if re.match(r"\(\w\)", t) or re.match(r"^\d+", t) or "Calculate" in t or "Show that" in t:
                        top_y = text_blocks[j][3] # Y1 of the block
                        print(f"  Preceding Question Text ends at Y={top_y:.1f}: {t[:40]}...")
                        break
                
                # Identify all content between top_y and caption_y0
                elements_rect = None
                
                # drawings
                for d in drawings:
                    dr = d['rect']
                    if dr.y1 <= caption_y0 + 2 and dr.y0 >= top_y - 10:
                        if elements_rect is None: elements_rect = dr
                        else: elements_rect |= dr
                
                # text blocks (labels inside the diagram)
                for b in text_blocks:
                    br = fitz.Rect(b[:4])
                    if br.y1 <= caption_y0 + 2 and br.y0 >= top_y - 2:
                        # Exclude the caption itself
                        if br.y0 == caption_y0: continue 
                        if elements_rect is None: elements_rect = br
                        else: elements_rect |= br
                
                if elements_rect:
                    print(f"  Content Box: {elements_rect}")
                    print(f"  Proposed Crop: Y from {elements_rect.y0-10:.1f} to {elements_rect.y1+5:.1f}")
                else:
                    print("  NO ELEMENTS DETECTED IN GAP!")

if __name__ == "__main__":
    diagnose_figs("9702_m24_qp_22.pdf")

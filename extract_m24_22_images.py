import os
import fitz
import re

def extract_m24_22_figures(pdf_path, paper_code):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    extracted_figs = {} # fig_num -> rect
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0]
        text_blocks.sort(key=lambda b: b[1])
        
        drawings = page.get_drawings()
        
        for i, block in enumerate(text_blocks):
            text = block[4].strip()
            
            # Simplified match for caption-like blocks
            match = re.match(r"Fig\.\s*(\d+)\.(\d+)(.*)", text)
            if match:
                fig_num = f"{match.group(1)}_{match.group(2)}"
                # Only use it if it looks like a caption (short or near bottom of a figure)
                if len(text) < 100:
                    print(f"Candidate caption: 'Fig.{match.group(1)}.{match.group(2)}' on page {page_num + 1}")
                    
                    caption_rect = fitz.Rect(block[:4])
                    
                    # Find drawings above the caption but below the previous block
                    y_limit_top = text_blocks[i-1][3] if i > 0 else 0
                    # Ensure limit top isn't too far
                    if caption_rect.y0 - y_limit_top > 500:
                        y_limit_top = caption_rect.y0 - 450
                    
                    relevant_drawings = []
                    for d in drawings:
                        d_rect = d['rect']
                        if d_rect.y1 <= caption_rect.y0 + 2 and d_rect.y0 >= y_limit_top - 10:
                            relevant_drawings.append(d_rect)
                    
                    if relevant_drawings:
                        union_rect = relevant_drawings[0]
                        for r in relevant_drawings[1:]:
                            union_rect |= r
                        
                        pad = 10
                        crop_rect = fitz.Rect(max(0, union_rect.x0 - pad), 
                                              max(0, union_rect.y0 - pad), 
                                              min(page.rect.width, union_rect.x1 + pad), 
                                              min(page.rect.height, union_rect.y1 + pad))
                        
                        extracted_figs[fig_num] = (page_num, crop_rect)
                    else:
                        # Fallback
                        crop_rect = fitz.Rect(40, max(0, caption_rect.y0 - 320), page.rect.width - 40, caption_rect.y0)
                        extracted_figs[fig_num] = (page_num, crop_rect)

    # Now save them (this avoids duplicates or overwriting with worse crops if we logic it right)
    count = 0
    for fig_num, (p_num, rect) in extracted_figs.items():
        filename = f"9702_{paper_code}_qp_fig{fig_num}.png"
        filepath = os.path.join(output_dir, filename)
        page = doc[p_num]
        pix = page.get_pixmap(clip=rect, dpi=200)
        pix.save(filepath)
        print(f"Saved {filepath}")
        count += 1

    print(f"Extraction complete: {count} figures extracted.")

if __name__ == "__main__":
    extract_m24_22_figures("9702_m24_qp_22.pdf", "m24_22")

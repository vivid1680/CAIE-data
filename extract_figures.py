import sys
import re
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF is not installed. Run 'pip install PyMuPDF'")
    sys.exit(1)

def extract_figures_from_pdf(pdf_path, paper_code):
    """
    Scans a PDF for 'Fig. X.Y' blocks, calculates the whitespace gap above it
    (which visually contains the diagram) and extracts that region as an image.
    """
    doc = fitz.open(pdf_path)
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)
    
    extracted_count = 0
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Get text blocks: list of tuples (x0, y0, x1, y1, "text", block_no, block_type)
        blocks = page.get_text("blocks")
        
        # Sort blocks vertically by y0
        # block_type == 0 means text block
        text_blocks = [b for b in blocks if b[6] == 0]
        text_blocks.sort(key=lambda b: b[1])
        
        # Iterate over blocks looking for "Fig. "
        for i, block in enumerate(text_blocks):
            text = block[4].strip()
            
            # Use regex to match something like "Fig. 1.1" or "Fig. 1.2"
            # It might have trailing spaces or other things
            match = re.search(r"Fig\.\s*(\d+)\.(\d+)", text)
            if match:
                fig_num = f"{match.group(1)}_{match.group(2)}"
                print(f"Found {text!r} on page {page_num + 1}")
                
                # We need to find the boundary of the image. The image is likely
                # between this "Fig. X.Y" block and the text block immediately preceding it.
                if i > 0:
                    prev_block = text_blocks[i-1]
                    
                    # Define crop coordinates
                    # Some diagrams could be wide. We'll capture the full page width minus margins
                    page_rect = page.rect
                    crop_x0 = 40  # Left margin
                    crop_x1 = page_rect.width - 40  # Right margin
                    
                    # crop 300 points directly above the Fig caption
                    crop_y1 = block[1]
                    crop_y0 = max(0, crop_y1 - 320)
                    
                    crop_rect = fitz.Rect(crop_x0, crop_y0, crop_x1, crop_y1)
                    
                    # Generate the image of this specific rectangle
                    pix = page.get_pixmap(clip=crop_rect, dpi=200) # 200 DPI for good quality
                    
                    # Format the output filename as requested (e.g., 9702_w25_qp_42_fig1_1.png)
                    filename = os.path.join(output_dir, f"9702_{paper_code}_qp_fig{fig_num}.png")
                    
                    # Save it
                    pix.save(filename)
                    print(f"  -> Saved {filename}")
                    extracted_count += 1

    print(f"Extraction complete for {pdf_path}: {extracted_count} figures extracted.")

if __name__ == "__main__":
    # Test on the w25_22 paper
    if os.path.exists("9702_w25_qp_22.pdf"):
        print("Processing w25_22...")
        extract_figures_from_pdf("9702_w25_qp_22.pdf", "w25_22")
        
    print("-" * 30)
    
    # Test on the w25_42 paper
    if os.path.exists("9702_w25_qp_42.pdf"):
        print("Processing w25_42...")
        extract_figures_from_pdf("9702_w25_qp_42.pdf", "w25_42")
        
    print("-" * 30)
    
    # Test on the w25_12 paper
    if os.path.exists("9702_w25_qp_12.pdf"):
        print("Processing w25_12...")
        # Note paper 12 might not use "Fig.", MCQ papers just have gaps or question numbers.
        # But if it does have any Fig. X.Y this will catch it!
        extract_figures_from_pdf("9702_w25_qp_12.pdf", "w25_12")

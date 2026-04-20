import fitz
import os

def extract_mcq_diagrams(pdf_path, paper_code, questions):
    doc = fitz.open(pdf_path)
    output_dir = os.path.join("data", "images")
    os.makedirs(output_dir, exist_ok=True)
    
    for q_num in questions:
        print(f"Searching for Question {q_num}...")
        found = False
        for page_num in range(len(doc)):
            page = doc[page_num]
            # Search for the question number at the start of a line
            text_instances = page.search_for(str(q_num), clip=fitz.Rect(0, 0, 100, page.rect.height))
            
            for inst in text_instances:
                # Check if it's really the start of the question (near left margin)
                if inst.x0 < 60:
                    start_y = inst.y0
                    # Find the next question to define the crop area
                    next_q = q_num + 1
                    next_inst = page.search_for(str(next_q), clip=fitz.Rect(0, start_y + 10, 100, page.rect.height))
                    
                    if next_inst:
                        end_y = next_inst[0].y0
                    else:
                        # If it's the last question on the page or the paper
                        end_y = page.rect.height - 50 
                    
                    # Vertical Slice Crop
                    crop_rect = fitz.Rect(30, start_y - 5, page.rect.width - 30, end_y - 5)
                    
                    filename = f"9702_{paper_code}_qp_fig{q_num}.png"
                    filepath = os.path.join(output_dir, filename)
                    pix = page.get_pixmap(clip=crop_rect, dpi=200)
                    pix.save(filepath)
                    print(f"  -> Extracted Q{q_num} on Page {page_num+1}")
                    found = True
                    break
            if found: break

if __name__ == "__main__":
    q_with_diagrams = [4, 6, 7, 8, 11, 13, 14, 18, 20, 23, 25, 28, 29, 33, 34, 35, 36, 37, 38]
    extract_mcq_diagrams("9702_w25_qp_11.pdf", "w25_11", q_with_diagrams)

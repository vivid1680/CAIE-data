import sys
import os
from PyPDF2 import PdfReader

def dump_pdf(pdf_path, output_path):
    print(f"Reading {pdf_path}")
    if not os.path.exists(pdf_path):
        print("File not found.")
        return
        
    reader = PdfReader(pdf_path)
    text = ""
    for idx, page in enumerate(reader.pages):
        text += f"\n---PAGE {idx+1}---\n"
        page_text = page.extract_text()
        if page_text:
            text += page_text
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Dumped to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dump_pdf.py <input.pdf> <output.txt>")
        sys.exit(1)
    dump_pdf(sys.argv[1], sys.argv[2])

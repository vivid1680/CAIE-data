import sys
import os
import fitz

def dump_pdf_fitz(pdf_path, output_path):
    print(f"Reading {pdf_path} using fitz")
    if not os.path.exists(pdf_path):
        print("File not found.")
        return
        
    doc = fitz.open(pdf_path)
    text = ""
    for idx, page in enumerate(doc):
        text += f"\n---PAGE {idx+1}---\n"
        text += page.get_text()
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Dumped to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dump_fitz.py <input.pdf> <output.txt>")
        sys.exit(1)
    dump_pdf_fitz(sys.argv[1], sys.argv[2])

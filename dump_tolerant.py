import sys
from PyPDF2 import PdfReader

def dump_pdf_tolerant(pdf_path, txt_path):
    print(f"Reading {pdf_path} tolerantly")
    reader = PdfReader(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            f.write(f"\n---PAGE {i+1}---\n")
            try:
                page_text = page.extract_text()
                f.write(page_text)
            except Exception as e:
                f.write(f"\n[ERROR EXTRACTING PAGE {i+1}: {e}]\n")
    print(f"Dumped to {txt_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dump_tolerant.py <pdf> <txt>")
    else:
        dump_pdf_tolerant(sys.argv[1], sys.argv[2])

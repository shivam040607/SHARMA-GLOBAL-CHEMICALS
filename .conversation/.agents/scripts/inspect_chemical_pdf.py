from pathlib import Path
import fitz

pdf_path = Path("attached_assets/Industrial_chemicals_20260903_211938_0000_1788583574710.pdf")
render_dir = Path(".agents/outputs/chemical_pdf_pages")
render_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"pages={doc.page_count}")
print(f"metadata={doc.metadata}")

for index, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    output_path = render_dir / f"page-{index + 1}.png"
    pix.save(output_path)
    print(f"rendered={output_path} size={page.rect.width}x{page.rect.height}")
    print(f"--- PAGE {index + 1} TEXT ---")
    print(page.get_text("text"))
    print(f"--- PAGE {index + 1} BLOCKS ---")
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") == 0:
            text = " ".join(
                span["text"]
                for line in block.get("lines", [])
                for span in line.get("spans", [])
            ).strip()
            if text:
                print(text)
#                  -----INFO----
# this is the free local alternative to the OpenAI version
# runs on your own machine via Ollama, no API key, no billing
# requires: ollama pull llama3.2-vision  (already pulling)
# note: vision models read PDFs as IMAGES, not raw files directly
# so we render each PDF page to a PNG first using PyMuPDF, then feed that to Ollama


import pymupdf
import ollama

pdf_path = "Parsing_PDF_using_LLM/sample.pdf"
doc = pymupdf.open(pdf_path)

extracted_pages = []

for page_index in range(len(doc)):
    page = doc[page_index]

    # render the page to an image (higher zoom = higher resolution = better OCR-like reading)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
    image_path = f"page_{page_index}.png"
    pix.save(image_path)

    response = ollama.chat(
        model="llama3.2-vision",
        messages=[
            {
                "role": "user",
                "content": "Extract the text content from this page. Exclude texts from tables or images.",
                "images": [image_path]
            }
        ]
    )

    page_text = response["message"]["content"]
    extracted_pages.append(page_text)

    print(f"--- Page {page_index} ---")
    print(page_text)

# join all pages together with a page delimiter, same idea as PyMuPDF's form feed marker
full_text = "\x0c".join(extracted_pages)
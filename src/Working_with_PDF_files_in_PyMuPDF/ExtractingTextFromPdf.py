import pymupdf

doc = pymupdf.open("Working_with_PDF_files_in_PyMuPDF/a.pdf") # opens a document 

out = open("output.txt", "wb") # creating text output

for page in doc : # for each page in the doc
    text = page.get_text("text",sort=True).encode("utf-8") # get plain text that is in utf-8
    out.write(text) # write text of page
    out.write(bytes((12,))) # write the page delimeter (some sort of "go to next page")
out.close()


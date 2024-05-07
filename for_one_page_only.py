from PyPDF2 import PdfReader

# Open the PDF file
reader = PdfReader('F:\coding\web Projects\Python Projects\Text_extraction_from_pdf\Practical Python and OpenCV, 3rd Edition.pdf') #book path here

# Choose the page you want to extract (e.g., page 50)
page_number = 50
page = reader.pages[page_number]

# Extract text from the chosen page
extracted_text = page.extract_text()

# Create a new text file to save the extracted text
with open('extracted_text_page_{}.txt'.format(page_number), 'w', encoding='utf-8') as f:
    f.write(extracted_text)

# Print the extracted text
print(extracted_text)

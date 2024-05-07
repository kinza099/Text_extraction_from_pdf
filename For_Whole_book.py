from PyPDF2 import PdfReader

# Open the PDF file
reader = PdfReader('F:\coding\web Projects\Python Projects\Text_extraction_from_pdf\Practical Python and OpenCV, 3rd Edition.pdf') #give Book path here

# Create a new text file to save the extracted text
with open('extracted_text.txt', 'w', encoding='utf-8') as f:
    # Loop through each page of the PDF
    for i, page in enumerate(reader.pages):
        # Extract text from the current page
        text = page.extract_text()
        
        # Write the text to the file along with the page number
        f.write(f'\nPage number: {i + 1}\n')
        f.write(text)

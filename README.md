# PDF Text Extraction

This repository contains Python scripts that demonstrate how to extract text from PDF files using the PyPDF2 library.

## Requirements

- Python 3.x
- PyPDF2 library (install using `pip install PyPDF2`)

## Usage

### Extracting Text from All Pages

The script `extract_text_all_pages.py` extracts text from all pages of a PDF file and saves it to a single text file.

To run the script, use the following command:

python extract_text_all_pages.py


### Extracting Text from a Specific Page

The script `extract_text_single_page.py` extracts text from a specific page of a PDF file and saves it to a text file.

To run the script, you need to specify the page number you want to extract. Use the following command:
python extract_text_single_page.py


Make sure to replace the file path in the scripts with the path to your PDF file.

## Output

- For the `extract_text_all_pages.py` script, the extracted text from each page will be saved to a single text file named `extracted_text.txt`.

- For the `extract_text_single_page.py` script, the extracted text will be saved to a text file named `extracted_text_page_{page_number}.txt`, where `{page_number}` is the specified page number.

## Note

- Ensure that the PyPDF2 library is installed before running the scripts.
- If you encounter any issues, feel free to open an issue on GitHub.



# PDF Text Extractor

PDF Text Extractor is a Python script that allows users to extract text from specified pages of a PDF document. It provides a convenient command-line interface for specifying the PDF file path, the range of pages to extract from, and the output file path where the extracted text will be saved.

## Features

- Extract text from a range of pages in a PDF file.
- Save extracted text to a specified output file.
- Easy to use command-line interface.

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later installed on your system.
- `pip` for installing Python packages.

### Steps

1. Clone the repository or download the script to your local machine.
2. Install the required package `PyMuPDF` by running:
   ```bash
   pip install pymupdf
   ```

## Usage

To use the PDF Text Extractor, navigate to the directory containing the script and run it using the following syntax:

```bash
python extract_pdf_text.py <pdf_path> <start_page> <end_page> <output_file>
```

### Parameters:

- `<pdf_path>`: Path to the PDF file from which to extract text.
- `<start_page>`: The starting page number for extraction (0-indexed).
- `<end_page>`: The ending page number for extraction (0-indexed, inclusive).
- `<output_file>`: Path to the output file where the extracted text will be saved.

### Example:

```bash
python extract_pdf_text.py my_document.pdf 0 5 extracted_text.txt
```

This command will extract text from pages 1 to 6 of `my_document.pdf` and save it to `extracted_text.txt`.

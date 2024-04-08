import argparse
import fitz  # PyMuPDF

def extract_text_from_range(pdf_path, start_page, end_page):
    """
    Extracts text from a range of pages in a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.
        start_page (int): The starting page number, 0-indexed.
        end_page (int): The ending page number, 0-indexed and inclusive.

    Returns:
        str: The extracted text from the specified range of pages.
    """
    text = ""
    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        for page_num in range(start_page, end_page + 1):
            # Check if page number is valid
            if page_num < len(doc):
                # Get the page
                page = doc.load_page(page_num)
                # Extract text from the page
                text += page.get_text() + "\n\n"
            else:
                print(f"Page {page_num + 1} is out of range.")
    return text

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Extract text from specified pages of a PDF and save to a file.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("start_page", type=int, help="Starting page number (0-indexed)")
    parser.add_argument("end_page", type=int, help="Ending page number (0-indexed, inclusive)")
    parser.add_argument("output_file", help="Path to the output text file")

    # Parse the arguments
    args = parser.parse_args()

    # Extract the text
    extracted_text = extract_text_from_range(args.pdf_path, args.start_page, args.end_page)

    # Write the extracted text to the specified output file
    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write(extracted_text)
    print(f"Extracted text has been saved to {args.output_file}")

if __name__ == "__main__":
    main()

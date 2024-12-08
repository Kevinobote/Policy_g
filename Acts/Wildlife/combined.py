from PyPDF2 import PdfReader
import os

def extract_text_from_pdfs_to_single_file(folder_path, output_file):
    """
    Extracts text from all PDFs in a folder and saves to a single output file.
    Skips files that cannot be processed due to errors.

    Args:
        folder_path (str): Path to the folder containing PDFs.
        output_file (str): Path to save the combined text output.
    """
    skipped_files = []  # To log files that were skipped due to errors
    with open(output_file, "w", encoding="utf-8") as output:
        for filename in os.listdir(folder_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(folder_path, filename)
                try:
                    # Try reading the PDF
                    reader = PdfReader(file_path)
                    text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
                    # Write extracted text to the output file
                    output.write(f"--- Start of {filename} ---\n")
                    output.write(text)
                    output.write(f"\n--- End of {filename} ---\n")
                    print(f"Processed: {filename}")
                except Exception as e:
                    # Catch all exceptions and skip the file
                    skipped_files.append((filename, str(e)))
                    print(f"Skipped {filename} due to error: {e}")

    # Log skipped files
    if skipped_files:
        print("\nSkipped files:")
        for file, error in skipped_files:
            print(f"- {file}: {error}")

# Usage
folder_path = os.getcwd()  # Use the current working directory
output_file = os.path.join(folder_path, "combined_wildlife.txt")
extract_text_from_pdfs_to_single_file(folder_path, output_file)

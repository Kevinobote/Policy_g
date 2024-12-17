# PDF Text Extraction and Combination Tool

This project provides a set of Python scripts for extracting text from PDF files and combining the extracted content into a single text file. It is designed to process multiple PDF files across various categories of legal acts, including Biosafety, Climate, Energy Laws, Environment, Fisheries, Forestry, Land, Mining, Water, and Wildlife.

## Repository Structure

The repository is organized into the following structure:

```
.
├── Acts
│   ├── Biosafety
│   ├── Climate
│   ├── EnergyLaws
│   ├── Environment
│   ├── Fisheries
│   ├── Forestry
│   ├── Land
│   ├── Mining
│   ├── water
│   ├── Wildlife
│   └── download.py
├── combined.py
└── test.py
```

### Key Files:

- `combined.py`: The main script for extracting text from PDFs and combining them.
- `Acts/download.py`: A script for downloading PDF files from a specific webpage.
- `Acts/[Category]/combined.py`: Category-specific scripts for text extraction and combination.

## Usage Instructions

### Installation

1. Ensure you have Python 3.6 or later installed.
2. Install the required libraries:

```bash
pip install PyPDF2 requests beautifulsoup4
```

### Getting Started

1. To download PDF files:
   - Navigate to the `Acts` directory.
   - Run the `download.py` script:

     ```bash
     python download.py
     ```

   This will download PDF files to a `forestry` folder in the root directory.

2. To extract and combine text from PDFs:
   - Navigate to the directory containing the PDF files you want to process.
   - Run the appropriate `combined.py` script:

     ```bash
     python combined.py
     ```

   This will create a combined text file in the same directory.

### Common Use Cases

1. Extracting text from all PDFs in the current directory:

```python
import os
from combined import extract_text_from_pdfs_to_single_file

folder_path = os.getcwd()
output_file = os.path.join(folder_path, "combined_output.txt")
extract_text_from_pdfs_to_single_file(folder_path, output_file)
```

2. Processing PDFs from a specific category:

```python
import os

category = "Biosafety"
folder_path = os.path.join("Acts", category)
output_file = os.path.join(folder_path, f"combined_{category.lower()}.txt")
extract_text_from_pdfs_to_single_file(folder_path, output_file)
```

### Troubleshooting

- If you encounter `PyPDF2.errors.PdfReadError`, ensure the PDF file is not corrupted or password-protected.
- For `UnicodeDecodeError`, try specifying the correct encoding when opening the output file.

### Debugging

To enable verbose logging:

1. Add the following import at the beginning of the script:

```python
import logging
```

2. Set the logging level to DEBUG:

```python
logging.basicConfig(level=logging.DEBUG)
```

3. Add log statements in the `extract_text_from_pdfs_to_single_file` function:

```python
logging.debug(f"Processing file: {filename}")
```

Log files will be output to the console. To save logs to a file, modify the `logging.basicConfig` call:

```python
logging.basicConfig(filename='pdf_extraction.log', level=logging.DEBUG)
```

## Data Flow

The data flow in this application follows these steps:

1. PDF files are downloaded from a specified webpage using `Acts/download.py`.
2. The `combined.py` script (or category-specific scripts) reads PDF files from a specified folder.
3. Each PDF file is processed using PyPDF2 to extract text content.
4. Extracted text is written to a single output file, with each PDF's content separated by headers.
5. Any errors during processing are logged, and problematic files are skipped.

```
[Web Source] -> [download.py] -> [PDF Files] -> [combined.py] -> [Extracted Text] -> [Combined Output File]
```

Note: Error handling is implemented to ensure the process continues even if individual files fail to process.
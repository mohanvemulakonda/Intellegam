# PDF to Markdown Conversion Using Anthropic API and PyMuPDF

## Overview
This project demonstrates how to convert text extracted from a PDF document into Markdown format using the Anthropic API and PyMuPDF. The program reads the contents of a PDF file, processes the extracted text, and converts it into Markdown format.

## Features
- Extract text from a PDF document using the `PyMuPDF` library.
- Use the Anthropic API to convert the extracted text into Markdown.
- Save the converted Markdown content into a file.

## Requirements
- Python 3.x
- Anthropic API Key
- PyMuPDF (`fitz`)
- Anthropic Python SDK

## Installation

1. Install PyMuPDF:
   ```bash
   pip install PyMuPDF
2. Install the Anthropic Python SDK:
   ```bash
   pip install anthropic
3. Clone this repository and navigate to the project directory:
```bash
git clone <repository-url>
cd <repository-directory>
`````````

## Setup

**Anthropic API Key**: You will need to sign up for access to Anthropic’s API and obtain an API key. Replace the placeholder `api_key` in the code with your actual key:

```python
client = anthropic.Anthropic(api_key="your-api-key-here")
```
##Usage

Once the necessary dependencies are installed and API credentials are configured, you can run the program to convert your PDF document into Markdown format.

bash
Copy code
python main.py
Example
The provided code demonstrates how to convert a sample PDF into a Markdown file:

python
Copy code
# usage
pdf_path = "/content/Owners Manual.pdf"
document = pdf_to_markdown(pdf_path)

# Write the output to a markdown file
file_name = "hilti.md"
with open(file_name, "w") as file:
    file.write(document)
After running the program, you should find the extracted content from the PDF saved as a Markdown file (owner.md).

Code Overview

Functions
read_pdf(pdf_path): Reads and extracts text from the specified PDF file.
convert_text_to_markdown(text): Sends the extracted text to the Anthropic API and converts it to Markdown format.
pdf_to_markdown(pdf_path): Combines the above two functions to read a PDF and convert its contents into Markdown format.
Usage Example
python
Copy code
# Convert a PDF to Markdown and save to file
pdf_path = "/content/Technisches Handbuch-Befestigungstechnik.pdf"
markdown_content = pdf_to_markdown(pdf_path)

# Save the markdown content to a file
with open("hilti.md", "w") as file:
    file.write(markdown_content)
Notes

Make sure that your Anthropic API key is kept secure and not exposed in public repositories.
Test the code with different PDFs, especially large files, to verify performance and formatting.

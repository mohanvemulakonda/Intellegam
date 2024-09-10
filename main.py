https://colab.research.google.com/gist/mohanvemulakonda/09614f0fdd0084081123cc7dc2146e3c/intellegam-pdf-to-md-claude.ipynb
#Anthropic API case
#install PyMuPDF & Anthropic
#reading the PDF
import fitz  # PyMuPDF

def read_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

#sending text to Anthropic API

import anthropic

# Initialize the client
client = anthropic.Anthropic(api_key="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")

def convert_text_to_markdown(text):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"Convert the following text to Markdown format:\n\n{text}"}
        ]
    )
    return message.content

#combination

def pdf_to_markdown(pdf_path):
    # Step 1: Read the PDF
    pdf_text = read_pdf(pdf_path)
    
    # Step 2: Convert text to Markdown
    markdown_content = convert_text_to_markdown(pdf_text)
    
    return markdown_content

# usage
pdf_path = "/content/Owners Manual.pdf"
document = pdf_to_markdown(pdf_path)
print(markdown)

#check
print(document[0].text[:5000])

#add file

file_name="owner.md"
with open(file_name, "w") as file:
    file.write(document[0].text)

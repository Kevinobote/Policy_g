import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# URL of the webpage containing PDF links
url = 'https://new.kenyalaw.org/akn/ke/act/2016/34/eng@2022-12-31'

# Create a "forestry" folder in the root directory
root_folder = os.getcwd()  # Get the current working directory
folder_location = os.path.join(root_folder, 'forestry')
if not os.path.exists(folder_location):
    os.makedirs(folder_location)

# Fetch the content of the webpage
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Parse the webpage content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links ending with .pdf
pdf_links = soup.find_all('a', href=lambda href: href and href.lower().endswith('.pdf'))

for link in pdf_links:
    # Get the full URL of the PDF file
    pdf_url = urljoin(url, link['href'])
    # Get the filename by splitting the URL path
    filename = os.path.join(folder_location, os.path.basename(link['href']))
    # Download the PDF file
    with requests.get(pdf_url, stream=True) as pdf_response:
        pdf_response.raise_for_status()
        with open(filename, 'wb') as pdf_file:
            for chunk in pdf_response.iter_content(chunk_size=8192):
                if chunk:
                    pdf_file.write(chunk)
    print(f'Downloaded: {filename}')

from PIL import Image
from pytesseract import pytesseract
import os

# Define the path to tesseract.exe => which i installed on my pc after downloading
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the path to images folder
path_to_images = r'images'

# point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):
    # iterate over the each file in the folder
    for file_name in file_names:

        # Open image with PIL
        img = Image.open(path_to_images + '/' + file_name)

        # convert image to text string / Extract text from image
        text = pytesseract.image_to_string(img)
        
        # Append that Extracted Text in .txt file
        with open('extractedText.txt', 'a') as file:
            file.write(text)       
            print(text)

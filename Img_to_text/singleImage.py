from PIL import Image
from pytesseract import pytesseract

# Define the path to tesseract.exe => which i installed on my pc after downloading
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the path to images folder
path_to_image = 'images/download3.png'

# point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open the image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(img)

# Print that extracted text
print(text)
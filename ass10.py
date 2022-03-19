import img2pdf
from PIL import Image
import os

# storing image path
img_path = "/Users/neelpatel/Desktop/sem4/sem3mark.png"

# storing pdf path
pdf_path = "/Users/neelpatel/Desktop/sem4/file.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()
file.close()
print("successfully made pdf")

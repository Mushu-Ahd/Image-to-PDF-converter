import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

input_directory = input("Enter the Images location please...\n")

output_pdf_location = input("Enter the PDF file location you want to save it in...\n")

input_files = os.listdir(input_directory)

canvas_pdf = canvas.Canvas(output_pdf_location, pagesize=letter)

for filename in input_files:
    if filename.lower().endswith(('.png','.jpg','.jpeg','.gif')):
        image = Image.open(os.path.join(input_directory,filename))
        width, height = image.size
        aspect_ratio = width/float(height)
        target_width = 500
        target_height = target_width/aspect_ratio
        canvas_pdf.drawImage(os.path.join(input_directory,filename), x=50 , y=550, width=target_width , height=target_height)

        if filename != input_files[-1]:
            canvas_pdf.showPage()
canvas_pdf.save()

print(f'The Images has been converted into {output_pdf_location}')

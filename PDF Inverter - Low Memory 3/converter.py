# Step1 - Make Image of all pages
# Step2 - Invert the images
# Step3 - Make pdf from all the images

import fitz
from PIL import Image, ImageOps
import os

total_pages = None

def invertPagePdf(source):
    global total_pages
    pdf = fitz.open(source)
    total_pages = pdf.page_count

    for x in range(0,total_pages):
        page = pdf.load_page(x)
        pix = page.get_pixmap()
        pix.pil_save(f"img_page{x}.png")
        img = Image.open(f"img_page{x}.png")
        img = ImageOps.invert(img)
        img.save(f"inv_page{x}.png")
        os.remove(f"img_page{x}.png")
        del page
        del pix
        del img

    for x in range(0,total_pages):
        img = Image.open(f"inv_page{x}.png")
        pdf_image = img.convert("RGB").save(f"pdf_page{x}.pdf")
        del img
        del pdf_image
        os.remove(f"inv_page{x}.png")

def generateInvertedPDF(output):

    inverted_pdf = fitz.open()

    for x in range(0,total_pages):
        i = fitz.open(f"pdf_page{x}.pdf")
        inverted_pdf.insert_pdf(i, from_page=1, to_page=1)
        del i
        os.remove(f"pdf_page{x}.pdf")

    inverted_pdf.save(output)
    del inverted_pdf



#invertPagePdf("pd.pdf")
#print(total_pages)
#generateInvertedPDF("Final.pdf")

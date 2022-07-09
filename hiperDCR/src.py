from pdf2image import convert_from_path
from PIL import Image

pages = convert_from_path('C:\www\hiperDCR\pdfs\sample01.pdf', 500, poppler_path=r'C:\www\poppler-0.68.0_x86\poppler-0.68.0\bin')

for i, image in enumerate(pages):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")


im = Image.open('C:\www\hiperDCR\pngs\image1.png')
im_crop = im.crop((60, 20, 400, 200))
im_crop.save('C:\www\hiperDCR\pngs\image1_crop.png', quality=95)
im_crop.show()
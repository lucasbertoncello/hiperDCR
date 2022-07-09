from email.headerregistry import ContentTypeHeader
from pdf2image import convert_from_path
from PIL import Image
import requests

class Image_processing:

    def pdf2png_crop():

        pages = convert_from_path('C:\www\hiperDCR2\sample01.pdf', 500, poppler_path=r'C:\www\poppler-0.68.0_x86\poppler-0.68.0\bin')

        for i, image in enumerate(pages):
            fname = 'image'+str(i)+'.png'
            image.save(fname, "PNG")

        im = Image.open('C:\www\hiperDCR2\image1.png')
        im_crop = im.crop((3299,12,4034,288))
        im_crop.save('C:\www\hiperDCR2\image1_crop.png', quality=95)

        campo = "378,79"
        url = f"http://localhost:54226/ocr?valorComparacao={campo}"

        files = {
            'arquivo': open('C:\www\hiperDCR2\image1_crop.png', 'rb'),
        }
        response = requests.post(url, files=files, verify=False)

        status_code = response.status_code

        if status_code != 200:
            raise SystemError(
                "Bad response from Processing: {!r} / {!r} / {!r}".format(response.status_code, response.headers, response.text)
            )
       
        return response.json()
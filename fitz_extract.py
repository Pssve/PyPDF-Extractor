import fitz

file = fitz.open('pdftest1.pdf')


#text extraction by page
for pageNumber, page in enumerate (file.pages(), start = 1):
    text = page.getText()
    txt = open(f'report_Page_{pageNumber}.txt', 'a')
    txt.writelines(text)
    txt.close()


#this is for extracting images. Currently it does not work as all images extracted are blank images.
for pageNumber, page in enumerate(file.pages(), start=1):
    for imgNumber, img in enumerate(page.getImageList(), start=1):
        xref = img[0]
        pix = fitz.Pixmap(file, xref)
        if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.writePNG(f'image_Page{pageNumber}_{imgNumber}.png')

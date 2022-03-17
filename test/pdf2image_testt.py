import pdf2image as pdf

pages = pdf.convert_from_path(r'C:\Users\Benja\Code\Python\Kassenzettel\test\Doc Feb 28 2022.pdf')

for i in range(len(pages)):
    pages[i].save(r'C:\Users\Benja\Code\Python\Kassenzettel\test\page_new'+ str(i) +'.jpg', 'JPEG')
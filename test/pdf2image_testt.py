import pdf2image as pdf

pages = pdf.convert_from_path(r'C:\Users\Benja\Code\Python\Kassenzettel\test\Doc Feb 26 2022(1).pdf')

for i in range(len(pages)):
    pages[i].save(r'C:\Users\Benja\Code\Python\Kassenzettel\test\page'+ str(i) +'.jpg', 'JPEG')
import glob
import PyPDF2 as pdf
import text_recognition
import textract

files = glob.glob(r"C:\Users\Benja\Code\Python\Kassenzettel\test\*.pdf") #r"C:\Users\Benja\Code\Python\Kassenzettel\test\*.pdf")
print(files)
# pdf_reader = pdf.PdfFileReader(files[0])
# for page in pdf_reader.pages:
#     print(page.getContents())

# test = textract.process(files[1])#, encoding='utf-8', language='deu')#.decode()
# print(test)

files = glob.glob(r"C:\Users\Benja\Code\Python\Kassenzettel\test\*.jpg")
print (files[2])
text = text_recognition.img_to_text(files[2])

print('Der Kassenzettel sagt: ')
print(text)
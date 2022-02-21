import PyPDF2 as pdf
import os
import glob
import datetime
from dataclasses import dataclass


path = r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\Input"
files = glob.glob(path)

for file in files:
    pdf_reader = pdf.PdfFileReader(file)

@dataclass
class receipt:
    name: str
    date: datetime.datetime
    items: list

@dataclass
class item:
    name: str
    full_name: str
    prize: float
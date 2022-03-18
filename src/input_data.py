from gzip import READ
import PyPDF2 as pdf
import os
import glob
import datetime
import re
from dataclasses import dataclass


# path = r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\Input"
# files = glob.glob(path)

# for file in files:
#     pdf_reader = pdf.PdfFileReader(file)

class Data_extracter:
    
    def __init__(self, path):
        self.path = path
        self.name = None
        self.date = None
        self.items = list()
        self.data = None

    def txt_inputfile(self):
        with open(self.path, 'r') as file:
            self.data = file.readlines()
        return

    def extract_data(self):
        """Method to combine all data gathering routines."""
        self.name = self.extract_name()
        self.date = self.extract_date()
        self.items = self.extract_items()
        return Receipt(name=self.name, date=self.date, items=self.items)

    def extract_date(self):
        """Extract the date from the inputdata."""
        date_re = re.compile(r"\d\d.\d\d.\d\d\d\d")
        for line in self.data:
            temp = date_re.search(line)
            if temp != None:
                return datetime.datetime(year=int(temp[0][6:]),
                                         month=int(temp[0][3:5]), 
                                         day=int(temp[0][0:2]))

    def extract_name(self):
        """Extract the name of the job from the inputdata."""
        with open(r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\lookup\shops.txt", 'r') as shopfile:
            shoplist = shopfile.readlines()
            for shop in shoplist:
                for line in self.data:
                    if (line.find(shop) != -1):
                        return shop

    def extract_items(self):
        """Extract the itmes and the corresponding prices."""
        item_list=[]
        price_re = re.compile(r"\d+,\d\d")
        with open(r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\lookup\goods.txt", 'r') as goodsfile:
            goods = goodsfile.readlines()
            for good in goods:
                for line in self.data:
                    if (line.find(good) != -1):
                        item_list.append(
                            Item(name=good,
                                 prize=float(price_re.search(line)[0].replace(',', '.'))
                                 )
                            )
        return item_list


@dataclass
class Receipt:

    name: str
    date: datetime.datetime
    items: list

    
@dataclass
class Item:

    name: str
    # full_name: str
    prize: float
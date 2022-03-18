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
        # das könnte eine gute anwendung für decorators sein
        self.cleanup_lookup(r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\lookup\shops.txt")
        self.cleanup_lookup(r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\lookup\goods.txt")
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
            
            answer = self.ask_input(text=self.data, problem='Which shop is this from? : ')
            self.add_lookup(data=answer.upper(), path=r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\lookup\shops.txt")
            return answer

    def extract_items(self):
        """Extract the itmes and the corresponding prices."""
        item_list=[]
        price_re = re.compile(r"\d+,\d\d")
        with open(r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\lookup\goods.txt", 'r') as goodsfile:
            goods = goodsfile.readlines()
            for line in self.data:
                prc = price_re.search(line) 
                if prc != None:
                    for good in goods:
                        if (line.find(good) != -1):
                            item_list.append(
                                Item(name=good,
                                    prize=float(prc[0].replace(',', '.'))
                                )
                            )
                            break
                    
                    product = self.ask_input(text=line, problem='What product is that? : ')  # kann ich das über dekorator lösen?
                    self.add_lookup(data=product.upper(), path=r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\lookup\goods.txt")
        
        return item_list

    def ask_input(self, text, problem):
        """Ask the user for Input."""
        print('-------------------------------------------------------------------')
        print(text)
        return input(problem)
    
    def add_lookup(self, data, path):
        """Append the data to the lookup file."""
        with open(path, 'a') as file:
            file.write('\n')
            file.write(data)
            file.close()

    def cleanup_lookup(self, path):
        with open(path, 'r') as file:
            content = file.readlines()
            content = list(set(content))
            content.remove('\n')
            
        word = ""
        for good in content:
            word += good
        
        with open(path, 'w') as file:
            file.write(word)


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
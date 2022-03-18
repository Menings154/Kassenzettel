import input_data as id
import re

extracter = id.Data_extracter(r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\data\edeka_test_1.txt")
extracter.txt_inputfile()
kassenzettel = extracter.extract_data()
print(kassenzettel.name)
print(kassenzettel.date)
print(kassenzettel.items)

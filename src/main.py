import input_data as id
import re

extracter = id.Data_extracter(r"C:\Users\Benja\Code\Python\Kassenzettel\Folderstructure\data\edeka_test_1.txt")
extracter.txt_inputfile()
extracter.extract_data()
print(extracter.date)

print('Nice')
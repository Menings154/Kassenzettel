import cv2
import numpy as np
import pytesseract
from pytesseract import Output

path = r'C:\Users\Benja\Code\Python\Kassenzettel\test\page_new0.jpg'

img = cv2.imread(path)
print(img.shape)
img = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)

print(img.shape)
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
# cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

height = 10
myconfig = r"--psm 11 --oem 3"
#print(img.shape)

cv2.imshow('test', img)
cv2.waitKey(0)

for i in range(int(img.shape[0]/height)):
    cropped = img[i*height : (i+1)*height, 15:85]
    # cv2.imshow('test', cropped)
    # cv2.waitKey(0)
    data = pytesseract.image_to_data(cropped, output_type=Output.DICT,
                                    lang='deu', config=myconfig)
    for j in range(len(data['text'])):
        if float(data['conf'][j]) > 40:
            print(data['text'][j], end=' ')
    print()
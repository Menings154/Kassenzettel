import cv2
import glob
import numpy as np
import pytesseract

files = glob.glob(r'C:\Users\Benja\Code\Python\Kassenzettel\test\*.jpg')
img = cv2.imread(files[0])

# cv2.imshow('beginning', img)
# cv2.waitKey(0)

img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

# cv2.imshow('1. step', img)
# cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('2. step', img)
# cv2.waitKey(0)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

# cv2.imshow('3. step', img)
# cv2.waitKey(0)

img = cv2.erode(img, kernel, iterations=1)

# cv2.imshow('4. step', img)
# cv2.waitKey(0)

cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.imshow('5. step', img)
# cv2.waitKey(0)

text = pytesseract.image_to_string(img, lang="deu", )
print(text)
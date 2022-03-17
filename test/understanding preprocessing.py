import cv2 as cv
import numpy as np
from PIL import Image
from helper import showimg

# img = cv.imread(r'C:\Users\Benja\Code\Python\Kassenzettel\test\page0.jpg')
# showimg(img, 'start')

# #image scaling
# im = Image.open(r"C:\Users\Benja\Code\Python\Kassenzettel\test\page0.jpg")
# im.save(r"C:\Users\Benja\Code\Python\Kassenzettel\test\page0_300.jpg", dpi=(300,300))

img = cv.imread(r'C:\Users\Benja\Code\Python\Kassenzettel\test\page_new0.jpg')
showimg(img, 'start')
#image increase contrast/brightness
# alpha = 1.5 # Contrast control (1.0-3.0)
# beta = 0 # Brightness control (0-100)
# adjusted = cv.convertScaleAbs(img, alpha=alpha, beta=beta)

# showimg(adjusted, 'adjusted')

# #binarising the image
# im_gray = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
# (thresh, im_bw) = cv.threshold(img, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# im_bw = cv.threshold(im_gray, thresh, 255, cv.THRESH_BINARY)[1]

#image noise removal
# im_nr = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
# showimg(im_nr, 'noise')
# im_nr = cv.fastNlMeansDenoising(img, None, 10, 7, 15)
# showimg(im_nr, 'noise')

# im_nr = cv.fastNlMeansDenoising(img, None, 50, 7, 15)
# showimg(im_nr, 'noise')
#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(image, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
    return rotated
img_ds=deskew(img)
showimg(img_ds, 'deskrew')
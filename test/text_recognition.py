from xml.dom import HierarchyRequestErr
import cv2
import pytesseract
import re

# Mention the installed location of Tesse"ract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def img_to_text(img_path: str) -> list:
    # Read image from which text needs to be extracted
    img = cv2.imread(img_path)

    # Preprocessing the image starts
    
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    cv2.imshow('thrsh',thresh1)
    cv2.waitKey(0)
    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    cv2.imshow('kernel',rect_kernel)
    cv2.waitKey(0)
    # Applying dilation on the threshold image
    dilation = thresh1#cv2.dilate(thresh1, rect_kernel, iterations = 1)

    cv2.imshow('dilation_before', dilation)
    cv2.waitKey(0)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)


    cv2.imshow('dilation', dilation)
    cv2.waitKey(0)   
    
    # Creating a copy of image
    im2 = img.copy()
    
    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    list_of_words = []
    for cnt in contours:
   
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('contl', rect)
        cv2.waitKey(0)           
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
    
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        
        # Appending the text into file
        list_of_words.append(text)

    return list_of_words

def extract_words(text: str) -> str:
    word_only = re.compile(r"\w*[*a-zA-Z- ]\w*")
    return word_only.findall(text)


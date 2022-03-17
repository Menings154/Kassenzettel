import cv2

def showimg(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
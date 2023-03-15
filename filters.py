import numpy as np
import cv2 as cv
#from tensorflow.keras.preprocessing.image import img_to_array


# greyscale
def grayscale(img, lbl):
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imshow('Grayscale', gray_image)
    # cv.waitKey(0)
    cv.imwrite('results/grayscaled.jpg', gray_image)
    lbl.configure(width=75, height=20, text="Hasil Tersimpan", image='')

# B&W


def bnw(img, lbl):
    (thresh, binary) = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    #cv.imshow("Black N White", binary)
    # cv.waitKey(0)
    cv.imwrite('results/blacknwhite.jpg', binary)
    lbl.configure(width=75, height=20, text="Hasil Tersimpan", image='')

# Gaussian Blur


def gaussian_blur(img, lbl):
    gaussImage = cv.GaussianBlur(img, (21, 21), 0)
    #cv.imshow("Gaussian Blur", gaussImage)
    # cv.waitKey(0)
    cv.imwrite('results/blurred.jpg', gaussImage)
    lbl.configure(width=75, height=20, text="Hasil Tersimpan", image='')
    # gaussImage.save('images/gaussian_blur.jpg')

# Dilation


def Dilation_Opencv(img, lbl):
    kernel = np.ones((7, 7), np.uint8)
    dilate = cv.dilate(img, kernel, iterations=1)
    #cv.imshow("Dilation Output Image", dilate)
    # cv.waitKey(0)
    cv.imwrite('results/dilated.jpg', dilate)
    lbl.configure(width=75, height=20, text="Hasil Tersimpan", image='')
    # cv.destroyAllWindows()

# Erosion


def Erosion_Opencv(img, lbl):
    kernel = np.ones((7, 7), np.uint8)
    erosion = cv.erode(img, kernel, iterations=1)
    #cv.imshow("Erosion Output Image", erosion)
    # cv.waitKey(0)
    cv.imwrite('results/eroted.jpg', erosion)
    lbl.configure(width=75, height=20, text="Hasil Tersimpan", image='')

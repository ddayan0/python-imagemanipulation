import cv2 as cv
def togrey(img, newimgname):
    userimg = cv.imread(img, 0)
    cv.imwrite(newimgname, userimg)





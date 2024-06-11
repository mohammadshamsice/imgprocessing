import cv2
import glob
for img in glob.glob("img/to/folder/*.png"):
    cv_img = cv2.imread(img)
    cv2.imshow(cv_img)
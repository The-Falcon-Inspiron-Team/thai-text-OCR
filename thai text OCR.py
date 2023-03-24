import cv2
import pytesseract
 
image = cv2.imread("image.jpg")
 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
text = pytesseract.image_to_string(gray, lang='tha')
 
print("\n" + text)
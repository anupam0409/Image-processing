#Resulting text from Normal Image
'''from PIL import Image
import pytesseract,sys
im = Image.open(sys.argv[1]+".png")
text = pytesseract.image_to_string(im, lang = 'eng',config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
if text:
    print(text)
else:
    print("cant detect image")'''

#Resulting text from Scanned car Number plate image
import cv2, sys
import pytesseract

img = cv2.imread(sys.argv[1] + '.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
contours, h = cv2.findContours(thresh, 1, 2)

largest_rectangle = [0, 0]
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    if len(approx) == 4: 
        area = cv2.contourArea(cnt)
        if area > largest_rectangle[0]:
            largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

x, y, w, h = cv2.boundingRect(largest_rectangle[1])
roi = img[y:y + h, x:x + w]
text = pytesseract.image_to_string(roi)
if text:
    print(text)
else:
    print("cant detect image")
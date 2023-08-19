import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('1.jpg')
img = cv2.resize(img, (1300, 1100))
hImg, wImg, _ = img.shape

boxes = pytesseract.image_to_boxes(img)

html_content = "<html><head></head><body style='position: relative;'>"

for b in boxes.splitlines():
    b = b.split(' ')
    word = b[0]
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    html_content += f"<div style='position: absolute; left: {x}px; top: {hImg - y}px;'>{word}</div>"

html_content += "</body></html>"

with open("output.html", "w") as f:
    f.write(html_content)
import cv2
import pytesseract


if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    img = cv2.imread('266.jpg')

    text = pytesseract.image_to_string(img)

    print(text)

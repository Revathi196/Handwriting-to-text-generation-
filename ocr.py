import pytesseract
import cv2
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

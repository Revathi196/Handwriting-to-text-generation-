import cv2
import pytesseract
from image_processing import preprocess_image
from ocr import extract_text

def main():
    image_path = "handwritten_sample.jpg"  # Change to your image file
    processed_image = preprocess_image(image_path)
    text = extract_text(processed_image)
    print("Extracted Text:")
    print(text)

if __name__ == "__main__":
    main()

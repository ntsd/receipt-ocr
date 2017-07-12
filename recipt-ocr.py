import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def preprocess(url):
    im = Image.open(url)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('temp.jpg')

if __name__ == '__main__':
    images = ['sample1.jpg', 'sample2.jpg']
    preprocess(images[0])
    im = Image.open("temp.jpg")
    text = pytesseract.image_to_string(im, config='-psm 10')
    print(text)

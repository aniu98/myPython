import pytesseract
from PIL import Image
# img = Image.open('./testImages/test01.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# s = pytesseract.image_to_string(img, lang='chi_sim')  #不加lang参数的话，默认进行英文识别
print("111")

import numpy as np
import pytesseract
from PIL import Image
import cv2

# 이미지를 불러옵니다.
image_path = 'C:/project_django/사업.jpeg'
image = Image.open(image_path)

# 이미지 전처리를 위해 OpenCV를 사용하여 이미지를 그레이스케일로 변환합니다.
image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

# 이미지를 향상시키기 위해 적절한 전처리를 수행합니다.
# 예를 들어, 이미지를 블러 처리하거나 가우시안 블러를 적용할 수 있습니다.
# image_cv = cv2.blur(image_cv, (3, 3))

# 전처리된 이미지를 PIL Image 객체로 변환합니다.
image_preprocessed = Image.fromarray(image_cv)

# Tesseract OCR을 사용하여 이미지에서 텍스트를 추출합니다.
extracted_text = pytesseract.image_to_string(image_preprocessed, lang='kor')

# 추출된 텍스트를 출력합니다.
print(extracted_text)

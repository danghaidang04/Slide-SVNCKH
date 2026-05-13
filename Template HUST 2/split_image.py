from PIL import Image
import os

img_path = '/Users/danghaidang04/CodeSpace/LamSlide/Template HUST 2/image/abstractive.png'
if os.path.exists(img_path):
    img = Image.open(img_path)
    w, h = img.size
    left_img = img.crop((0, 0, w//2, h))
    right_img = img.crop((w//2, 0, w, h))
    
    left_img.save('/Users/danghaidang04/CodeSpace/LamSlide/Template HUST 2/image/extractive_method.png')
    right_img.save('/Users/danghaidang04/CodeSpace/LamSlide/Template HUST 2/image/abstractive_method.png')
    print("Split abstractive.png successfully.")
else:
    print("Image not found.")

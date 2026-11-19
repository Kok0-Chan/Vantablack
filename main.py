import os
import random
from PIL import Image, ImageDraw, ImageFont

folder = "images"
files = [
    os.path.join(folder, name)
    for name in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, name))
]

if files:
    random_file = random.choice(files)
    print("Выбран файл:", random_file)

    with open('mem_texts.txt', 'r', encoding='utf-8') as file:
        text = file.read().splitlines()

    img = Image.open(random_file)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Impact.ttf", size=50)
    draw.text((20, 50), random.choice(text), font=font, fill="white", stroke_width=4, stroke_fill="black")
    img.save("save_images/memosik.jpg")
    img.show()





else:
    print("В папке нет файлов.")

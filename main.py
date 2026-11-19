import os
import random
from PIL import Image, ImageDraw, ImageFont

folder = "images"
save_folder = "save_images"

# Создаем папку для сохранения, если её еще нет
os.makedirs(save_folder, exist_ok=True)

files = [
    os.path.join(folder, name)
    for name in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, name))
]

if files:
    random_file = random.choice(files)
    print("your file:", random_file)

    with open('mem_texts.txt', 'r', encoding='utf-8') as file:
        # Берем только непустые строки
        texts = [line.strip() for line in file if line.strip()]

    if texts:
        chosen_text = random.choice(texts)
        
        img = Image.open(random_file).convert("RGB")  # convert("RGB") защитит от ошибки при сохранении PNG в JPG
        draw = ImageDraw.Draw(img)
        width, height = img.size
        center_x = width // 2

        # Подбираем размер шрифта, чтобы текст заполнял ~90% ширины картинки
        target_width = width * 0.9
        font_size = 10
        font = ImageFont.truetype("Impact.ttf", size=font_size)

        while font.getlength(chosen_text) < target_width and font_size < height // 5:
            font_size += 2
            font = ImageFont.truetype("Impact.ttf", size=font_size)

        # Отступ сверху (5% от высоты картинки) и толщина обводки пропорционально шрифту
        top_margin = int(height * 0.05)
        stroke = max(2, font_size // 12)

        # anchor="mt" ставит центр верхней границы текста ровно в точку (center_x, top_margin)
        draw.text(
            (center_x, top_margin),
            chosen_text,
            font=font,
            fill="white",
            stroke_width=stroke,
            stroke_fill="black",
            anchor="mt"
        )

        output_path = os.path.join(save_folder, "memosik.jpg")
        img.save(output_path)
        img.show()
    else:
        print("Файл mem_texts.txt пуст")
else:
    print("Папка images пуста")

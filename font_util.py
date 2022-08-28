from PIL import ImageFont, ImageDraw, Image
import os

width, height = 60, 60

unicodes = [0x3000,
            0x303f,
            0x3041,
            0x309f,
            0x30a0,
            0x30ff,
            0xff00,
            0xffef,
            0x4e00,
            0x9faf]

total_unicodes = 0
for i in range(len(unicodes), 0, -2):
    total_unicodes += unicodes[i - 1] - unicodes[i - 2]

def generate_image(character, font_path, image_path):
    background_color = 'black'
    text_color = (255)
    color_mode = 'L'
    font_size=55

    font = ImageFont.truetype(font=font_path, size=font_size)
    image = Image.new(mode=color_mode, size=(width, height), color=background_color)
    image_draw = ImageDraw.Draw(image)

    bbox = image_draw.textbbox((0, 0), text=chr(character), font=font)
    xy = ((width - (bbox[2] + bbox[0])) / 2, (height - (bbox[3] + bbox[1])) / 2)

    image_draw.text(xy=xy, text=chr(character), fill=text_color, font=font)

    for i in range(width):
        for j in range(height):
            if image.getpixel((i, j)) != 0:
                if not os.path.exists(image_path):
                    os.mkdir(os.path.dirname(image_path))
                image.save(image_path)
                return True
    
    return False


def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False
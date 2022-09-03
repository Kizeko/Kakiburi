from PIL import ImageFont, ImageDraw, Image
from fontTools.ttLib import TTFont

# Defining image properties
background_color = 'black'
text_color = (255)
color_mode = 'L'
font_size=55
width, height = 60, 60
MIN_NUMBER_OF_IMAGES_PER_UNICODE = 20

# Ranges of unicode to create
# Respectively the first and last unicode of each range
# Punctuation, Hiragana, Katakana, Symbols and Kanji.
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

# Getting the total number of characters to generate (for the progress bar)
total_unicodes = 0
for i in range(len(unicodes), 0, -2):
    total_unicodes += unicodes[i - 1] - unicodes[i - 2]

# Font support function
def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False

# Generating the image
def generate_image(character, font_path, img_dir_path, img_path):
    # Checking if the font supports this unicode
    font = TTFont(font_path)
    if not char_in_font(chr(character), font):
        return (False, None)

    # Generating the image
    font = ImageFont.truetype(font=font_path, size=font_size)
    image = Image.new(mode=color_mode, size=(width, height), color=background_color)
    image_draw = ImageDraw.Draw(image)

    bbox = image_draw.textbbox((0, 0), text=chr(character), font=font)
    xy = ((width - (bbox[2] + bbox[0])) / 2, (height - (bbox[3] + bbox[1])) / 2)

    image_draw.text(xy=xy, text=chr(character), fill=text_color, font=font)

    # Checking again if the font supports this unicode
    if not image.getbbox():
        return (False, None)

    return (True, image)

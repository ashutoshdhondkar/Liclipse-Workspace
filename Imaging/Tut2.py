from PIL import Image

img = Image.open('1234.png')

img.convert("RGB").show()

del img
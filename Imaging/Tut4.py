from PIL import Image,ImageFilter

img = Image.open('brett.png')
img.filter(ImageFilter.SHARPEN).show()

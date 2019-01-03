from PIL import Image

img = Image.open('brett.png')
img.crop((10,10,300,300)).show()

# (top left,right bottom) same as rectangle(x1,y1,x2,y2) in C
del img
from PIL import Image , ImageDraw , ImageFont

img = Image.open('boo.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf' , 30)
text = 'abcdefghijklmnop'
draw.text((553,660) , text , (0,0,0) , font = font)
draw.text((553,710) , text , (0,0,0) , font = font)
img.show()
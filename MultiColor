import os
from PIL import Image, ImageFont, ImageDraw
import appex

#将像素转换为ascii码
def get_char(r,g,b,alpha = 256):
	ascii_char = list("MNHQ$OC?7o>!:-;. ")
	if alpha == 0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	unit = (256.0+1)/length
	return ascii_char[int(gray/unit)]

def main():
	w = 3
	h = 6
	if not appex.is_running_extension():
		print('Running in Pythonista app, using test image...')
		im = Image.open('test:Pythonista')
	else:
		im = appex.get_image()
	WIDTH = int(im.width/int(w))
	HEIGHT = int(im.height/int(h))
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
	
	txt = ""
	colors = []
	for i in range(HEIGHT):
		for j in range(WIDTH):
			pixel = im.getpixel((j,i))
			colors.append((pixel[0],pixel[1],pixel[2]))#记录像素颜色信息
			if(len(pixel) == 4):
				txt += get_char(pixel[0],pixel[1],pixel[2],pixel[3])
			else:
				txt += get_char(pixel[0],pixel[1],pixel[2])
		txt += '\n'
		colors.append((255,255,255))
	x=y=0
	#ImageDraw为每个ascii码进行上色
	img = Image.new("RGB", (im.width*3, im.height*5), (255, 255, 255))
	dr = ImageDraw.Draw(img)
	#ImageDraw为每个ascii码进行上色
	for i in range(len(txt)):
		if(txt[i]=='\n'):
			x+=5
			y=-10
		dr.text([y,x],txt[i],colors[i])
		y+=3
	img.show()
	
if __name__=='__main__':
	main()

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
	if not appex.is_running_extension():
		print('Running in Pythonista app, using test image...')
		im = Image.open('test:Pythonista')
	else:
		im = appex.get_image()
	WIDTH = int(im.width/6) #高度比例为原图的1/6较好，由于字体宽度
	HEIGHT = int(im.height/15)  #高度比例为原图的1/15较好，由于字体高度
	im_txt = Image.new("RGB",(im.width,im.height),(255,255,255))
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
	dr = ImageDraw.Draw(im_txt)
	font=ImageFont.load_default().font#获取字体
	x=y=0
	#获取字体的宽高
	font_w,font_h=font.getsize(txt[1])
	font_h *= 1.37 #调整后更佳
	#ImageDraw为每个ascii码进行上色
	for i in range(len(txt)):
		if(txt[i]=='\n'):
			x+=font_h
			y=-font_w
		dr.text([y,x],txt[i],colors[i])
		y+=font_w
	#输出
	im_txt.show()

if __name__=='__main__':
	main()

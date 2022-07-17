# _*_ coding:utf-8 _*_
from PIL import Image
import appex
import dialogs
import photos
import Image, ImageDraw

#将像素转换为ascii码
def get_char(r,g,b,alpha = 256):
	#灰度表
	ascii_char = list("MNHQ$OC?7o>!:-;. ")
	if alpha == 0:
		return ' '
	length = len(ascii_char)
	#装换为灰度
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	unit = (256.0+1)/length
	#将像素颜色映射为对应的ascii码
	return ascii_char[int(gray/unit)]
	
def main():
	w = 5
	h = 10
	#检测是否在pythonista中运行
	if not appex.is_running_extension():
		print('Running in Pythonista app, using test image...')
		img = Image.open('test:Pythonista')
	else:
		img = appex.get_image()
	#开始图像处理
	if img:
		#重构图像大小
		WIDTH = int(img.width/int(w))
		HEIGHT = int(img.height/int(h))
		img = img.resize((WIDTH,HEIGHT),Image.NEAREST)
		#将图片的每一个像素根据灰度表转换为字符
		txt = ""
		for i in range(HEIGHT):
			for j in range(WIDTH):
				pixel = img.getpixel((j,i))
				if(len(pixel) == 4):
					txt += get_char(pixel[0],pixel[1],pixel[2],pixel[3])
				else:
					txt += get_char(pixel[0],pixel[1],pixel[2])
			txt += '\n'
		#将字符文件转图片
		im = Image.new("RGB", (img.width*7, img.height*12), (255, 255, 255))
		dr = ImageDraw.Draw(im)
		dr.text((10, 5), txt, fill="#000000")
		im.show()
	else:
		pass
		
if __name__=='__main__':
	main()

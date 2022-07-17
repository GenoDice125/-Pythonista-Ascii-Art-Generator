import ui
import dialogs
import BlackWhite
import Color
import MultiColor
import clipboard
import appex

def main():
	s = dialogs.alert('Image Convert', 'Choose a style you want','Char','Color Char','Super Color Char')
	if s == 1:
		BlackWhite.main()
	elif s == 2:
		Color.main()
	elif s == 3:
		MultiColor.main()
	else:
		pass
	i = dialogs.alert('Finished', 'You can tap and hold the image to save it to your photo library.','Okay')
	if i == 1:
		pass
	else:
		pass
			
if __name__=='__main__':
	main()

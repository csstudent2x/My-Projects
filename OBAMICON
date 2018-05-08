
#GWC PROJECT

dark_blue=(0,51,76)
red=(217,26,33)
light_blue=(112,150,158)
yellow=(252,227,166)

im=Image.open("PACMAN.jpg")
width=im.size[0]
height=im.size[1]

data = im.getdata()

data_list=list(data)


def colorize (image_data):
	new_pic = []
	for pixel in data_list:
		if pixel[0]+pixel[1]+pixel[2] < 182:
			new_pic.append(dark_blue)
		elif pixel[0]+pixel[1]+pixel[2] < 364:
			new_pic.append(red)

		elif pixel[0]+pixel[1]+pixel[2] > 546:
			new_pic.append(yellow)
		else:
			new_pic.append(light_blue)
	return new_pic 
data_colorized = colorize(data_list)
new_image = Image.new(im.mode,im.size)
new_image.putdata(data_colorized)
new_image.show()
new_image.save("output", "jpeg")
		

	
	


from PIL import Image
im = Image.open("campbellriver.jpg")
im.rotate(45).show()
new_image = Image.new(im.mode, im.size)
new_image.save("output.jpg", "jpeg")
#---------------------------------------------------------------------------------------------------------------------
darkBlue = (0,51,76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

list_of_pixels = list(im.getdata())
#print(list_of_pixels[3])
pixel_list = []

for pixel in list_of_pixels:
	R = pixel [0]
	G = pixel [1]
	B = pixel [2]
	intensity = R + G + B
	if intensity <= 182:
		pixel_list.append(darkBlue)
	elif 182 < intensity <= 364:
		pixel_list.append(red)
	elif 364 < intensity <= 546:
		pixel_list.append(lightBlue)
	else:
		pixel_list.append(yellow)



new_image.putdata(pixel_list)
new_image.show()



#if 182<intensity or intensity<364:


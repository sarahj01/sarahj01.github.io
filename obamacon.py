from PIL import Image
im = Image.open("campbellriver.jpg")
im.rotate(45).show()
new_image = Image.new(im.mode, im.size)
new_image.save("output.jpg", "jpeg")



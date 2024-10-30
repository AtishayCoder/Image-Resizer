from PIL import Image

image = input("Enter the full path to the image: \n")

with Image.open(image) as i:
    new_i = i.resize((int(input("Enter required width of image: \n")), int(input("Enter required height of image:\n"))))
    new_i.save(image)

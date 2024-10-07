from PIL import Image

# Load the PNG image
img = Image.open('info_extraction.webp')


# Save the image in JPG format
img.save('info_extraction.jpg')

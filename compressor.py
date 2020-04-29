# import PIL module
import PIL
# importing image from PIL module
from PIL import Image

# opening image from the current working directory
img = Image.open("margot.jpg")

# resizing the image to specific dimensions
img = img.resize((500, 500), PIL.Image.ANTIALIAS)

# saving the resize image to the directory
img.save("margot2.jpg")

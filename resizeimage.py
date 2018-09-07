
from PIL import Image
import os

image_file = "00000001.jpg"
basewidth = 800

#convert to the basewidth
img = Image.open(image_file).convert("RGB")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)

# split image filename into name and extension
name, ext = os.path.splitext(image_file)

# create a new file name for saving the result
new_image_file = "%s%s%s" % (name, '.'+str(basewidth), ext)
img.save(new_image_file)
print("resized file saved as %s" % new_image_file)

# one way to show the image is to activate
# the default viewer associated with the image type
import webbrowser
webbrowser.open(new_image_file)


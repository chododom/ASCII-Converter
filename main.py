from pip._vendor.distlib.compat import raw_input
from image import *

while True:
    try:
        path = raw_input("Which image would you like to convert to ASCII art? (type path to image)\n")
    except EOFError:
        break

    img = JPG(path)
    img.convert_to_ascii()

    print(img)

#!/usr/bin/env python

import os
from Pillow import Image test

# Owned
__author__ = "fstoaldo"
__maintainer__ = "fstoaldo"
__email__ = "fstoaldo@gmail.com"

"""images.py: the initial goal of this program is to open an image file and retrieve the top5 most frequent colours 
of it. """


def main():
    im = Image.open('dead_parrot.jpg')  # Can be many different formats.
    pix = im.load()
    print
    im.size  # Get the width and hight of the image for iterating over
    print
    pix[x, y]  # Get the RGBA Value of the a pixel of an image
    pix[x, y] = value  # Set the RGBA Value of the image (tuple)
    im.save('alive_parrot.png')  # Save the modified pixels as .png


if __name__ == '__main__':
    main()


"""
Usage:
    python gify.py image1 image2 image3
"""

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    images.append(Image.open(arg))

images[0].save(
    "out.gif",
    save_all=True,
    append_images=images[1:],
    duration=150,
    loop=0,
)

print("Done")

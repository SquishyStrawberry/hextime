from wand.color import Color
from wand.image import Image
import time

current_time = time.strftime("%H%M%S")
current_hex = "#" + current_time
with Color(current_hex) as color:
	with Image(width=200, height=200, background=color) as image:
		image.save(filename="current_time.jpg")

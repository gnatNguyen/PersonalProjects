import cv2 as cv
import time
import numpy as np
import random
from os import system

PIXEL_RANGE_DICTIONARY = {"range1":"B", "range2":"S", "range3":"F", "range4":"H", 
							"range5":"0", "range6":"8", "range7":"A", "range8":"&", 
							"range9":"%", "range10":"#", "range11":"!", "range12":"*", 
							"range13":"^", "range14":":", "range15":"."}


def main():
	
	cap = cv.VideoCapture(0, cv.CAP_DSHOW)

	width = 120
	height = 90

	# width = 80
	# height = 60
	dimension = (width, height)

	# last_time = time.time()

	blank_image = np.zeros(shape=[200, 200, 3], dtype=np.uint8)

	blank_frame = cv.putText(blank_image, 'PRESS Q TO QUIT', (30, 100), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

	cv.imshow('WINDOW', blank_frame)

	while True:
		ret, frame = cap.read()

		resized_frame = cv.resize(cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2GRAY), dimension, interpolation=cv.INTER_AREA)

		system('cls')

		for lenPixel in range(22, height-15):
			for widthPixel in range(width):

				if resized_frame[lenPixel, widthPixel] <= 17:
					print(PIXEL_RANGE_DICTIONARY["range1"], end='')

				elif 17 < resized_frame[lenPixel, widthPixel] <= 34:
					print(PIXEL_RANGE_DICTIONARY["range2"], end='')

				elif 34 < resized_frame[lenPixel, widthPixel] <= 51:
					print(PIXEL_RANGE_DICTIONARY["range3"], end='')

				elif 51 < resized_frame[lenPixel, widthPixel] <= 68:
					print(PIXEL_RANGE_DICTIONARY["range4"], end='')

				elif 68 < resized_frame[lenPixel, widthPixel] <= 85:
					print(PIXEL_RANGE_DICTIONARY["range5"], end='')

				elif 85 < resized_frame[lenPixel, widthPixel] <= 102:
					print(PIXEL_RANGE_DICTIONARY["range6"], end='')

				elif 102 < resized_frame[lenPixel, widthPixel] <= 119:
					print(PIXEL_RANGE_DICTIONARY["range7"], end='')

				elif 119 < resized_frame[lenPixel, widthPixel] <= 136:
					print(PIXEL_RANGE_DICTIONARY["range8"], end='')

				elif 136 < resized_frame[lenPixel, widthPixel] <= 153:
					print(PIXEL_RANGE_DICTIONARY["range9"], end='')

				elif 153 < resized_frame[lenPixel, widthPixel] <= 170:
					print(PIXEL_RANGE_DICTIONARY["range10"], end='')

				elif 170 < resized_frame[lenPixel, widthPixel] <= 187:
					print(PIXEL_RANGE_DICTIONARY["range11"], end='')

				elif 187 < resized_frame[lenPixel, widthPixel] <= 204:
					print(PIXEL_RANGE_DICTIONARY["range12"], end='')

				elif 204 < resized_frame[lenPixel, widthPixel] <= 221:
					print(PIXEL_RANGE_DICTIONARY["range13"], end='')

				elif 221 < resized_frame[lenPixel, widthPixel] <= 238:
					print(PIXEL_RANGE_DICTIONARY["range14"], end='')

				else:
					print(PIXEL_RANGE_DICTIONARY["range15"], end='')

			print()

		if cv.waitKey(1) & 0xFF == ord('q'):
			break

		# try:
		# 	frames_per_second = f'{round(1/(time.time() - last_time), 1)} fps'

		# 	print(frames_per_second)
		# except:
		# 	passh

		# last_time = time.time()

	cap.release()
	cv.destroyAllWindows()

main()


# SLOWER WAY

# if resized_frame[lenPixel, widthPixel] <= 17:
# 	print(PIXEL_RANGE_DICTIONARY["range1"], end='')

# elif resized_frame[lenPixel, widthPixel] > 17 and resized_frame[lenPixel, widthPixel] <= 34:
# 	print(PIXEL_RANGE_DICTIONARY["range2"], end='')

# elif resized_frame[lenPixel, widthPixel] > 34 and resized_frame[lenPixel, widthPixel] <= 51:
# 	print(PIXEL_RANGE_DICTIONARY["range3"], end='')

# elif resized_frame[lenPixel, widthPixel] > 51 and resized_frame[lenPixel, widthPixel] <= 68:
# 	print(PIXEL_RANGE_DICTIONARY["range4"], end='')

# elif resized_frame[lenPixel, widthPixel] > 68 and resized_frame[lenPixel, widthPixel] <= 85:
# 	print(PIXEL_RANGE_DICTIONARY["range5"], end='')

# elif resized_frame[lenPixel, widthPixel] > 85 and resized_frame[lenPixel, widthPixel] <= 102:
# 	print(PIXEL_RANGE_DICTIONARY["range6"], end='')

# elif resized_frame[lenPixel, widthPixel] > 102 and resized_frame[lenPixel, widthPixel] <= 119:
# 	print(PIXEL_RANGE_DICTIONARY["range7"], end='')

# elif resized_frame[lenPixel, widthPixel] > 119 and resized_frame[lenPixel, widthPixel] <= 136:
# 	print(PIXEL_RANGE_DICTIONARY["range8"], end='')

# elif resized_frame[lenPixel, widthPixel] > 136 and resized_frame[lenPixel, widthPixel] <= 153:
# 	print(PIXEL_RANGE_DICTIONARY["range9"], end='')

# elif resized_frame[lenPixel, widthPixel] > 153 and resized_frame[lenPixel, widthPixel] <= 170:
# 	print(PIXEL_RANGE_DICTIONARY["range10"], end='')

# elif resized_frame[lenPixel, widthPixel] > 170 and resized_frame[lenPixel, widthPixel] <= 187:
# 	print(PIXEL_RANGE_DICTIONARY["range11"], end='')

# elif resized_frame[lenPixel, widthPixel] > 187 and resized_frame[lenPixel, widthPixel] <= 204:
# 	print(PIXEL_RANGE_DICTIONARY["range12"], end='')

# elif resized_frame[lenPixel, widthPixel] > 204 and resized_frame[lenPixel, widthPixel] <= 221:
# 	print(PIXEL_RANGE_DICTIONARY["range13"], end='')

# elif resized_frame[lenPixel, widthPixel] > 221 and resized_frame[lenPixel, widthPixel] <= 238:
# 	print(PIXEL_RANGE_DICTIONARY["range14"], end='')

# else:
# 	print(PIXEL_RANGE_DICTIONARY["range15"], end='')
import time
from matplotlib import pyplot as plt

# USE DATA SCRAPED, CLEANS AND GRAPHS IT

def main():
	videoAxis, viewsAxis, channel_name = clean_data()

	graph_data(videoAxis, viewsAxis, channel_name)


def clean_data():
	data_file = open("data.txt").read()

	data_list = data_file.split("\n")

	data_list.pop(-1)
	channel_name = data_list[0]

	for n, x in enumerate(data_list):
		if x == "CC":
			data_list.pop(n)

	views = []
	viewsAxis = []

	number_abrev = {"K":"000", "M":"00000"}

	for x in data_list:
		
		if " views" in x:
			views.append(x)

	for x in views:
		cleanUp_view = x.split(' ')
		for x in cleanUp_view:
			if x == "views":
				cleanUp_view.remove(x)

		stripped_views = ''.join(cleanUp_view)

		word_list = list(stripped_views)
		
		for x in word_list:
			if x == " ":
				word_list.remove(x)

			if x == "K" and "." not in word_list:
				word_list.remove(x)

				word_list.append("000")

			elif x == "K" and "." in word_list:
				word_list.remove(x)

				word_list.append("00")

			elif x == "M" and "." in word_list:
				word_list.remove(x)
				word_list.append("00000")

			elif x == "M" and "." not in word_list:
				word_list.remove(x)
				word_list.append("000000")

		for x in word_list:
			if x == ".":
				word_list.remove(x)

		word_string = ''.join(word_list)
		string_to_integer = int(word_string)
		viewsAxis.append(string_to_integer)

	videoAxis = []

	for x in range(len(viewsAxis)):
		videoAxis.append(x)

	return videoAxis, viewsAxis, channel_name


def graph_data(videoAxis, viewsAxis, channel_name):
	plt.plot(videoAxis, viewsAxis, color='black')
	plt.ticklabel_format(style = 'plain')

	plt.xlabel('Videos')
	plt.ylabel('Views')
	plt.title(channel_name + " Views History")

	plt.grid(True)
	plt.show()


main()
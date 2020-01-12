import bs4 as bs
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from os import system
import sys

# SCRAPE VIEWS FROM CHANNEL

youtube_channel = input("Enter a channel name: ")

print("Setting up simulated browser and needed data...")
time.sleep(1)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')

browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.youtube.com/')
browser.maximize_window()
time.sleep(2)


def main():
	latest_video_title = setupBrowser()

	scrollToBottom(latest_video_title)

	writeData()

	print("Successfully finished scraping " + youtube_channel + "'s channel.")
	print()
	time.sleep(1)
	print("Data has been written to the \"data.txt\" file.")
	print()
	time.sleep(1)
	print("Run the dataCompiler program to display the graph.")
	time.sleep(1)
	print()
	input("Press enter to exit")


def setupBrowser():
	searchBar = browser.find_elements_by_id('search')

	searchBar[0].send_keys(youtube_channel)
	time.sleep(.2)
	searchBar[0].send_keys(Keys.ENTER)
	time.sleep(2)

	channel_main_page = browser.find_elements_by_class_name('style-scope ytd-channel-renderer')
	channel_main_page[0].click()

	time.sleep(3)

	videos_tab = browser.find_elements_by_class_name('style-scope paper-tab')
	videos_tab[1].click()

	time.sleep(3)

	video_titles = browser.find_elements_by_xpath('//*[@id="video-title"]')

	titles = []

	for n, x in enumerate(video_titles):
		if len(x.text) != 0:
			titles.append(x.text)

	latest_video_title = titles[0]

	drop_down = browser.find_elements_by_class_name('style-scope yt-dropdown-menu')
	time.sleep(2)
	drop_down[1].click()
	time.sleep(1)

	oldest_dropDown = browser.find_elements_by_xpath('//*[@id="menu"]/a[2]/paper-item/paper-item-body/div[1]')

	try:
		oldest_dropDown[1].click()
	except:
		oldest_dropDown[0].click()

	time.sleep(1)

	return latest_video_title


def scrollToBottom(latest_video_title):
	SCROLL_PAUSE_TIME = 1.5

	while True:
		scrollingAnimation()

		browser.find_element_by_tag_name('body').send_keys(Keys.END)
		time.sleep(SCROLL_PAUSE_TIME)

		latest_video = browser.find_elements_by_id('video-title')

		if latest_video[-1].text == latest_video_title:
			system("cls")
			print("Video has been found!")
			time.sleep(.5)
			break


def writeData():
	channel_name_list = browser.find_elements_by_class_name('style-scope ytd-channel-name')
	channel_name = channel_name_list[0].text

	videos = browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

	data_file = open("data.txt", "w")

	num_of_videos = len(videos)

	try:
		data_file.write(channel_name+"\n")

	except:
		data_file.write(youtube_channel+"\n")


	for pos, tags in enumerate(videos):
		dataWriteAnimation(pos, num_of_videos)

		try:
			data_file.write(tags.text+"\n")

		except:
			data_file.write("Title Error" + "\n")

	time.sleep(2)

	data_file.close()
	browser.close()
	browser.quit()


def dataWriteAnimation(pos, num_of_videos):
	system("cls")
	print("Writing data to file")
	print(str(pos+1) + " out of " + str(num_of_videos) + " items.")
	

def scrollingAnimation():
	system("cls")
	print("Scrolling until latest video found.")
	time.sleep(.08)
	system("cls")
	print("Scrolling until latest video found..")
	time.sleep(.08)
	system("cls")
	print("Scrolling until latest video found...")
	time.sleep(.08)


main()

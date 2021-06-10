import os
from pytube import YouTube
import sys

#TODO: get's the downloads folder path
def getdesktoppath ():
  return os.path.join (os.path.expanduser ("~"), "Downloads")

# print(getdesktoppath())

while True:
    video = input("Enter URL to download YouTube Videod and EXIT to quit:  ")

    if(video == 'exit' or video == 'EXIT'):
        sys.exit("Bye!")
    else:
        print("Fetching . . .\n")
        yt = YouTube(video)


        print( yt.title)
        print("Author : ", yt.author)
        print("Description : ", yt.description)
        print("thumbnail_url : ", yt.thumbnail_url)
        print("Views : ", yt.views)
        print("Date : ", yt.publish_date)

        print("\n\n")

        while True:
            qual = int(input("Enter 1 for high resolution and 0 for low resolution : "))

            # yt.streams.get_by_resolution(qual).download()
            if(qual == 1):
                print("Downloading in highest res . . .")
                yt.streams.get_highest_resolution().download(getdesktoppath())
                break
            elif(qual == 0):
                print("Downloading in lowest res . . .")
                yt.streams.get_lowest_resolution().download(getdesktoppath())
                break
            else:
                print("Please enter valid input")

        print("Done! video is in Downloads folder ")

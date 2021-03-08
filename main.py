from pytube import YouTube
import sys


while True:
    video = input("Enter URL to download YouTube Videod and EXIT to quit:  ")

    if(video == 'exit' or video == 'EXIT'):
        sys.exit("Bye!")
    else:
        yt = YouTube(video)

        print("Fetching...\n")

        print( yt.title)
        print("Author : ", yt.author)
        print("Description : ", yt.description)
        print("Length : ", yt.length)
        print("Rating : ", yt.rating)
        print("thumbnail_url : ", yt.thumbnail_url)
        print("Views : ", yt.views)
        print("Date : ", yt.publish_date)

        print("Printing available resolutions \nNOTE : (some of the resolution might not work so if it gives any try again with different res) ->")

        l = list(yt.streams)
        for i in (l):
            #print(str(i), end= "\n")
            res = str(i).find('res')
            for j in range(10) :
                st = str(i)
                print(st[res], end="")
                res = res + 1
            print("\n")

        qual = input("Enter video resolution : ")

        yt.streams.get_by_resolution(qual).download()

        print("Done! video is inside the current dir ")

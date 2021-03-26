from pytube import YouTube
import sys


while True:
    video = input("Enter URL to download YouTube Videod and EXIT to quit:  ")
    print("Fetching . . .\n")

    if(video == 'exit' or video == 'EXIT'):
        sys.exit("Bye!")
    else:
        yt = YouTube(video)


        print( yt.title)
        print("Author : ", yt.author)
        print("Description : ", yt.description)
        print("Length : ", yt.length)
        print("Rating : ", yt.rating)
        print("thumbnail_url : ", yt.thumbnail_url)
        print("Views : ", yt.views)
        print("Date : ", yt.publish_date)



        # l = list(yt.streams)
        # for i in (l):
        #     #print(str(i), end= "\n")
        #     res = str(i).find('res')
        #     for j in range(10):
        #         st = str(i)
        #         print(st[res], end="")
        #         res = res + 1
        #     print("\n")

        while True:
            qual = int(input("Enter 1 for high resolution and 0 for low resolution : "))

            # yt.streams.get_by_resolution(qual).download()
            if(qual == 1):
                print("Downloading in highest res . . .")
                yt.streams.get_highest_resolution().download()
                break;
            elif(qual == 0):
                print("Downloading in lowest res . . .")
                yt.streams.get_lowest_resolution().download()
                break
            else:
                print("Please enter valid input")

        print("Done! video is inside the current dir ")

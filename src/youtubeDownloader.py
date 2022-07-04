#!/bin/python3
import pafy
# in pafy changed "backend_youtube_dl.py" line 54 to "self._dislikes = self._ydl_info.get('dislike_count',0)" since youtube dissabled the dislike count


def main():
    # user changable variables
    isVideo=False
    usePath=False

    videoPath="~/video"
    audioPath="~/audio"

    urls = ["",
            "",
            ""]

    # ------------------------


    i = 1
    fails=""
    completed=False
    maxTries=5
    tries=0
    title=""
    nonEmptyLength=0
    for string in urls:
        if len(string) > 0:
            nonEmptyLength+=1

    for url in urls:
        if url != "":
            while (not completed) and (tries<maxTries):
                try:
                    video = pafy.new(url)
                    title = video.title

                    if isVideo:
                        print(str(i) + "/" + str(nonEmptyLength) + "\t[video]\t" + video.title)
                        best = video.getbest(preftype="mp4")
                        if(usePath):
                            best.download(filepath=videoPath)
                        else:
                            best.download()
                    else:
                        print(str(i) + "/" + str(nonEmptyLength) + "\t[audio]\t" + video.title)
                        best = video.getbestaudio(preftype="m4a")
                        if(usePath):
                            best.download(filepath=audioPath)
                        else:
                            best.download()

                    completed=True
                except Exception as e:
                    print(e)
                    tries+=1
            if(tries>=maxTries):
                fails+=title+": "+url+"\n"

            completed=False
            tries=0
        i+=1


    print("DONE")
    print("fails: ")
    print(fails)

if __name__ == '__main__':
    main()

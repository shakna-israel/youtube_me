from __future__ import unicode_literals
import youtube_dl
import time
import os

def clear_screen():
    os.system(['clear','cls'][os.name == 'nt'])

def get_files():
    infinite_loop = True
    while infinite_loop:
        if int(time.strftime("%H")) > 0 and int(time.strftime("%H")) < 9:
            video_folder = os.path.expanduser("~/youtube_me/videos")
            video_title = video_folder + "/" + '%(title)s' + ".mp4"
            ydl_opts = {'nooverwrites':True,'outtmpl':video_title,'sleep-interval':'10'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                with open(os.path.expanduser("~/youtube_me/download.list"),'r') as filePointer:
                    for line in filePointer:
                        if int(time.strftime("%H")) > 0 and int(time.strftime("%H")) < 9:
                            if line.strip() != '':
                                ydl.download([line.strip("\n").strip("\r")])
        else:
            clear_screen()
            hours_til = 24 - int(time.strftime("%H"))
            mins_til = 60 - int(time.strftime("%M"))
            time_til = [hours_til,mins_til]
            print("Time till next download... " + str(time_til[0]) + ":" + str(time_til[1]))
            time.sleep(120)

if __name__ == '__main__':
    if os.path.isdir(os.path.expanduser("~/youtube_me")):
        path_exists = True
    else:
        os.mkdir(os.path.expanduser("~/youtube_me"))
    if os.path.isdir(os.path.expanduser("~/youtube_me/videos")):
        path_exists = True
    else:
        os.mkdir(os.path.expanduser("~/youtube_me/videos"))
    if os.path.isfile(os.path.expanduser("~/youtube_me/download.list")):
        file_exists = True
    else:
        with open(os.path.expanduser("~/youtube_me/download.list"),'w+') as filePointer:
            filePointer.write("\n")
    get_files()

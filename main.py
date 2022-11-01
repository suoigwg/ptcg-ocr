# This is a sample Python script.
import os.path
import sys

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import pytesseract
import re
from db import Connection
from timer import Timer
from pytube import YouTube

card_codes = set()
timer = Timer()
conn = Connection()


def download_video(url='https://www.youtube.com/watch?v=JIQb0PYGt4A&t=204s',
                   download_folder='/Users/yishengyang/Downloads/ptcg-video', is_debug=True
                   ):
    print("video url {}".format(url))
    timer.start_new_phase("DOWNLOAD")
    yt = YouTube(url)
    video_stream = yt.streams.filter(file_extension='mp4').filter(res="360p").first()
    title = yt.title.title()
    file_path = os.path.join(download_folder, title+'.mp4')
    if is_debug or os.path.isfile(file_path):
        return file_path
    print('Downloading video to {}'.format(file_path))
    video_stream.download(output_path=download_folder)
    return file_path


def decode(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)


def match(text):
    matches = re.findall("[A-Z0-9]{3}-[A-Z0-9]{4}-[A-Z0-9]{3}-[A-Z0-9]{3}", text)
    if len(matches) != 0:
        card_codes.add(matches[0])
        print(matches)


def process_video(path):
    timer.start_new_phase("PROCESS")
    cap = cv2.VideoCapture(path)
    counter = 0
    while True:
        ret, frame = cap.read()
        if ret:
            if counter % 60 == 0:
                match(decode(frame))
            counter = counter + 1
        # Break the loop
        else:
            break
    print(card_codes)


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=JIQb0PYGt4A&t=204s' if len(sys.argv) <= 2 else sys.argv[1]
    process_video(download_video(is_debug=False, url=url))
    timer.summary()
    # print(youtube.get_channel_videos())

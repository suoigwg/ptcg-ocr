from pytube import YouTube, Channel, Stream


def get_channel_videos(channel_url='https://www.youtube.com/c/PokePulch/videos'):
    channel = Channel(channel_url)
    video_streams = []
    print(channel.last_updated)
    for video in channel.video_urls:
        video_streams.append(video.streams.filter(file_extension='mp4').filter(res="360p").first())
    return video_streams


def download_video(video: Stream):
    return video.download()

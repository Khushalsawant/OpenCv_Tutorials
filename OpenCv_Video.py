# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "C:/Users/khushal/Pictures/Khushal_videos/"  # to_do

# link of the video to be downloaded
link = "https://youtu.be/c3avv1U31LU"

try:
    # object creation using YouTube which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# filters out all the files with "mp4" extension
mp4files = YouTube(link).filter('mp4')

YouTube(link).set_filename('Phir Mulaaqat song-Video')  # to set the name of the file

# get the video with the extension and resolution passed in the get() function
d_video = YouTube(link).get(mp4files[-1].extension, mp4files[-1].resolution)
try:
    # downloading the video
    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')
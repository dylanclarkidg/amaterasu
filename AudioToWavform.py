# FFMPEG Download
import os

import imageio
imageio.plugins.ffmpeg.download()
# MoviePy Audio Extractor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
# Audio Reader for Numpy Arrays
from scipy.io.wavfile import read
# MatPlotLib to try and plot the array
import matplotlib.pyplot as plt

# Subclip Creator
from moviepy.video.VideoClip import VideoClip as clip

path = os.path.join(os.getcwd(), 'files')
print(path)

ffmpeg_extract_audio(path + "/test.mp4", path + "/audio.wav")

rate, data = read(path + "/audio.wav")
print(data)
print(type(data))

#plt.imshow(data)
#plt.show()


def subclip_creator(clip, start, end):
    return clip.subclip(start, end)



# FFMPEG Download
import imageio
imageio.plugins.ffmpeg.download()

# MoviePy Audio Extractor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

# Audio Reader for Numpy Arrays
from scipy.io.wavfile import read

ffmpeg_extract_audio("C:/work/personaldev/python/amaterasu/files/test.mp4", "C:/work/personaldev/python/amaterasu/files/audio.wav")

rate, data = read("C:/work/personaldev/python/amaterasu/files/audio.wav")
print(data)


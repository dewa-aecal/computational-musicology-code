# -*- coding: utf-8 -*-
"""
@author: Dewa Ardiana
"""
import librosa
import numpy as np
import matplotlib.pyplot as plt

path='music/audio1.mp3'

data, sr=librosa.load(path, sr=None, duration=10)

#converting time domain signal into frequency domain representation using short-time Fourier Transform
d=librosa.stft(data)

#converting amplitude to decibels
sig=librosa.amplitude_to_db(np.abs(d), ref=np.max)

#Displaying the spectogram
librosa.display.specshow(sig, x_axis="time", y_axis="log")
plt.title(f"Segment Spectogram of {path}")
plt.colorbar(format="%+2.0f dB")
plt.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dewa ardiana
"""
import librosa
import matplotlib.pyplot as plt

#audio file path. change with your audio file path
path='music/audio1.mp3'

#create subplot
fig, ax=plt.subplots(nrows=2, sharex=True)

#load audio data with duration 10 seconds and mono
data,sr=librosa.load(path, sr=None, duration=10)
librosa.display.waveshow(data, sr=sr, ax=ax[0])
ax[0].set(title="mono")
ax[0].label_outer()

#load audio data with duration 10 seconds and stereo
data,sr=librosa.load(path, sr=None, mono=False, duration=10)
librosa.display.waveshow(data, sr=sr, ax=ax[1])
ax[1].set(title="Stereo")
ax[1].label_outer()

plt.show()

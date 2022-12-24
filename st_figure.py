# -*- coding: utf-8 -*-
"""
streamlit run st_figure.py

streamlit 输出绘图、图片、视频、音频
"""
import streamlit as st
from PIL import Image


#%% 图像、音视频

## caption (str or list of str) 图片说明。如果显示多个图像，标题应为 标题列表（每张图片一个）。
image = Image.open('data/f1.jpg')
st.image(image=image, caption=None, width=None, use_column_width=None, clamp=False, 
         channels="RGB", output_format="auto")


### data: io.open(). Raw audio data, filename, or a URL pointing to the file to load. Numpy arrays and raw data formats must include all necessary file headers to match specified file format.
audio_file = open('myaudio.ogg', 'rb')
st.audio(data = audio_file, format="audio/wav", start_time=0)
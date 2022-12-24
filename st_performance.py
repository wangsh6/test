# -*- coding: utf-8 -*-
"""
各种装饰器。 本质都是用于存储，以减小开销
"""

import streamlit as st 
from PIL import Image
import time

image1 = Image.open('data/f1.jpg')
image2 = Image.open('data/f2.jpg')
image3 = Image.open('data/f3.jpg')

image = Image.open('data/t.png')

#### 页面头部设置
st.set_page_config(
    page_title="装饰器内存",    #页面标题
    page_icon=image,        #icon  
    # layout="wide",                #页面布局
    # initial_sidebar_state="auto"  #侧边栏 
    
)


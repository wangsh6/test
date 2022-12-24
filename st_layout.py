# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:58:46 2022

@author: wangsh6
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
    page_title="页面布局",    #页面标题
    page_icon=image,        #icon  
    # layout="wide",                #页面布局
    # initial_sidebar_state="auto"  #侧边栏 
    
)

#%%  布局方式一： st.columns 可以横排布置 


st.write("**column布局**")

### gap = "small" 可选 "small", "medium", or "large"
### 设置每行有 3列
col1, col2, col3 = st.columns(3)

col1.write("图片1")
col1.image(image=image1,channels="RGB", output_format="auto")

col2.write("图片2")
col2.image(image=image2,channels="RGB", output_format="auto")

col3.write("图片3")
col3.image(image=image3,channels="RGB", output_format="auto")


st.markdown('<br>',unsafe_allow_html=True)  

#%%  布局方式二：st.tab 选项卡布局

tab1, tab2, tab3 = st.tabs(["选项一", "选项一", "选项一"])

tab1.write("图片1")
tab1.image(image=image1,channels="RGB", output_format="auto")

tab2.write("图片2")
tab2.image(image=image2,channels="RGB", output_format="auto")

tab3.write("图片3")
tab3.image(image=image3,channels="RGB", output_format="auto")

st.markdown('<br>',unsafe_allow_html=True)  

#%%  布局方式三： st.expander 可隐藏容器
#### with 与 expander.write(...) 效果相同
with st.expander("扩展选项", expanded=False):
    st.write("通过扩展选项，可以实现控件的隐藏")
    st.image(image=image1,channels="RGB", output_format="auto")

st.markdown('<br>',unsafe_allow_html=True)  

#%%  布局方式四: st.container（）。
#### 功能1： 可以允许无序插入。即 同一容器内的控件会置于相同位置。
### 功能2： 分部分。可以设置几个 container。不同的container之间会有分隔的标识

container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")

st.markdown('<br>',unsafe_allow_html=True)  

#%%  扩展： st.empty()  --- 用于替换输出。 如 1-2-3-4-5.。。 的变换


placeholder = st.empty()

for i in range(5): 
    placeholder.write( "第{}次循环".format(i) )
    time.sleep(1)

# Clear all those elements:
placeholder.empty()

st.markdown('<br>',unsafe_allow_html=True)  

#%% 

# import streamlit as st
# from streamlit.components.v1 import html

# st.button('button背景色？换一个吧')
# st.text_area('del', placeholder='Label多余？删了就好')
# st.radio('想放大label字号, 修改字体吗？', ['想', '很想'])

# # st.markdown('''<style>
# # /* radio label字号、字体 */
# # #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(3) > div > label {
# #      font-size: 50px;
# #      font-family: "Times New Roman", serif;
# # }

# #  #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(3) > div > label
            
# # /* button背景色 */ 
# # #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(1) > div > button {
# #     background-color: black;
# #     color: white;
# # }

# # /* radio选中项颜色 */
# # #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(3) > div > div > label:nth-child(1) > div.st-co.st-cs.st-ct.st-cu.st-cv.st-cw.st-az.st-b4.st-cx.st-cy.st-cz.st-d0.st-d1.st-d2.st-c4.st-d3.st-d4.st-d5.st-b2.st-bl {
# #      background-color: black;
# # }
# # </style>''', unsafe_allow_html=True)

# # js_delete = '''window.parent.document.querySelector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(2) > div > label").remove()'''
# # html(f'''<script>{js_delete}</script>''',
# #      width=0,
# #      height=0)

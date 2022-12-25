# -*- coding: utf-8 -*-
"""
通过前端改写，设置 颜色、字体、等细节

方法一： st.markdown撰写CSS来修改st组件的样式

方法二：from streamlit.compoents.v1 import html 编写 html代码
"""


import streamlit as st
from streamlit.components.v1 import html


st.write("第一行文本")
st.markdown('<br>',unsafe_allow_html=True) 

st.write("第二行文本") 
st.markdown('<br>',unsafe_allow_html=True) 

st.button('禁用', disabled=True)
st.markdown('<br>',unsafe_allow_html=True) 

st.button('按钮选项')
st.markdown('<br>',unsafe_allow_html=True) 


############# 步骤： 
# 首先， 使用 st.markdown 处理。同时 markdown 要在代码最后部分加入。
# 打开 检查，查找 CSS位置(即 seletor)。

## 添加 '''<style>   CSS内容  <style>'''   
### 对 {} 内容进行自定义修改
# font-size 字体
# font-family 字号 
# ackground-color 背景色 

st.markdown( '''<style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(1) > div > div > p
            {background-color: rgb(255 75 75 / 50%);
             font-size: 50px;
             font-family: "仿宋", serif;
             color:white}
            <style>''' , unsafe_allow_html=True)



# js_delete = '''window.parent.document.querySelector("
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > footer
#   ").remove()'''
# html(f'''<script>{js_delete}</script>''',
#       width=0,
#       height=0)
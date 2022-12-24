# -*- coding: utf-8 -*-
"""
通过前端改写，设置 颜色、字体、等细节
"""

import jieba
import streamlit as st

corpus=['工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作。'] 
tmp1=[[word for word in jieba.lcut(doc,cut_all=False)] for doc in corpus]
st.write( tmp1 ) 
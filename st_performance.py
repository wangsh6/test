# -*- coding: utf-8 -*-
"""
各种装饰器。 本质都是用于存储，以减小开销
"""

import streamlit as st 
from PIL import Image
import time
import pandas as pd
# import torch 
from transformers import  AutoModelForSeq2SeqLM


#### 页面头部设置
st.set_page_config(
    page_title="装饰器内存",    #页面标题
    page_icon=":chart_with_upwards_trend:",        #icon  
    # layout="wide",                #页面布局
    # initial_sidebar_state="auto"  #侧边栏 
    
)

#%%  caching  缓存大型的数据集、模型等 当输入函数的参数不变时，刷新网页会直接读取缓存的内容而不会重新加载

# persist 是否在磁盘上持久化
# suppress_st_warning 禁止在函数内部调用 st
# allow_output_mutation ： 当返回值发生变化，进行预警. 若想取消预警，则定义为 True
# show_spinner  当缓存消失时启动旋转器（等待条）
# hash_funcs  dict/None 类型或完全限定名到哈希函数的映射。这用于覆盖Streamlit缓存机制内散列器的行为:当散列器遇到一个对象时，它将首先检查它的类型是否匹配这个字典中的键，如果匹配，将使用提供的函数为它生成一个散列。
# max_entries  int/None 最大缓存数
# ttl  float/None   在缓存中保留一个条目的最大秒数  The default is None.
# st.cache(func=None, persist=False, allow_output_mutation=False, show_spinner=True, suppress_st_warning=False, hash_funcs=None, max_entries=None, ttl=None)


@st.cache(suppress_st_warning=True) 
def load_data(path): 
    df = pd.read_excel(path,sheet_name='result')
    df = df.astype(str)  
    return df

### 第一次读取数据的时间较久。但是第二次从缓存读取，快读；第三次输入变化
#### 只要输入的参数（名）不改变，就不会改变.
ipath = ["data/result01.xlsx" ,"data/result01.xlsx", "data/result02.xlsx"]

for i in ipath:  
    
    t1 = time.time() 
    df = load_data(i)
    st.write(df) 
    st.write( " 方式一运行时间为",time.time() - t1 )  
    

################# 通过哈希的方式传入 . 它会检查文件名与文件修改的时间
#### PS： 未理解通透 

class File:
    def __init__(self, file_name): 
        self.name = file_name 

def hash_file_reference(file_reference):
    filename = file_reference.filename
    return filename

@st.cache(hash_funcs = {File: hash_file_reference} ,allow_output_mutation=True)
def load_data1(file_reference): 
    df = pd.read_excel(file_reference,sheet_name='result')
    df = df.astype(str)  
    return df

for i in ipath:  
    t1 = time.time() 
    df = load_data1(i)
    st.write(df) 
    st.write( " 方式二运行时间为",time.time() - t1 )  



#%%  st.experimental_memo  实验模式 用于存储 pickle 类型数据  & 记住函数的操作
'''
st.experimental_memo(func=None, *, persist=None, show_spinner=True, suppress_st_warning=False, max_entries=None, ttl=None)

st.experimental_memo.clear

'''

#%%%  重要 - 单例模式，即模型的只一次读取  (一样可以使用 cache ； 它属于实验模式)

# path = r"C:\Users\wangsh6\Desktop\py_file\DP_NLP\Hugging Face Transformers"



# @st.experimental_singleton
# def get_model(path):
    
#     model = AutoModelForSeq2SeqLM.from_pretrained( path+ "\pre-model-list\mT5_multilingual_XLSum")       
#     return model

# s1 = time.time() 
# get_model(path)
# st.write("第一次调用模型：时间为： " , time.time()-s1)

# s1 = time.time() 
# get_model(path)
# st.write("第二次调用模型： 时间为： " , time.time()-s1)

# st.experimental_singleton.clear()  ### 清除缓存 

# s1 = time.time() 
# get_model(path)
# st.write("清除缓存后调用：时间为： " , time.time()-s1)

# st.experimental_singleton.clear()


#%%  st.experimental_user 在 streamlit cloud 适用。里面为 字典。 {email: ...@} 
### 可以通过邮箱设置，设置不同用户的使用权限
# 私有程序： 用户必须登录到 云上，有自己的邮箱才可以登录i
# 公共网络： 显示为None 

st.write(st.experimental_user)

ADMIN_USERS = {
    'person1@email.com',
    'person2@email.com',
    'person3@email.com'
}
if st.experimental_user.email in ADMIN_USERS:
    st.write('存在用户')
else: 
    st.write('Please contact me to get access!')





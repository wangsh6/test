# -*- coding: utf-8 -*-
"""
streamlit run st_base01.py
"""

import streamlit as st
import pandas as pd
import numpy as np


#### 编写标题
st.title('测试')



'''
文字与公式的输出
'''

st.write("st，可以写入各种类型的数据")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.markdown("# Streamlit示例")



### 绘制地图 --- 
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data) 



#################### 选项操作 
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)



# -*- coding: utf-8 -*-
"""
streamlit run st_base01.py

https://www.webfx.com/tools/emoji-cheat-sheet/
https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
字体颜色

write 同行输出 公式 + 空格

button 只可以按下一次

文件下载
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image




#### 页面头部设置
st.set_page_config(
    page_title="基础操作测试",    #页面标题
    page_icon=":rainbow:",        #icon  可以是 图片&图标
    # layout="wide",                #页面布局  centered / wide
    # initial_sidebar_state="auto"  #侧边栏 "auto" or "expanded" or "collapsed"
    menu_items={    ### 配置在右边菜单栏希望出现的选项
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# There is Shihao. This is an *extremely* cool app!"
    }
)



# #%%  初始化全局配置。 通过该配置，只有在第一次打开页面的时候才会更改一下配置
# #### session_state 中的变量都可以自己配置. 目的：各控件重新运行之间共享变量的方法
# #### 同时，可以尝试通过 session_state 的配置来进行组件的删除与重现
# if 'first_visit' not in st.session_state:
#     st.session_state.first_visit=True
# else:
#     st.session_state.first_visit=False

# ## 删除 del session_state['first_visit']
# # 初始化全局配置
# if st.session_state.first_visit:
#     st.balloons()  #第一次访问时才会放气球
#     st.snow()  ## 雪花
    
    
# 	#在这里可以定义任意多个全局变量，方便程序进行调用。 名字可自选。本质为 init
#     # st.session_state.XXXX=datetime.datetime.now() + datetime.timedelta(hours=8) #Streamlit Cloud的时区是UTC，加8小时即北京时间


# #%%  标题构造
# '''
# 魔法方式： streamlit 对于 该方法与 "...." 会自动识别，无须编写 st.write() 
# '''

# ############# 标题输出
# st.title("文章的标题")

# ###### 标题输出方式1
# st.header("主标题 st.header")
# st.subheader("副标题 st.subheader")

# ##### 标题输出方式二 ,write 同理
# st.markdown("# 一级标题")
# st.markdown("## 二级标题")
# st.markdown("### 三级标题")

# ##### 
# st.caption("更小号字体，用于显示旁白")

# #%%   字体与颜色( write；markdown；text 均使用 )  
# #### 对于更大字体、颜色。方法一： 查看 st_js.py； 方法二：通过 markdown 语言，但只支持部分
# # :sunglasses:  表示输入为表情   可参考如下2个网址：
# # https://www.webfx.com/tools/emoji-cheat-sheet/
# # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

# #  *World!*   斜体. 或者 _world!_
# #  **巴拉巴拉**  加粗
# st.write("***粗斜体表示***，*斜体表示*，**加粗表示**，~删除线~，表情： :sunglasses:",)

# st.write('<u>下划线</u> ',unsafe_allow_html=True) ## 下划线涉及html，需要开启 html （可以混合使用）

# st.write(">这是一段引用")

# st.markdown('<br>',unsafe_allow_html=True)  ### 添加空行 -- 需要更改 html内容



# #%%  基本输出  write 传入的参数类型可支持字典、DataFrame、func、module、model、error 等多种形式


    
# ########### 3种基本输出方式（区别在于展现的形态有所差异）
# st.write("基本输出方式1: st.write(最常用) ")
# st.markdown("基本输出方式2: st.markdown")
# st.text("基本输出方式3： st.text")

# ########## 输出支持输出数字或者文本，或者混合模式
# st.write(1234,"数字形式输出")
# st.write("1234", "文本形式输出")
# st.write("1 + 1 = ", 2,'混合形式输出')


# ##### 输出列表，write；markdown；text 均使用
# st.write("""
# 无序列表：
# - 元素1
# - 元素2
# - 元素3
# """)


# ###### 输入网址 
# st.write("[学习更多，跳转页面](https://github.com/)")

# #### Latex公式 输出
# #### https://katex.org/docs/supported.html
# st.latex("\sum_{i=1}^{n}")
# st.markdown("[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity.")


# ############ 表格的输出 --- 以DataFrame为例。分为静态与动态2种。
# ### width=none， height=none
# df = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# # write 与 dataframe：动态表格。支持选中与 标记。对于多行使用滑动条查看
# st.write(df)
# st.dataframe(df)
# # table：静态表格。 read_only, 无法选择。对于多行选择直铺到第
# st.table(df) 


# ###### 动态扩增表格  
# ######### 表格、图片可以使用 add_rows() 方法添加新数据
# def func():
#     df1 = pd.DataFrame(
#     np.random.randn(5, 5),
#     columns=("col %d" % i for i in range(5))
#     )
#     tb_table = st.table(df1)
    
#     for i in range(10):
#         df2 = pd.DataFrame(
#             np.random.randn(1, 5),
#             columns=("col %d" % i for i in range(5))
#         )
#         tb_table.add_rows(df2)
#         time.sleep(0.5)
#     return 
# func()



# ######## 展示 代码
# code = """
# def sum_(x):
#     return np.sum(x)
# """
# st.code(code, language="python") 

# #### 展示 Code，同时执行 Code；需要将 code 放入 st.echo() 内
# with st.echo():
#     for i in range(5):
#         st.write("hello")


# #####   用于输出指标
# # delta: None; int; float;string 类型均可
# # delta_color：normal；reverse；off
# st.metric(label='指标输出', value=20, delta='32%', delta_color="normal", help=None)
        
# #%% 控件与侧边栏 若控件想放置在侧边栏，可使用 st.sidebar.控件()

# #######  检查框,输出为 True / False
# res1 = st.sidebar.checkbox("I agree")
# st.sidebar.write(res1)

# ####### 单选框, 与单选按钮相似
# res2 = st.sidebar.selectbox("Which would you like", [1, 2, 3])
# st.sidebar.write(res2)

# ####### 单选按钮
# res3 = st.sidebar.radio("Which would you like", [1, 2, 3])
# st.sidebar.write(res3)

# ####### 多选框。
# selector = st.sidebar.multiselect("Which would you like", [1, 2, 3])
# st.sidebar.write(selector)


# # 数字输入框  min_value=None, max_value=None
# number = st.sidebar.number_input("Insert a number", 123) ### 123为初始值

# # 单行文本输入框  max_chars=None
# word = st.sidebar.text_input("Insert a word", "123")
# st.sidebar.write("The number is", number, "The word is", word)  ### 读取数字用于文本框里面的值

# # 多行文本输入框  max_chars=None ， on_change=None ， args=None
# st.sidebar.text_area("多行文本输入框", "初始值可不填")
# st.sidebar.text_area("多行文本输入框",  placeholder='示例')

# # 日期输入框,默认为今天  value  = datetime.date(2019, 7, 6)
# st.sidebar.date_input("输出日期")

# # 时间输入框    datetime.time(8, 45)
# st.sidebar.time_input("Insert a time")


# ################ 按钮操作
# # 点击按钮。 若按下按钮，则返回 True
# ### on_click: 单击此按钮时调用的可选回调函数
# ### help：当按钮悬停在上面时显示的可选工具提示。
# ### key: int&str 用作小组件唯一键的可选字符串或整数
# #### args &  kwargs 元组参数
# button = st.button("click it",key=None, on_click=None, help=None,args=None,disabled=False)
# st.write("返回值:", button)


# # 滑动条
# ### value 表示当前值，也可以为元组表示范围：value=(25.0, 75.0)
# x = st.sidebar.slider("Square滑动条", min_value=0, max_value=80,step=None,value = 10)
# st.sidebar.write(x, "squared is", np.power(x, 2))

# ### 范围滑动条
# st.select_slider(label='列表滑动条', options=['var1','var2','var3','var4'], value=None)


# #%%   文件的上传与下载 

# #### 上传
# uploaded_file = st.file_uploader("请选择 CSV 文件", type="csv")

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     st.write(data)

# ##### 下载(建议还是使用 button功能，调用回调函数)
# ### MIME: 其他时候可不填。若是数据表，填 mime='text/csv'； 图片为 mime="image/png"

# df= pd.DataFrame(
# np.random.randn(5, 5),
# columns=("col %d" % i for i in range(5))
# )

# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')
# st.download_button(label='下载文件', data=convert_df(df), file_name="生成文件.csv", mime='text/csv', key=None, 
#                    help=None, on_click=None, args=None, kwargs=None, disabled=False)


    

# #%%  特殊效果。可用于增添趣味性

# # 气球效果
# # st.balloons()

# ##### 状态展示
# st.error("错误显示为")
# st.warning("警告显示为")
# st.info("普通消息显示为")
# st.success("成功消息显示为")
# e = RuntimeError('This is an exception of type RuntimeError')
# st.exception(e)


# ##### 进度条
# # 添加占位符
# placeholder = st.empty()
# # 创建进度条
# bar = st.progress(0)

# for i in range(10):
#     time.sleep(0.05)
#     # 不断更新占位符的内容
#     placeholder.text(f"Iteration {i+1}")
#     # 不断更新进度条
#     bar.progress(i + 1)

# # 状态
# st.success("Finished")


# ########### 等待条
# with st.spinner("Wait for it..."): 
#     time.sleep(2)

st.success("Done!")


def func(): 
    st.write('time1')
    st.write(b1)
    


b1 = st.button('run',on_click=func)

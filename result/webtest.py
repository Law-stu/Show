from itertools import count
from tkinter import CENTER
import streamlit as st
import pandas as pd
import numpy as np
import cv2


# 设置网页信息 
st.set_page_config(page_title='基于AI生成的时装设计与虚拟试衣系统')

st.title('基于AI生成的时装设计与虚拟试衣系统')

st.sidebar.title("功能区：")
st.sidebar.text("1 : AI生成衣服")
title = st.sidebar.text_input("请输入你想象的衣服关键词：",)
if title != "":
   st.text("根据关键词AI生成的时装结果如下：")
col1, col2, col3, col4 = st.columns(4)
if title =='女上衣':
   with col1:
      st.image("./生成/女上衣1.png")
      st.text("1")
   with col2:   
      st.image("./生成/女上衣2.png")
      st.text("2")
   with col3:   
      st.image("./生成/女上衣3.png")
      st.text("3")
   with col4:   
      st.image("./生成/女上衣4.png")
      st.text("4")
   title_name = "女上衣"
elif title == "格子衬衫":
   with col1:
      st.image("./生成/格子1.png")
      st.text("1")
   with col2:   
      st.image("./生成/格子2.png")
      st.text("2")
   with col3:   
      st.image("./生成/格子3.png")
      st.text("3")
   with col4:   
      st.image("./生成/格子4.png")
      st.text("4")
   title_name = "2"
elif title == "短袖":
   with col1:
      st.image("./生成/s短袖1.jpg")
      st.text("1")
   with col2:   
      st.image("./生成/s短袖2.jpg")
      st.text("2")
   with col3:   
      st.image("./生成/s短袖3.jpg")
      st.text("3")
   with col4:   
      st.image("./生成/s短袖4.jpg")
      st.text("4")
   title_name = "s短袖"

      
st.sidebar.text("2 : 淘宝店铺衣服搜索")
title1 = st.sidebar.text_input("请输入你想要的衣服关键词：",)
if title1 != "":
   st.text("根据关键词在淘宝店铺搜索的结果如下：")
col11, col21, col31, col41 = st.columns(4)
if title1 =='短袖':
   if title != "":
      count = 4
   else:
      count = 0
   with col11:
      st.image("./淘宝/t短袖1.jpg")
      count +=1
      st.text(count)
   with col21:   
      st.image("./淘宝/t短袖2.jpg")
      count +=1
      st.text(count)
   with col31:   
      st.image("./淘宝/t短袖3.jpg")
      count +=1
      st.text(count)
   with col41:   
      st.image("./淘宝/t短袖4.jpg")
      count +=1
      st.text(count)
   Taobao = "t短袖"
elif title1 == "女衣服":
   if title != "":
      count = 4
   else:
      count = 0
   with col11:
      st.image("./淘宝/女衣服1.jpg")
      count +=1
      st.text(count)
   with col21:   
      st.image("./淘宝/女衣服2.jpg")
      count +=1
      st.text(count)
   with col31:   
      st.image("./淘宝/女衣服3.jpg")
      count +=1
      st.text(count)
   with col41:   
      st.image("./淘宝/女衣服4.jpg")
      count +=1
      st.text(count)
   Taobao = "女衣服"





col5, col6 ,col7= st.columns(3)
uploaded_file = st.sidebar.file_uploader("上传换衣模特照片", type=["jpg", "png", "bmp", "jpeg"])

with col5:
   if uploaded_file is not None:
      # 将传入的文件转为Opencv格式
      file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
      opencv_image = cv2.imdecode(file_bytes, 1)
      # 展示图片
      st.text("换衣人物图片如下：")
      st.image(opencv_image, channels="BGR")
      # # 保存图片
      # cv2.imwrite('test.png',opencv_image)
      model_name = uploaded_file.name


option = st.sidebar.selectbox('选择你喜欢的一件衣服进行换装：', (' ','1', '2', '3','4','5','6','7','8'))
if option !=' ':
   if int(option) <=4:
      with col6:
         if title != "":
            st.text("你选择换装的衣服为：")
            st.image('./生成/'+title_name+option+".jpg")
            name =title_name+str(option)
         else:
            st.text("你选择换装的衣服为：")
            st.image('./淘宝/'+Taobao+option+".jpg")
            name =Taobao+str(option)
   elif int(option)>4:
      opt = int(option)-4
      with col6:
         st.text("你选择换装的衣服为：")
         st.image('./淘宝/'+Taobao+str(opt)+".jpg")
         name =Taobao+str(opt)


if st.sidebar.button('确认进行换装'):

   with col7:
      st.text("换装结果如下：")
      st.image('./result/'+model_name[0:2]+"_"+name+".jpg") 
      

      





# # 背景图片的网址
# img_url = 'https://png.pngtree.com/background/20210714/original/pngtree-blue-carbon-background-with-sport-style-and-golden-light-picture-image_1200848.jpg'

# # 修改背景样式
# st.markdown('''<style>.css-fg4pbf{background-image:url(''' + img_url + ''');
# background-size:100% 100%;background-attachment:fixed;}</style>
# ''', unsafe_allow_html=True) 
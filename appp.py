import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# إعداد الصفحة
st.set_page_config(page_title="تطبيق Streamlit جميل", layout="centered")

# العنوان
st.markdown("<h1 style='text-align: center; color: #4B0082;'>مرحباً بك في تطبيق Streamlit</h1>", unsafe_allow_html=True)

# إدخال البيانات في بطاقات
with st.container():
    st.subheader("أدخل بياناتك")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("اسمك")
    with col2:
        age = st.number_input("عمرك", min_value=1, max_value=120, value=25)

# زر لإظهار البيانات
if st.button("اعرض البيانات"):
    st.success(f"مرحباً {name}, عمرك {age} سنة!")

# مثال على رسم بيانات
st.subheader("رسم بياني توضيحي")
data = np.random.randn(100)
fig, ax = plt.subplots(figsize=(8,4))
sns.histplot(data, kde=True, color="#4B0082", ax=ax)
ax.set_title("توزيع البيانات العشوائية", fontsize=14)
st.pyplot(fig)

# تذييل الصفحة
st.markdown("<hr><p style='text-align:center;'>تطبيق Streamlit بتصميم جميل</p>", unsafe_allow_html=True)
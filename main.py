import streamlit as st
from dataset import *
# Set the page title
# st.title("مساجل الشعر العربي")
st.markdown('''
            <div dir="rtl"> 
            <h1 dir="center"> مساجل الشعر العربي </h1>
<h2>هذا الموقع لزيادة المقدرة على المساجلة الشعرية</h2>
<h3> الطريق كالتالي: تكتب بيت الشعر ثم الحاسوب يجيبك ببيت أوله آخر بيتك وأنت تعيد الجواب على نفس المنوال </h3>
 </div>
''',unsafe_allow_html=True)

# Load your photo
photo = "title2.jpg"
if photo is not None:
    st.image(photo, caption="", use_column_width=True)
# Load your photo
photo2 = "mosajel.jpg"
if photo2 is not None:
    st.image(photo2, caption="", use_column_width=True)
# Create two text input boxes
st.markdown('''
<div dir="rtl">
<h5>اكتب بيت الشعر هنا</h5> 
</div>
''',unsafe_allow_html=True)
arabic_text = st.text_input("بيت شعرٍ", "وهكذا المثال ... بيت لطيفٌ قالوا")
last_letter = ""
# result_text = st.text_input("Result:", "", key="result")
if arabic_text != "" or arabic_text != " ":
    if arabic_text[-1] == "ة":
        last_letter = "ت"
    else:
        if arabic_text == "" or arabic_text == " ":
            last_letter = "أ"
        else:
            last_letter = arabic_text[-1] 
    # Define a dictionary to store responses based on user input
    loader = Loader()
    dataset = loader.loads()
    result_text = loader.take_sample(dataset, last_letter)
else:
    result_text = "أدخل بيت شعر أو أول حرفٍ منه"

# Display the result

st.text_area("Result:", result_text, disabled=True)

# Optionally, you can add a button to clear the input
if st.button("مرة أخرى"):
    arabic_text = ""
    result_text = ""

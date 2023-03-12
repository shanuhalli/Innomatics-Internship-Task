import os
from PIL import Image
import streamlit as st
import streamlit.components.v1 as stc

path = os.path.dirname(__file__)
my_file = path +'/resources/images/Innomatics.png'
img1 = Image.open(my_file)
st.image(img1,width=700)

html_temp = """<h1 align="center"> Hello, I'm Shanu Halli </h1>
		   <h2 align="center"> A Passionate Data Science Learner </h2> """

st.balloons()
stc.html(html_temp)

path = os.path.dirname(__file__)
my_file = path +'/resources/images/Shanu.JPG'
img2 = Image.open(my_file)
st.image(img2)

st.markdown ("<h3 style='color:#1C1CA6'>🙋‍♂️ About Myself </h3>",unsafe_allow_html=True)
st.write("""
		##### I am an enthusiast for new technology. 
		##### I learn data science to pursue a career in the field of Data Science. 		
		##### I am passionate about what I do, and I love to help people.
		""")

st.markdown ("<h3 style='color:#1C1CA6'>👨‍💻 Machine Learning Projects </h3>",unsafe_allow_html=True)
st.write("""
		##### 1. Real Estate Price Prediction.
		##### 2. Gold Price Forecasting.
        """)

st.markdown("<h3 style='color:#1C1CA6'>🔗Connect with me</h3>",unsafe_allow_html=True)
st.markdown('''
        </h3> 
        <a href="https://github.com/shanuhalli" target="_blank"><img alt="Github" width="40px" src="https://cdn-icons-png.flaticon.com/512/733/733553.png"></a> &nbsp&nbsp&nbsp
        <a href="https://www.linkedin.com/in/hallishanu" target="_blank"><img alt="LinkedIn" width="40px" src="https://cdn-icons-png.flaticon.com/512/3536/3536505.png"></a> &nbsp&nbsp&nbsp
        <a href="https://www.instagram.com/shanu_halli" target="_blank"><img alt="Instagram" width="40px" src="https://cdn-icons-png.flaticon.com/512/1384/1384063.png"></a> &nbsp&nbsp&nbsp
		</p> 
    	''',unsafe_allow_html=True)

# socials  = ["LinkedIn", "Github", "GMail"]
# linkedin = "https://www.linkedin.com/in/hallishanu"
# github   = "https://github.com/shanuhalli"
# mail     = "shanuhalli@gmail.com"

# with st.expander(label='Check my Socials Links',expanded=True):
# 	a = st.selectbox("Socials", socials)
# 	if a =="LinkedIn":
# 		st.write(linkedin)
# 	elif a =="Github":
# 		st.write(github)
# 	elif a=="GMail":
# 		st.write(mail)

st.write("### Thank you for your time... ")
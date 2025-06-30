# ##Pip install streamlit

# python library
# webpage for Ai and Data set project
# html css No requirement
#####run ke liye streamlit run st(file name).py



import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import time 

#page configuration 

st.set_page_config(
    page_title = "streamlit Fuction demo",
    page_icon = "👻",
    layout="centered"
    
)
##title and text element
st.title("Hello World")
st.header("1. text element")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,code text")
st.code("print('hello everyone')",language="python")
st.latex(r'a^2+b^2=c^2')



##metrices and messages      

st.header("2. metrices and messages")
st.metric(label="Reverse",value=65334,delta='+10%',delta_color="normal")
st.error("this is an enter message")
st.warning("this is a warning message")
st.info("this is a info message")
st.success("this is a success message")
st.exception(ValueError("this is an exception message"))


##Data Display
st.header("3. Data Display")
df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())

##charts
st.header("4. Charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)



st.divider()
##File Handling 
##Generator and decorator
##Multithreading and multiprocessing
##method overloading and overriding
##debug and unit testing 

st.header("6. Widgets")
with st.form("input form"):
    name  = st.text_input("Enter your name", type="password")
    age = st.number_input("Enter your age")
    mood = st.radio("Select your mood",("Happy","sad","neutral"))
    Language = st.multiselect("Select your language",("English","Hindi"))
    submit = st.form_submit_button("Submit")

    if submit :
        st.success(f"Name : {name}, Age : {int(age)}, mood : {mood}, Language : {Language}")


col1, col2,col3= st.columns((4,1,1))
with col1:
    st.text_input("Enter your name")
    st.number_input("Enter your age")

with col2:
    st.radio("Select your mood",("Happy","sad","neutral"))
    st.multiselect("Select your language",("English","Hindi"))

with col3:
    st.title("Output")


    ##you can divide form into multiple columns 
    ##for that first define form the define columns 

col1, col2 = st.columns(2)

with col1:
    number = st.slider("Select a number",0,100)
with col2:
    colour = st.color_picker("select a colour")

st.text_area("Enter your message")
st.date_input("Select a date")
st.time_input("Select a time")
st.file_uploader("Select a file")

##Media 

st.header("7. media")
st.image("https://picsum.photos/400",caption="random image")
st.video("https://www.youtube.com/watch?v=OMEA1uxBPe8")
st.audio("https://www.youtube.com/watch?v=OMEA1uxBPe8")


##Sidebar and layout

st.sidebar.header("sidebar header")
st.sidebar.write("this is a sidebar text")
st.sidebar.button("click on")
option = st.sidebar.selectbox("select an option",("option 1","option 2","option 3"))

with st.container():
    st.write("this is a container")

with st.expander("expander header"):
    st.write("this is a expander")

with st.spinner("loading data ...."):
    time.sleep(10)
# st.success("data loaded")
st.toast("toast message",icon="😱")

st.page_link("https://www.youtube.com/",label="youtube website",icon="😀")


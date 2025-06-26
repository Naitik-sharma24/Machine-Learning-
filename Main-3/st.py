# ##Pip install streamlit

# python library
# webpage for Ai and Data set project
# html css No requirement



import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

#page configuration 

st.set_page_config(
    page_title = "streamlit Fuction demo",
    page_icon = "👌",
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
st.metric(label="Reverse",value=65334,delta='+10%',delta_color="inverse")
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
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image 


st.set_page_config(page_title = "Survey Results",layout='wide')
st.header("Survey Results 2021")
st.subheader("survey of different department")

url = r'C:\Users\07936P744\Desktop\python\dashboard\survey\Survey_Results.xlsx'
url1 = r'C:\Users\07936P744\Desktop\python\dashboard\survey\pic.PNG'

df = pd.read_excel(url,sheet_name='DATA',skiprows =3, usecols = 'B:D')
df1 = pd.read_excel(url,sheet_name='DATA',skiprows =3, usecols = 'F:G')

#----------------------------------------------------------------------#
dept = df.Department.unique().tolist()
ages = df.Age.unique().tolist()
age_selection = st.slider("Age:",min_value=min(ages), max_value=max(ages),value=(min(ages),max(ages)))
dept_selection = st.multiselect("Department:",dept, default =dept)

mask = df.Age.between(*age_selection) & df.Department.isin(dept_selection)
result = df[mask].shape[0]
st.markdown(f'*Availble result is:{result}*')
df_grouped = df[mask].groupby(by="Rating").count()[["Age"]]
df_grouped= df_grouped.rename(columns={"Age":"vote"})
df_grouped = df_grouped.reset_index()
bar_chart = px.bar(df_grouped,x = "Rating", y="vote", text="vote",
                   color_discrete_sequence= ['#F63366']*len(df_grouped),
                   template= 'plotly_white')

st.plotly_chart(bar_chart)

col1, col2 = st.columns(2)

col1.dataframe(df)
df1 = df1.dropna()
p_chart = px.pie(df1,title="Total no of participants",values="Participants",names="Departments")

st.plotly_chart(p_chart)

img = Image.open(url1)

col2.image(img,caption="designed by streamlit",use_column_width = True)
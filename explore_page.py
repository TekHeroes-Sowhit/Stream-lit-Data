
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories,cutoff):
    categorical_map={}
    for i in range(len(categories)):
        if categories.values[i]>=cutoff:
            categorical_map[categories.index[i]]=categories.index[i]
        else:
            categorical_map[categories.index[i]]='Other'
    return categorical_map
def clean_experience(x):
    if x=='More than 50 years':
        return 50
    if x=="Less than 1 year":
        return 0.5
    return float(x)
def clean_education(x):
    if 'Bachelors degree' in x:
        return 'Bachelors Degree'
    if 'Master Degree' in x:
        return 'Master Degree'
    return 'less than a bachelor'

@st.cache
def load_data():
    df=pd.read_csv()
    df=df[["Country","EdLevel","YearsCodePro","Employment","ConvertedComp"]]
    df=df[df["ConvertedComp"].notnull()]
    df=df.dropna()
    df=df[df["Employment"]=='Employed full-time']
    df=df.drop("Employment",axis=1)
    country_map=shorten_categories(df.Country.value_counts(),400)
    df["Country"]=df[df["ConvertedComp"]<=2500]
    df=df[df["ConvertedComp"]>=10000]
    df=df[df["Country"]!="Other"]
    df["YearsCodePro"]=df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"]=df["EdLevel"].apply(clean_education)
    return df

df=load_data()

def show_explore_page():
    st.title('new')
    st.write("""
    Stack overflow developer salary
    """)
    data=df["Countrt"].value_counts()
    fig1,ax1=plt.subplots()
    ax1.pie(data,labels=data.index,autopct="%1.1f",shadow=True,stratangle=90)
    ax1.axis("equal")
    st.write("# no of data from different countries")
    st.pyplot(fig1)
    
    


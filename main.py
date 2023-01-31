import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from pandas.core.frame import DataFrame




df=pd.read_csv("./Stocks of frozen poultry meat.csv")
labels = ['Chicken', 'Turkey', 'Ducks', 'Geese ', 'Other fowl']
month=[]

turkey=[]
turkey_on=[]
turkey_que=[]
turkey_alt=[]
turkey_man=[]
turkey_sas=[]
turkey_alb=[]
turkey_bc=[]



duck=[]
duck_on=[]
duck_que=[]
duck_alt=[]
duck_man=[]
duck_sas=[]
duck_alb=[]
duck_bc=[]

geese=[]
geese_on=[]
geese_que=[]
geese_alt=[]
geese_man=[]
geese_sas=[]
geese_alb=[]
geese_bc=[]


genre = st.radio("Meat Item",['duck','geese','turkey'])
if(genre=='turkey'):
    for row in df.itertuples():
        if (getattr(row,'REF_DATE')>='2020-01') :
            month.append(getattr(row,'REF_DATE'))
            if(getattr(row,'GEO') =='Ontario' and getattr(row,'Commodity')=='Turkeys, total'):
                turkey_on.append(getattr(row,'VALUE'))
            if(getattr(row,'GEO') =='Quebec' and getattr(row,'Commodity')=='Turkeys, total'):
                turkey_que.append(getattr(row,'VALUE'))
            if (getattr(row, 'GEO') == 'Atlantic provinces' and getattr(row,'Commodity')=='Turkeys, total'):
                turkey_alt.append(getattr(row, 'VALUE'))
            if(getattr(row,'GEO') =='Manitoba' and getattr(row,'Commodity')=='Turkeys, total'):
                turkey_man.append(getattr(row,'VALUE'))
            if(getattr(row,'GEO') =='Saskatchewan' and getattr(row,'Commodity')=='Turkeys, total'):
                turkey_sas.append(getattr(row,'VALUE'))
            if(getattr(row,'GEO') =='Alberta' and getattr(row,'Commodity')=='Turkeys, total'):
                turkey_alb.append(getattr(row,'VALUE'))
            if(getattr(row,'GEO') =='British Columbia' and getattr(row,'Commodity')=='Turkeys, total'):
                turkey_bc.append(getattr(row,'VALUE'))
    turkey.append(turkey_on)
    turkey.append(turkey_que)
    turkey.append(turkey_alt)
    turkey.append(turkey_man)
    turkey.append(turkey_sas)
    turkey.append(turkey_alb)
    turkey.append(turkey_bc)
    df2=DataFrame(turkey)
    df2 = df2.T


    df2.rename(columns={0:'Ontario',1:'Quebec',2:'Atlantic provinces',3:'Manitoba',4:'Saskatchewan',5:'Alberta',6:'British Columbia'},inplace=True)
    df2.rename(index={0:'2020-01',1:'2020-02',2:'2020-03',3:'2020-04',4:'2020-05',5:'2020-06',6:'2020-07',7:'2020-08',8:'2020-09',9:'2020-10',10:'2020-11',11:'2020-12',12:'2021-01',13:'2021-02',14:'2021-03',15:'2021-04',16:'2021-05',17:'2021-06',18:'2021-07',19:'2021-08',20:'2021-09',21:'2021-10',22:'2021-11',23:'2021-12',24:'2022-01',25:'2022-02',26:'2022-03',27:'2022-04',28:'2022-05',29:'2022-06',30:'2022-07',31:'2022-08',32:'2022-09',33:'2022-10',34:'2022-11',35:'2022-12',},inplace=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Food Trends in Canada in the Past Three Years </h4>", unsafe_allow_html=True)
    st.line_chart(df2)
if(genre=='geese'):
    for row in df.itertuples():
        if (getattr(row,'REF_DATE')>='2020-01'):
            month.append(getattr(row,'REF_DATE'))
            if (getattr(row, 'GEO') == 'Ontario' and getattr(row, 'Commodity') == 'Geese, total'):
                geese_on.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Quebec' and getattr(row, 'Commodity') == 'Geese, total'):
                geese_que.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Atlantic provinces' and getattr(row, 'Commodity') == 'Geese, total'):
                geese_alt.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Manitoba' and getattr(row, 'Commodity') == 'Geese, total'):
                geese_man.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Saskatchewan' and getattr(row, 'Commodity') == 'Geese, total'):
                geese_sas.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Alberta' and getattr(row, 'Commodity') == 'Geese, total'):
                geese_alb.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'British Columbia' and getattr(row, 'Commodity') == 'Geese, total'):
                geese_bc.append(getattr(row, 'VALUE'))
    geese.append(geese_on)
    geese.append(geese_que)
    geese.append(geese_alt)
    geese.append(geese_man)
    geese.append(geese_sas)
    geese.append(geese_alb)
    geese.append(geese_bc)
    df2=DataFrame(geese)
    df2 = df2.T


    df2.rename(columns={0:'Ontario',1:'Quebec',2:'Atlantic provinces',3:'Manitoba',4:'Saskatchewan',5:'Alberta',6:'British Columbia'},inplace=True)
    df2.rename(index={0:'2020-01',1:'2020-02',2:'2020-03',3:'2020-04',4:'2020-05',5:'2020-06',6:'2020-07',7:'2020-08',8:'2020-09',9:'2020-10',10:'2020-11',11:'2020-12',12:'2021-01',13:'2021-02',14:'2021-03',15:'2021-04',16:'2021-05',17:'2021-06',18:'2021-07',19:'2021-08',20:'2021-09',21:'2021-10',22:'2021-11',23:'2021-12',24:'2022-01',25:'2022-02',26:'2022-03',27:'2022-04',28:'2022-05',29:'2022-06',30:'2022-07',31:'2022-08',32:'2022-09',33:'2022-10',34:'2022-11',35:'2022-12',},inplace=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Food Trends in Canada in the Past Three Years </h4>", unsafe_allow_html=True)
    st.line_chart(df2)
if(genre=='duck'):
    for row in df.itertuples():
        if (getattr(row,'REF_DATE')>='2020-01'):
            month.append(getattr(row,'REF_DATE'))
            if (getattr(row, 'GEO') == 'Ontario' and getattr(row, 'Commodity') == 'Ducks, total'):
                duck_on.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Quebec' and getattr(row, 'Commodity') == 'Ducks, total'):
                duck_que.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Atlantic provinces' and getattr(row, 'Commodity') == 'Ducks, total'):
                duck_alt.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Manitoba' and getattr(row, 'Commodity') == 'Ducks, total'):
                duck_man.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Saskatchewan' and getattr(row, 'Commodity') == 'Ducks, total'):
                duck_sas.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'Alberta' and getattr(row, 'Commodity') == 'Ducks, total'):
                duck_alb.append(getattr(row, 'VALUE'))
            if (getattr(row, 'GEO') == 'British Columbia' and getattr(row, 'Commodity') == 'Ducks, total'):
                duck_bc.append(getattr(row, 'VALUE'))
    duck.append(duck_on)
    duck.append(duck_que)
    duck.append(duck_alt)
    duck.append(duck_man)
    duck.append(duck_sas)
    duck.append(duck_alb)
    duck.append(duck_bc)
    df2=DataFrame(duck)
    df2 = df2.T


    df2.rename(columns={0:'Ontario',1:'Quebec',2:'Atlantic provinces',3:'Manitoba',4:'Saskatchewan',5:'Alberta',6:'British Columbia'},inplace=True)
    df2.rename(index={0:'2020-01',1:'2020-02',2:'2020-03',3:'2020-04',4:'2020-05',5:'2020-06',6:'2020-07',7:'2020-08',8:'2020-09',9:'2020-10',10:'2020-11',11:'2020-12',12:'2021-01',13:'2021-02',14:'2021-03',15:'2021-04',16:'2021-05',17:'2021-06',18:'2021-07',19:'2021-08',20:'2021-09',21:'2021-10',22:'2021-11',23:'2021-12',24:'2022-01',25:'2022-02',26:'2022-03',27:'2022-04',28:'2022-05',29:'2022-06',30:'2022-07',31:'2022-08',32:'2022-09',33:'2022-10',34:'2022-11',35:'2022-12',},inplace=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Food Trends in Canada in the Past Three Years </h4>", unsafe_allow_html=True)
    st.line_chart(df2)















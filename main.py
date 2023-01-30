import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from pandas.core.frame import DataFrame




df=pd.read_csv(r"C:\Users\Rambo\PycharmProjects\CSE780\Stocks of frozen poultry meat.csv")
labels = ['Chicken', 'Turkey', 'Ducks', 'Geese ', 'Other fowl']
chicken_list=['Grade A chickens, under 2 kilograms, total','Other chicken, under 2 kilograms, total','Grade A chickens, 2 kilograms and over, total','Other chicken, 2 kilograms and over, total','Chicken further processed, total']
other_fowl_list=['Reported Grade A fowl, total','Other fowl, total']
month=[]
chicken=[]
turkey=[]
duck=[]
geese=[]
other_fowl=[]
on_chicken_amount=0
on_other_fowl_amount=0
for row in df.itertuples():
    if (getattr(row,'REF_DATE')>='2020-01') and (getattr(row,'GEO')=='Ontario') :
        month.append(getattr(row,'REF_DATE'))
        if len(month)>2 and month[-1]!=month[-2]:
            chicken.append(on_chicken_amount)
            other_fowl.append(on_other_fowl_amount)
            on_chicken_amount = 0
            on_other_fowl_amount = 0
        if(getattr(row,'Commodity') in chicken_list):
            on_chicken_amount+=getattr(row,'VALUE')
        if(getattr(row,'Commodity') in other_fowl_list):
            on_other_fowl_amount+=getattr(row,'VALUE')
        if(getattr(row,'Commodity') =='Turkeys, total'):
            turkey.append(getattr(row,'VALUE'))
        if (getattr(row, 'Commodity') == 'Ducks, total'):
            duck.append(getattr(row, 'VALUE'))
        if(getattr(row,'Commodity') =='Geese, total'):
            geese.append(getattr(row,'VALUE'))

chicken.append(on_chicken_amount)
other_fowl.append(on_other_fowl_amount)
month_list=sorted(list(set(month)))
total_list=[]

total_list.append(chicken)
total_list.append(duck)
total_list.append(geese)
total_list.append(turkey)
total_list.append(other_fowl)

df2=DataFrame(total_list)
df2=df2.T
df2.rename(columns={0:'chicken',1:'duck',2:'geese',3:'turkey',4:'other fowl'},inplace=True)
df2.rename(index={0:'2020-01',1:'2020-02',2:'2020-03',3:'2020-04',4:'2020-05',5:'2020-06',6:'2020-07',7:'2020-08',8:'2020-09',9:'2020-10',10:'2020-11',11:'2020-12',12:'2021-01',13:'2021-02',14:'2021-03',15:'2021-04',16:'2021-05',17:'2021-06',18:'2021-07',19:'2021-08',20:'2021-09',21:'2021-10',22:'2021-11',23:'2021-12',24:'2022-01',25:'2022-02',26:'2022-03',27:'2022-04',28:'2022-05',29:'2022-06',30:'2022-07',31:'2022-08',32:'2022-09',33:'2022-10',34:'2022-11',35:'2022-12',},inplace=True)



st.markdown("<h4 style='text-align: center; color: black;'>Food Trends in Ontario in the Past Three Years </h4>", unsafe_allow_html=True)
st.line_chart(df2)

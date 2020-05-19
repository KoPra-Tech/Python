# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:34:05 2020

@author: KoPra
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.getcwd()

#Question b

hur = pd.read_csv("hurricanes.csv",sep='|')

hur.dtypes

pd.set_option('display.max_columns',10)

pd.set_option('display.max_rows',200)

hur.head(5)

#Question c

hur = pd.read_csv("hurricanes.csv",sep='|',usecols=['Month','Highest_Category'])

hur.describe()

hur.dtypes

#Replacing TS as 0.5 for better understanding

hur['Highest_Category']=hur['Highest_Category'].str.replace('TS','0.5')

hur.groupby('Month')['Highest_Category'].max()

hur1=pd.DataFrame(hur.groupby('Month')['Highest_Category'].max())

hur1=hur1.reset_index()

plt.scatter(x=hur1['Month'],y=hur1['Highest_Category'])

plt.title('Scatterplot of Highest Category by Month')

plt.xlabel('Month')

plt.ylabel('Highest Category')

plt.show()

#Question d

hur = pd.read_csv("hurricanes.csv",sep='|',usecols=['Central_Pressure_mb','Max_Winds_kt'])

hur.describe()

hur.dtypes

hur.corr('pearson')

plt.scatter(hur['Central_Pressure_mb'],hur['Max_Winds_kt'])

plt.title('Winds in kt by Pressure in mb')

plt.xlabel('Central Pressure')

plt.ylabel('Max Winds')

plt.show()

#Question e

hur = pd.read_csv("hurricanes.csv",sep='|',usecols=['Central_Pressure_mb','Highest_Category'])

hur.describe()

hur.dtypes

#Replacing TS as 0.5 for better understanding

hur['Highest_Category'] = hur['Highest_Category'].replace('TS', 0.5)

hur['Highest_Category'] = hur['Highest_Category'].astype(float)

hur.corr('pearson')

plt.scatter(hur['Central_Pressure_mb'],hur['Highest_Category'])

plt.title('Highest Category by Pressure in mb')

plt.xlabel('Central Pressure')

plt.ylabel('Highest Category')

plt.show()

#Question f

hur = pd.read_csv("hurricanes.csv",sep='|',usecols=['Month','Highest_Category'])

hur.describe()

hur.dtypes

hur.groupby('Month').size().sort_values(ascending=False)

hur1= pd.DataFrame(hur.groupby('Month').size().sort_values(ascending=False))

hur1=hur1.reset_index()

hur1=hur1.rename(columns={0:'Frequency'})

plt.bar(hur1['Month'],hur1['Frequency'],color='Blue')

plt.title('Barplot of frequency of Hurricanes by Month')

plt.xlabel('Months')

plt.ylabel('Frequency')

plt.show()

#Question g

hur = pd.read_csv("hurricanes.csv",sep='|',usecols=['States_Affected'])

hur=hur.drop('States_Affected', axis=1).join(hur['States_Affected'].str.split(';',expand=True).stack().reset_index(level=1,drop=True).rename('States_Affected'))

hur=hur.reset_index().drop('index',axis=1)

hur.dtypes

for i in range(len(hur)):
    #print(hur['States_Affected'][i])
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('I-','')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace(' ',',')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('FL,NW','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('FL,SW','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('FL,SE','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('FL,NE','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('TX,C','TX,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('TX,S','TX,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('TX,N','TX,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('NW','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('SW','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('SE','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('NE','FL,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('AL1','AL,1')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace('LA2','LA,2')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace(',C',',TX,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace(',S',',TX,')
    hur['States_Affected'][i]=hur['States_Affected'][i].replace(',N',',TX,')

hur=hur.drop('States_Affected', axis=1).join(hur['States_Affected'].str.split(',',expand=True).stack().reset_index(level=1,drop=True).rename('States_Affected'))

hur=hur.reset_index().drop('index',axis=1)

hur = pd.DataFrame({'States_Affected':hur['States_Affected'].iloc[::2].values, 'Category':hur['States_Affected'].iloc[1::2].values})

hur    #Answer for g

hur.describe()

#Question i 'continuation'
hur['Number of Storms']=1

storm_state=pd.DataFrame(hur.groupby(['States_Affected','Category'])['Number of Storms'].sum())

ax=storm_state.plot(kind='bar', stacked=True, figsize=(18.5, 10.5),title='Number of Storms per State for each Category')

ax.set_xlabel('States,Category')

ax.set_ylabel('Frequency')


#Question h

hur = pd.read_csv("hurricanes.csv",sep='|',usecols=['Year','States_Affected'])

hur=hur.drop('States_Affected', axis=1).join(hur['States_Affected'].str.split(';',expand=True).stack().reset_index(level=1,drop=True).rename('States_Affected'))

hur=hur.reset_index().drop('index',axis=1)

hur['Year and States_Affected']=hur['Year'].astype(str)+','+hur['States_Affected']

hur=hur.drop('Year',axis=1).drop('States_Affected',axis=1)

hur.dtypes

for i in range(len(hur)):
    #print(hur['Year and States_Affected'][i])
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('I-','')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace(' ',',')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('FL,NW','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('FL,SW','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('FL,SE','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('FL,NE','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('TX,C','TX,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('TX,S','TX,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('TX,N','TX,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('NW','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('SW','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('SE','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('NE','FL,')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('AL1','AL,1')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace('LA2','LA,2')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace(',C1',',TX,1')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace(',S2',',TX,2')
    hur['Year and States_Affected'][i]=hur['Year and States_Affected'][i].replace(',N1',',TX,1')


l=[]

df3=pd.DataFrame()

df2=hur['Year and States_Affected'].str.split(',',expand=True)

for i in range(len(df2)):
    df3.loc[i,'0']=df2[0][i]
    df3.loc[i,'1']=df2[1][i]
    df3.loc[i,'2']=df2[2][i]
    
    if(df2[3][i]!=None and df2[4][i]!=None):
        print(df2[0][i],df2[3][i],df2[4][i])
        
        l.append( [(df2[0][i]),(df2[3][i]),(df2[4][i]) ] )
        df3 = df3.append({'0' : str(df2[0][i]),'1' : str(df2[3][i]) , '2' : str(df2[4][i])} , ignore_index=True)
        
    if(df2[5][i]!=None and df2[6][i]!=None):
        print(df2[0][i],df2[5][i],df2[6][i])
        df3 = df3.append({'0' : df2[0][i],'1' : df2[5][i] , '2' : df2[6][i]} , ignore_index=True)
        l.append( [(df2[0][i]),(df2[3][i]),(df2[4][i]) ] )
        
df4 = df3.append(pd.DataFrame(l, columns=['0','1','2']),ignore_index=True)

df4=df4.rename(columns={'0':'Year','1':'States_Affected','2':'Category'})

df4=df4.drop('States_Affected',axis=1)

df4['Number of Storms']=1

storm_year=pd.DataFrame(df4.groupby(['Year','Category'])['Number of Storms'].sum())

ax=storm_year.plot(kind='bar', stacked=True, figsize=(100,60))

ax.set_title('Number of Storms per Year for each Category',fontsize=50)

ax.set_xlabel('Year,Category',fontsize=50)

ax.set_ylabel('Frequency',fontsize=50)

#Question j

hur = pd.read_csv("hurricanes.csv",sep='|',usecols=['Central_Pressure_mb','Max_Winds_kt'])

hur.describe()

hur.dtypes

hur.corr('pearson')

hur=hur.drop(238)

plt.boxplot(hur['Central_Pressure_mb'])

plt.boxplot(hur['Max_Winds_kt'])
    
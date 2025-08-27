import pandas as pd
s = pd.Series([10,20,30,40])
data = {'Name':['Tony Stark','Steve Rogers','Bruce Banner','Clint Barton','Natasha Romanoff','Thor Odinson'],'Age':[42,105,44,42,42,None]}
#df = pd.DataFrame(data)
#print(f"\n{df.head()}")
#print(f"\n{df.head(3)}")
#print(df.tail())
#print(f"\n{df.tail(2)}")
#print(df.info())
#print(df.describe())
#print(df.columns)
#print(df.shape)

df = pd.DataFrame(data,index=['a','b','c','d','e','f'])
#print(df.loc['a':'c'])
#print(df.loc['a','Name'])

#print(df.iloc[0])
#print(df.iloc[1,0])
#print(df.iloc[:,0:2])
#print(df.isnull())
#print(df.dropna())  #drops the null row
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)
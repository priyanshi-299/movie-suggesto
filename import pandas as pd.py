import pandas as pd 
print(pd.__version__)
hi=pd.Series([1,2,3],index=[4,5,6])
print(hi)
hey={'roll.no':pd.Series([1,2,3]),'name':pd.Series([4,5,6]),'age':([7,8,9])}
huh=pd.DataFrame(hey)
print(huh)
df=pd.read_csv("D:\dataset\Book1.csv")
print(df)
print(df.columns)
print(df.shape)
print(df.head(1))#1st trip
print(df.tail(1))#last trip
print(df.describe())
print(df.info())
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())
print(df.dropna())#drops rows with null element default axis=0
print(df.dropna(axis=1))
print(df.dropna(how='any'))#agar any ki jagah all kiya to agar sare elements null honge tabhi remove hoga vo row
# df=df.dropna(inplace=True)#replaces dataset with dataset with no null elemenet or any operation 
# print(df)
print(df.fillna(0))
# print(df.fillna(0,inplace=True))
print(df.fillna({'name':'none', 'age':0}))
# df.fillna(method='ffill')fill with previous value
print(df['age'].fillna(value=df['age'].mean()))
# df.replace(2,4)
# df.replace(to_replace=[1,2,3,4],value='A')
# df.replace(to_replace=[1,2,3,4],value=['a','b','c','d'])
#df['age'].replace..... replaces only age column
print(df.replace('[A-Za-z]',0,regex=True))#replaces string with 0
# print(df.drop(['age'],axis=1))
# df2=pd.read_csv("D:\dataset\Book1.csv",index_col=['roll.no'])#this will consider roll.no as index
# print(df2.loc[1,['name']])
# print(df2.loc[df['age']<50])#loc ke andar conditions dete jao
# print(df2.iloc[0:1,1:2])#it considers normal indexes
ri=df.groupby(by='age')
print(ri.groups)
ri=df.groupby(by=['roll.no','age'])
print(ri.groups)
for group,data_frame in ri:
    print(group)
    print(data_frame) 
df1=pd.DataFrame({'rollno':[1,2,3],'physics':[34,45,56]})
df2=pd.DataFrame({'rollno':[1,2,3],'maths':[4,5,6]})
print(pd.merge(df1,df2))#how='left', right, outer
print(df1._append(df2,ignore_index=True))
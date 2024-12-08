import pandas as pd
df=pd.read_csv('data_studentlist.csv')
#print(df)

genders=df['gender'].value_counts()
proportion=genders['M'] / genders['F']
print('Proportion of male to female is ',proportion)

print('---------------------------------------------------------------------')

average=df.groupby('gender')['height'].mean()
print("averages of height by", average)

print('---------------------------------------------------------------------')


blood_type = df['bloodtype'].value_counts()
max=blood_type.max()
common_types=blood_type[blood_type == max].index.tolist()
print(df['bloodtype'].value_counts())
print(f"The most common blood type is: {common_types}")

print('---------------------------------------------------------------------')


df['height'] = df['height'] / 100
print(df)

print('---------------------------------------------------------------------')


sort = df.sort_values(by=['gender', 'bloodtype'])
print(sort)
#sort_df = df.sort_values(by=['gender', 'bloodtype'], ascending=[True, False]) #descending garna

print('---------------------------------------------------------------------')



pivot_table = df.pivot_table(index='gender', columns='bloodtype', values='height', aggfunc='count', fill_value=0)
#values='height' le specifiy garcha kun column aggregation garna...aile rows count garera which column doesnt matter
print(pivot_table)

print('---------------------------------------------------------------------')


df['BMI'] = df['weight'] / (df['height'] ** 2)
print(df)

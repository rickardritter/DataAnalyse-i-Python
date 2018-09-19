import pandas as pd

#Program som illustrerer priser paa bolig i Texax

df = pd.read_csv('ZILLOW-Z77006_ZRISFRR.csv')
print(df.head())

df.set_index('Date', inplace = True)

df.to_csv('newcsv2.csv')
df['Value'].to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df.columns = ['House_Prices']
print(df.head())

df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv', header=False)

df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'], index_col=0)
print(df.head())

df.to_html('example.html')


df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'])
print(df.head())

df.rename(columns={'House_Price':'Prices'}, inplace=True)
print(df.head())

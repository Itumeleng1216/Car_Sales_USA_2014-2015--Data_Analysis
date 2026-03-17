import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('car_prices.csv')  # Load the dataset

#Cleaning the dataset
print("Null counts before:", df.isnull().sum())
df = df.dropna()
print("Null counts after:", df.isnull().sum())

df.to_csv('cleaned_data.csv',index=False)

duplicates = df.duplicated().sum()
print(f"Number of duplicated rows: {duplicates}")
print(df[df.duplicated()])

df = pd.read_csv('cleaned_data_updated.csv')
df['saledate'] = df['saledate'].str.replace('(PDT)', '')
df.to_csv('cleaned_data_updated.csv',index=False)

df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce')

df['body'] = df['body'].replace(['regular-cab'], 'Regular Cab')

df.to_csv('cleaned_data_updated2.csv',index=False)
df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce')

#Xtracting year and month from saledate and calculating vehicle age and price difference

df['price_diff'] = df['sellingprice'] - df['mmr']

#Grouping car mileages into categories/groups
bins = [0, 20000, 50000, 100000, 150000, 200000, 300000]
labels = ['0-20k', '20k-50k', '50k-100k', '100k-150k', '150k-200k', '200k+']
df['odometer_group'] = pd.cut(df['odometer'], bins=bins, labels=labels)

#Grouping car conditions into categories/groups
df['condition_group'] = pd.cut(df['condition'],
                        bins = [0, 10, 20, 30, 40, 50],
                        labels = ['Very Bad', 'Bad', 'Average', 'Good', 'Excellent'])

df.to_csv('car_sales_clean.csv', index=False)

pd.read_csv('car_sales_clean.csv')
df['sale_year'] = df['saledate'].dt.year
df['sale_month'] = df['saledate'].dt.month
df['sale_month_name'] = df['saledate'].dt.month_name()
df['vehicle_age'] = df['sale_year'] - df['year']
df.to_csv('car_sales_final.csv', index=False)


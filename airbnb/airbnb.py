import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\IShop\Desktop\listings.csv')
df

df.shape
df.isna().sum()
df=df.drop(columns=['listing_url','scrape_id','description','neighborhood_overview','license','host_about','neighbourhood_group_cleansed','bathrooms','amenities','bedrooms'])
df

df.describe()

calc_host_list=df[['calculated_host_listings_count','calculated_host_listings_count_entire_homes','calculated_host_listings_count_private_rooms','calculated_host_listings_count_shared_rooms']]
sns.barplot(calc_host_list)
plt.title('host listings')
plt.xlabel('type of listing')
plt.ylabel('number of listing')
plt.xticks(rotation=90)
plt.show()



sns.scatterplot(x=df['latitude'],y=df['longitude'],hue=df['review_scores_location'],palette='coolwarm')
plt.show()


availability_data = df[['availability_30', 'availability_60', 'availability_90', 'availability_365']]
availability_data_melted = availability_data.melt(var_name='Availability Period', value_name='Number of Available Days')
plt.figure(figsize=(10, 6))
sns.barplot(data=availability_data_melted, x='Availability Period', y='Number of Available Days', ci=None)
plt.title('Availability Distribution for Different Time Periods')
plt.xlabel('Availability Period')
plt.ylabel('Number of Available Days')
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='property_type', order=df['property_type'].value_counts().index)
plt.title('Distribution of Property Types')
plt.xlabel('Property Type')
plt.ylabel('Count')
plt.xticks(rotation=90, ha='right') 
plt.tight_layout()  
plt.show()



fig, axes = plt.subplots(2, 1, figsize=(20, 15))
rev_by_property_type=df.groupby('property_type')['reviews_per_month'].mean().sort_values(ascending=False)
rev_by_location=df.groupby('neighbourhood')['reviews_per_month'].mean().sort_values(ascending=False)
sns.barplot(x=rev_by_property_type.values, y=price_by_property_type.index, ax=axes[0], palette='viridis')
axes[0].set_title('Average reviews_per_month by Property Type')
axes[0].set_xlabel('Average reviews_per_month (USD)')
axes[0].set_ylabel('Property Type')
sns.barplot(x=rev_by_location.values, y=price_by_location.index, ax=axes[1], palette='viridis')
axes[1].set_title('Average reviews_per_month by Neighborhood')
axes[1].set_xlabel('Average reviews_per_month (USD)')
axes[1].set_ylabel('Neighborhood')
plt.tight_layout()
plt.show()


import pandas as pd

# 1. Load the raw datasets
orders = pd.read_csv('olist_orders_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')
translation = pd.read_csv('product_category_name_translation.csv')

# 2. TRANSLATE PRODUCT CATEGORIES
# The raw product categories are in Portuguese. need to  merge them with the 
# translation table to add an English category column.

products_translation = pd.merge(

    products,
    translation,
    on ="product_category_name",
    how ="left"
)
# Dropping  the original Portuguese column to keep it clean

products_clean = products_translation.drop(columns=['product_category_name'])

# filling the other missing values 

# we have 3 datasets with missing values 
# olist_products_dataset (products_clean)
# olist_order_reviews_dataset (orders_review)
# olist_orders_dataset  (orders)

# Loading  the remaining datasets that contain null values

orders_review = pd.read_csv('olist_order_reviews_dataset.csv')

# filling the missing data for olist_products_dataset (products_clean)

find = products_clean.isnull().sum()
print(find)

# we dont have the products name but we do have products name length column 
# so filling the missign values with FILLL() method because we will get randome numbers + we dont have the 
# product name coolumn so it will not affect in future 

products_clean['product_name_lenght'] = products_clean['product_name_lenght'].ffill()

products_clean['product_description_lenght']=products_clean['product_description_lenght'].ffill()

# product_photos_qty is a column with rang of numbers from 1 - 4 
# so we can fill it with mean method
# if we use the column in future it will not affect the output

avg_value = products_clean['product_photos_qty'].mean()
round_avg = round(avg_value)
print(round_avg)

products_clean['product_photos_qty']= products_clean['product_photos_qty'].fillna(round_avg)

# filling the missing of the product_weight_g with median because this column contains outliers

mediun_finder = products_clean['product_weight_g'].median()
round_medium = round(mediun_finder)
print(round_medium)

products_clean['product_weight_g']=products_clean['product_weight_g'].fillna(round_medium)

# filling the missing of the product_length_cm with median because this column contains outliers

median_finder = products_clean['product_length_cm'].median()
round_M_finder = round(median_finder)
print(round_M_finder)

products_clean['product_length_cm'] = products_clean['product_length_cm'].fillna(round_M_finder)

# filling the missing of the product_height_cm with ffill() 

products_clean['product_height_cm']=products_clean['product_height_cm'].ffill()

# filling the missing of the product_width_cm with ffill() 

products_clean['product_width_cm']=products_clean['product_width_cm'].ffill()

date_column = ['review_creation_date','review_answer_timestamp']

for col in date_column:
    orders_review[col] = pd.to_datetime(orders_review[col])

    orders_review.loc[(orders_review['review_comment_title'].isna())&(orders_review['review_score']==1),'review_comment_title']= 'bad'
    orders_review.loc[(orders_review['review_comment_title'].isna())&(orders_review['review_score']==2),'review_comment_title'] = 'need improvement'
    orders_review.loc[(orders_review['review_comment_title'].isna())&(orders_review['review_score']==3),'review_comment_title'] ='good'
    orders_review.loc[(orders_review['review_comment_title'].isna())&(orders_review['review_score']==4),'review_comment_title'] = 'parfect'
    orders_review.loc[(orders_review['review_comment_title'].isna())&(orders_review['review_score']==5),'review_comment_title']= 'excelent'

    import numpy as np
orders_review['review_comment_message'] = orders_review['review_comment_message'].replace({np.nan: 'no message'})


# olist_orders_dataset  (orders)

 # When loaded from CSV, dates look like text strings. We convert them 
# to actual datetime objects so we can measure intervals later.

to_datetime = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date',
    
]

for col in to_datetime:
    orders[col]=pd.to_datetime(orders[col])

# in this orders datasets there are lots of missing values 
# but most of them are genuan missing 
# like the product is still in shipping canceld or in processing state 
# so missing data for that is mentioned as NAT (not a time)
# so except that missing values we will focus on the values that shows deliverd but missing with values 
# so i am going to use order state column to fill the other columns missing values 

# --- CRITICAL FIX 1: Fix delivered orders missing an approval timestamp ---
# Since they were delivered, they must have been approved. We proxy approval time using purchase time.

orders.loc[(orders['order_approved_at'].isna())& (orders['order_status']=='delivered'),'order_approved_at'] = orders['order_purchase_timestamp']

orders.loc[(orders['order_delivered_carrier_date'].isna())&(orders['order_status']=='delivered'),'order_delivered_carrier_date'] = orders['order_purchase_timestamp']

orders.loc[(orders['order_delivered_customer_date'].isna())&(orders['order_status']=='delivered'),'order_delivered_customer_date'] = orders['order_estimated_delivery_date']

#  EXPORT THE CLEANED FILES FOR SQL/BI

# olist_products_dataset (products_clean)
# olist_order_reviews_dataset (orders_review)
# olist_orders_dataset  (orders)

products_clean.to_csv('clean_products.csv', index=False)
orders_review.to_csv('cleaned_orders_review.csv', index=False)
orders.to_csv('cleaned_orders.csv', index=False)

df1 = pd.read_csv('olist_customers_dataset.csv')
df2 = pd.read_csv('olist_geolocation_dataset.csv')
df3 = pd.read_csv('olist_order_items_dataset.csv')
df4 = pd.read_csv('olist_order_payments_dataset.csv')
df5 = pd.read_csv('olist_sellers_dataset.csv')
df6 = pd.read_csv('product_category_name_translation.csv')
# olist_products_dataset (products_clean)
# olist_order_reviews_dataset (orders_review)
# olist_orders_dataset  (orders)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# DataFrame untuk visualisasi data
def create_order_by_cat_df(df):
    order_by_cat_df = df.groupby(by="product_category_name_english").order_id.nunique().reset_index().sort_values(by="order_id", ascending=False).head(10)
    order_by_cat_df.rename(columns={
        "order_id": "order_count",
        "product_category_name_english": "product_category"
    }, inplace=True)
    
    return order_by_cat_df

def create_sales_by_city_df(df):
    sales_by_city_df = df.groupby(by="customer_city").order_id.nunique().reset_index().sort_values(by="order_id", ascending=False).head(10)
    sales_by_city_df.rename(columns={
        "order_id": "order_count",
        "customer_city": "city"
    }, inplace=True)
    
    return sales_by_city_df

def create_payment_df(df):
    payment_df = df.groupby(by="payment_type").order_id.nunique().reset_index().sort_values(by="order_id", ascending=False)
    return payment_df

def create_review_score_df(df):
    review_df = df.groupby(by="review_score").order_id.nunique().reset_index()
    review_df.rename(columns={
        "order_id": "order_count",
        "review_score": "score"
    }, inplace=True)
    
    return review_df

# def create_rfm_df(df):
#     rfm_df = df.groupby(by="customer_id")

# Load main_data.csv
all_df = pd.read_csv("main_data.csv")

# Sidebar
with st.sidebar:
    # logo
    st.image("https://d3hw41hpah8tvx.cloudfront.net/images/logo_olist_d7309b5f20.png")

# Helper function
order_by_cat_df = create_order_by_cat_df(all_df)
sales_by_city_df = create_sales_by_city_df(all_df)
payment_df = create_payment_df(all_df)
review_score_df = create_review_score_df(all_df)

# Dashboard
st.header("Brazilian E-Commerce Public Dataset by Olist")

# Order by Top 10 Product Category
st.subheader("Order by Top 10 Product Category")
fig, ax = plt.subplots(figsize=(16, 8))
ax.bar(
    x = order_by_cat_df["product_category"],
    height = order_by_cat_df["order_count"],
    color = ["#0060DE", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
)
ax.tick_params(axis = "y", labelsize=20)
ax.tick_params(axis = "x", labelsize=16, rotation = 45)
st.pyplot(fig)

# Order by Top 10 City
st.subheader("Order by Top 10 City")
fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#0060DE", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
city = sales_by_city_df["city"].str.title() # agar kota jadi title case
sns.barplot(
    x = "order_count",
    y = city,
    data = sales_by_city_df.sort_values(by="order_count", ascending=False),
    palette = colors,
    ax = ax
)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

# Payment Type
st.subheader("Payment Type")
explode = (0.1, 0, 0, 0)
colors = ('#FF9100', '#E600FF', '#00E6FF', '#5EFF00')
fig, ax = plt.subplots(figsize=(10, 5))
ax.pie(
    x = payment_df['order_id'],
    labels = payment_df['payment_type'],
    autopct = '%1.1f%%',
    explode = explode,
    colors = colors,
    textprops={'fontsize': 10}
)
ax.axis('equal')
st.pyplot(fig)

# Review Score by Customer
st.subheader("Review Score by Customer")
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    review_score_df["score"],
    review_score_df["order_count"],
    marker = "o",
    color = "#0060DE"
)
ax.grid(True)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis = "x", rotation = 45)
st.pyplot(fig)

st.caption('Dicoding Data Scientist Project 2023')

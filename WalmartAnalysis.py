import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Header
st.set_page_config(page_title="Walmart Sales Report", page_icon="💼", layout="wide")

st.balloons()
st.title("Walmart Sales Analysis Report")
st.header("Appliances and Electronics Sales across Major US Cities")

# Company Logo
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRENYpBAINLaDDHo5VEv8-8MKyues1370ioeVzpzLVcZrRNY2epAuborGIAukhdHFN_ct4&usqp=CAU", width=200)

# Data Preparation
store_inventory = pd.DataFrame({
    "Store Location": ["Chicago, IL", "Dallas, TX", "Los Angeles, CA", "Miami, FL", "New York, NY"],
    "Total Inventory Price (USD Million)": [249333571.43, 253808834.6, 278224071.52, 249829554.61, 257512702.17],
    "Total Quantity Sold Worth (USD Million)": [3156726.82, 2903930.74, 3276299.63, 2962567.02, 2964077.24]
})

promotion_data = pd.DataFrame({
    "Promotion Type": ["BOGO", "None", "Percentage Discount"],
    "Quantity Sold": [2465, 10122, 2327],
    "Total Quantity Sold Worth (USD Million)": [1368661.84, 5454551.87, 1239197.32]
})

category_sales = pd.DataFrame({
    "Category": ["Appliances", "Electronics"],
    "Total Quantity Sold Worth (USD Million)": [7321969.65, 7941631.8]
})

payment_methods = pd.DataFrame({
    "Payment Method": ["Cash", "Credit Card", "Debit Card", "Digital Wallet"],
    "Total Quantity Sold Worth (USD Million)": [3816860.66, 3829054.57, 3652903.51, 3964782.71]
})

subcategory_sales = pd.DataFrame({
    "Product Name": ["Camera", "Fridge", "Headphones", "Laptop", "Smartphone", "Tablet", "TV", "Washing Machine"],
    "Total Quantity Sold Worth (USD Million)": [1895104.13, 1938012.69, 1846334.45, 1709159.24, 1931310.04, 1996253.02, 2049493.86, 1897934.02]
})

sentiment_analysis = pd.DataFrame({
    "Customer Gender": ["Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female",
                         "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male",
                         "Other", "Other", "Other", "Other", "Other", "Other", "Other", "Other"],
    "Product Name": ["Camera", "Fridge", "Headphones", "Laptop", "Smartphone", "Tablet", "TV", "Washing Machine",
                      "Camera", "Fridge", "Headphones", "Laptop", "Smartphone", "Tablet", "TV", "Washing Machine",
                      "Camera", "Fridge", "Headphones", "Laptop", "Smartphone", "Tablet", "TV", "Washing Machine"],
    "Quantity Sold": [556, 639, 601, 572, 657, 731, 641, 615,
                       660, 686, 620, 498, 628, 600, 676, 581,
                       657, 642, 595, 615, 591, 633, 609, 611]
})

# Total Inventory and Demand Data
inventory_level = 1265609
forecast_demand = 1485670
actual_demand = 1495442

# Key Metrics Section
st.subheader("Key Metrics Overview")
st.markdown("""
In this section, we present key metrics for Walmart's performance, including total inventory levels, forecasted demand, and actual demand. These metrics are essential to understanding the alignment of inventory with customer demand, providing insights into stock management and sales optimization. 

- **Total Inventory Level**: The inventory across the five stores analyzed amounts to over 1.2 million units, which indicates that Walmart has significant resources stocked.
- **Forecasted Demand**: The forecast predicts a total demand of approximately 1.5 million units, highlighting expected consumer purchases.
- **Actual Demand**: In comparison, the actual demand slightly exceeds the forecast, totaling around 1.5 million units. This small variance shows that Walmart's forecasting model is fairly accurate.
""")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Inventory Level", value=f"{inventory_level:,}")
with col2:
    st.metric(label="Forecasted Demand", value=f"{forecast_demand:,}")
with col3:
    st.metric(label="Actual Demand", value=f"{actual_demand:,}")

# Store Analysis
st.subheader("Store Performance Analysis")
st.markdown("""
The following table displays the total inventory price and quantity sold worth across Walmart stores located in major cities: Chicago, Dallas, Los Angeles, Miami, and New York. Analyzing this data allows us to compare how each store is performing in terms of sales, identifying the most successful locations and the impact of inventory management.

From the data, **Los Angeles, CA** shows the highest total sales value at approximately $3.3 billion, which may reflect both a larger customer base and possibly higher product demand compared to other cities like Miami and Chicago, which exhibit lower total sales figures.
""")
st.dataframe(store_inventory.style.format({
    "Total Inventory Price (USD Million)": "${:,.2f}",
    "Total Quantity Sold Worth (USD Million)": "${:,.2f}"
}))

store_chart = px.bar(
    store_inventory,
    x="Store Location",
    y="Total Quantity Sold Worth (USD Million)",
    title="Store Sales Comparison",
    color="Store Location",
    labels={"Total Quantity Sold Worth (USD Million)": "Sales (USD Million)"}
)
st.plotly_chart(store_chart)

# Promotion Analysis
st.subheader("Promotion Performance Analysis")
st.markdown("""
In this section, we analyze the impact of different promotion types on sales. The promotions considered are Buy One Get One (BOGO), no promotion, and percentage discounts. 

It is evident that **percentage discounts** have the highest total sales worth, contributing significantly to the overall revenue. Promotions like BOGO also show a strong effect, contributing over $1.3 billion in sales. This analysis suggests that introducing strategic promotions could drive further sales, especially in underperforming stores.
""")
st.dataframe(promotion_data.style.format({
    "Total Quantity Sold Worth (USD Million)": "${:,.2f}"
}))

promotion_chart = px.pie(
    promotion_data,
    names="Promotion Type",
    values="Total Quantity Sold Worth (USD Million)",
    title="Sales by Promotion Type",
    hole=0.4
)
st.plotly_chart(promotion_chart)

# Category Sales Analysis
st.subheader("Category-wise Sales Performance")
st.markdown("""
The sales breakdown between Appliances and Electronics shows that **Electronics** take the lead in terms of sales, contributing approximately $7.9 billion, compared to $7.3 billion for Appliances. Understanding the split between these categories helps Walmart optimize its marketing efforts and inventory management, potentially focusing more on electronics as a higher-selling category.
""")
st.dataframe(category_sales.style.format({
    "Total Quantity Sold Worth (USD Million)": "${:,.2f}"
}))

category_chart = px.bar(
    category_sales,
    x="Category",
    y="Total Quantity Sold Worth (USD Million)",
    title="Sales by Category",
    color="Category",
    labels={"Total Quantity Sold Worth (USD Million)": "Sales (USD Million)"}
)
st.plotly_chart(category_chart)

# Payment Methods Analysis
st.subheader("Sales by Payment Method")
st.markdown("""
Examining the payment methods used by customers provides insights into the preferred options for transactions. The analysis reveals that **Digital Wallets** and **Credit Cards** dominate the payment landscape, reflecting the ongoing shift toward digital and contactless payments. Walmart can use this data to further promote digital payment options and ensure seamless transactions for customers.
""")
st.dataframe(payment_methods.style.format({
    "Total Quantity Sold Worth (USD Million)": "${:,.2f}"
}))

payment_chart = px.pie(
    payment_methods,
    names="Payment Method",
    values="Total Quantity Sold Worth (USD Million)",
    title="Sales by Payment Method",
    hole=0.4
)
st.plotly_chart(payment_chart)

# Subcategory Sales Analysis
st.subheader("Sales by Product Subcategory")
st.markdown("""
In this section, we analyze the performance of individual product subcategories. Products like **TVs**, **Smartphones**, and **Tablets** lead the sales charts, with TVs generating over $2 billion in sales alone. Identifying top-selling products helps Walmart focus its inventory management and promotional efforts to meet consumer demand.
""")
st.dataframe(subcategory_sales.style.format({
    "Total Quantity Sold Worth (USD Million)": "${:,.2f}"
}))

subcategory_chart = px.bar(
    subcategory_sales,
    x="Product Name",
    y="Total Quantity Sold Worth (USD Million)",
    title="Sales by Product Subcategory",
    color="Product Name",
    labels={"Total Quantity Sold Worth (USD Million)": "Sales (USD Million)"}
)
st.plotly_chart(subcategory_chart)

# Sentiment Analysis by Gender
st.subheader("Gender-wise Purchasing Trends")
st.markdown("""
By analyzing sales based on customer gender, we gain valuable insights into purchasing patterns. For instance, **females** tend to purchase more **Tablets** and **TVs**, while **males** show higher purchasing behavior for products like **Cameras** and **TVs**. Tailoring marketing and promotional strategies to these preferences can enhance sales and customer satisfaction.
""")
st.dataframe(sentiment_analysis.style.format({
    "Quantity Sold": "{:,}"
}))

gender_chart = px.bar(
    sentiment_analysis,
    x="Product Name",
    y="Quantity Sold",
    color="Customer Gender",
    barmode="group",
    title="Gender-wise Sales by Product",
    labels={"Quantity Sold": "Quantity Sold"}
)
st.plotly_chart(gender_chart)

# Conclusion and Strategy
st.subheader("Conclusion and Strategic Recommendations")
st.markdown("""
Based on the analysis, we propose the following strategies to increase Walmart's sales performance:

- **Expand Promotions**: Focus on increasing percentage discounts and BOGO offers in underperforming stores.
- **Optimize Inventory**: Ensure high-demand products like TVs and Tablets are stocked adequately across all stores.
- **Enhance Digital Payments**: Promote digital wallet options to cater to modern payment preferences, especially among younger consumers.
- **Targeted Marketing**: Use city-specific insights to create localized campaigns for cities like Miami and Dallas, where product demand may differ.
- **Tailored Strategies by Gender**: Focus on promoting categories popular among specific genders. For example, increase promotions on Tablets and TVs for females and on Cameras and TVs for males.
""")

import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Header
st.set_page_config(page_title="Walmart Sales Report", page_icon="💼", layout="wide")
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
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Inventory Level", value=f"{inventory_level:,}")
with col2:
    st.metric(label="Forecasted Demand", value=f"{forecast_demand:,}")
with col3:
    st.metric(label="Actual Demand", value=f"{actual_demand:,}")

# Store Analysis
st.subheader("Store Performance")
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
st.subheader("Promotion Performance")
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
st.subheader("Category Sales")
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
st.subheader("Payment Methods")
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
st.subheader("Subcategory Sales")
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
st.subheader("Conclusion and Strategy")
st.markdown("""
- **Expand Promotions**: Focus on increasing percentage discounts and BOGO offers in underperforming stores.
- **Optimize Inventory**: Ensure high-demand products like TVs and Tablets are stocked adequately.
- **Enhance Digital Payments**: Highlight digital wallet options to cater to modern payment preferences.
- **Targeted Marketing**: Leverage city-specific insights to create localized campaigns for Miami and Dallas.
- **Tailored Strategies by Gender**: Focus on promoting categories popular among specific genders. For example, increase promotions on Tablets and TVs for females and on Cameras and TVs for males.
""")

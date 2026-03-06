import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("Online Retail.xlsx")

#Show first 5 rows

print(df.head())

#Show dataset rows and columns

print("ShapeeE:", df.shape)

# Show column names

print("Columns:", df.columns)

# Show null values

print("\nMissing Values:")
print("True:", df.isnull().sum())


#Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Sales column

df["Sales"] = df["Quantity"] * df["UnitPrice"]

print(df[["InvoiceDate", "Quantity", "UnitPrice", "Sales"]].head())

#Remove returns and invalid values

df_clean = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

print("Cleaned:", df_clean)


#Top 10 products by total sales

top_products = (
    df_clean.groupby("Description")["Sales"].sum().sort_values(ascending=False).head(10)
)

print("\nTop 10 Products by Revenue:")
print(top_products)

#Show monthly sales
# Create Year-Month column
df_clean["YearMonth"] = df_clean["InvoiceDate"].dt.to_period("M")

monthly_sales = (
    df_clean.groupby("YearMonth")["Sales"].sum().sort_values(ascending=False).head(10)
)

print("\nMonthly Sales:")
print(monthly_sales)

# Plot
plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Sales by Country

country_sales = (
    df_clean.groupby("Country")["Sales"].sum().sort_values(ascending=False).head(10)
)

print("\nTop 10 Countries by Revenue:")
print(country_sales)

# Plot
plt.figure(figsize=(12,6))
country_sales.plot(kind="bar")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Top Customers by Revenue

customer_sales = (
    df_clean.groupby("CustomerID")["Sales"].sum().sort_values(ascending=False).head(10)
)

print("\nTop 10 Customers by Revenue:")
print(customer_sales)

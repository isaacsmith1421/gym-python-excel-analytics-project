import pandas as pd


file_path = "gym_raw_data.xlsx"

products = pd.read_excel(file_path, sheet_name="Products")
sales = pd.read_excel(file_path, sheet_name="Sales")
checkins = pd.read_excel(file_path, sheet_name="CheckIns")
classes = pd.read_excel(file_path, sheet_name="Classes")
class_attendance = pd.read_excel(file_path, sheet_name="ClassAttendance")

for df in [products, sales, checkins, classes, class_attendance]:
    df.columns = df.columns.str.strip()

print("=== Loaded sheets successfully ===")
print("Products:", products.shape)
print("Sales:", sales.shape)
print("Check-ins:", checkins.shape)
print("Classes:", classes.shape)
print("Class Attendance:", class_attendance.shape)

if "SaleDateTime" in sales.columns:
    sales["SaleDateTime"] = pd.to_datetime(
        sales["SaleDateTime"], errors="coerce"
    )
    print("\nConverted Sales 'SaleDateTime' to datetime.")
else:
    print("\nWARNING: 'SaleDateTime' column not found in Sales sheet.")

checkin_dt_cols = [
    c for c in checkins.columns
    if "date" in c.lower() or "time" in c.lower()
]

if checkin_dt_cols:
    checkin_dt_col = checkin_dt_cols[0]
    checkins[checkin_dt_col] = pd.to_datetime(
        checkins[checkin_dt_col], errors="coerce"
    )
    print(f"Converted CheckIns datetime column: {checkin_dt_col}")
else:
    print("WARNING: No date/time column found in CheckIns sheet.")

if "SessionDate" in class_attendance.columns:
    class_attendance["SessionDate"] = pd.to_datetime(
        class_attendance["SessionDate"], errors="coerce"
    )
    print("Converted ClassAttendance 'SessionDate' to datetime.")
else:
    print("WARNING: 'SessionDate' column not found in ClassAttendance sheet.")

print("\n=== Sample Sales rows ===")
print(sales.head())

sales_with_products = sales.merge(
    products[["ProductID", "ProductName", "Category"]],
    on="ProductID",
    how="left",
)

print("\nMerged sales_with_products columns:")
print(sales_with_products.columns.tolist())


sales_with_products["Revenue"] = (
    sales_with_products["Quantity"] * sales_with_products["UnitPrice"]
)

print("\nAdded 'Revenue' column.")
print(sales_with_products[["SaleID", "ProductID", "Quantity",
                           "UnitPrice", "Revenue"]].head())


if "SaleDateTime" in sales_with_products.columns:
    sales_with_products["YearMonth"] = (
        sales_with_products["SaleDateTime"]
        .dt.to_period("M")
        .astype(str)
    )
else:
    sales_with_products["YearMonth"] = "Unknown"


revenue_by_product = (
    sales_with_products
    .groupby("ProductName", as_index=False)
    .agg(
        TotalRevenue=("Revenue", "sum"),
        UnitsSold=("Quantity", "sum"),
    )
    .sort_values("TotalRevenue", ascending=False)
)

print("\n=== Revenue by product ===")
print(revenue_by_product)


revenue_by_category = (
    sales_with_products
    .groupby("Category", as_index=False)
    .agg(
        TotalRevenue=("Revenue", "sum"),
        UnitsSold=("Quantity", "sum"),
    )
    .sort_values("TotalRevenue", ascending=False)
)

print("\n=== Revenue by category ===")
print(revenue_by_category)


monthly_revenue_by_category = (
    sales_with_products
    .groupby(["YearMonth", "Category"], as_index=False)
    .agg(
        TotalRevenue=("Revenue", "sum"),
        UnitsSold=("Quantity", "sum"),
    )
    .sort_values(["YearMonth", "TotalRevenue"], ascending=[True, False])
)

print("\n=== Monthly revenue by category ===")
print(monthly_revenue_by_category)


monthly_totals = (
    monthly_revenue_by_category
    .groupby("YearMonth", as_index=False)
    .agg(TotalRevenue=("TotalRevenue", "sum"))
)

print("\n=== Total revenue by month ===")
print(monthly_totals)

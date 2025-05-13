import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Step 1: Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="ISO-8859-1")

# Step 2: Clean and prepare data
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Step 3: Setup PDF export
pdf = PdfPages("Superstore_Visual_Storytelling_Report.pdf")
sns.set(style="whitegrid")

# --- Chart 1: Monthly Sales and Profit Trend ---
monthly = df.resample('M', on='Order Date')[['Sales', 'Profit']].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly, x='Order Date', y='Sales', label='Sales')
sns.lineplot(data=monthly, x='Order Date', y='Profit', label='Profit')
plt.title('Monthly Sales and Profit Trend')
plt.xlabel('Order Date')
plt.ylabel('Amount ($)')
plt.xticks(rotation=45)
plt.legend()
pdf.savefig()
plt.close()

# --- Chart 2: Sales by Category and Sub-Category ---
plt.figure(figsize=(14, 6))
cat_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().sort_values()
cat_sales.plot(kind='barh', color='skyblue')
plt.title('Sales by Category and Sub-Category')
plt.xlabel('Sales ($)')
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Chart 3: Regional Sales and Profit ---
region_data = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values('Sales', ascending=False)
region_data.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Regional Sales and Profit')
plt.ylabel('Amount ($)')
plt.xticks(rotation=0)
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Chart 4: Discount vs Profit Scatter Plot ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', alpha=0.6)
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.axhline(0, color='red', linestyle='--')
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Chart 5: Segment-wise Sales and Profit ---
segment_data = df.groupby('Segment')[['Sales', 'Profit']].sum()
segment_data.plot(kind='bar', color=['#1f77b4', '#ff7f0e'], figsize=(10, 6))
plt.title('Sales and Profit by Customer Segment')
plt.ylabel('Amount ($)')
plt.xticks(rotation=0)
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Summary Slide / Storyboard ---
plt.figure(figsize=(10, 6))
plt.axis('off')
plt.title("📊 Business Insights Summary", fontsize=16, weight='bold')
plt.text(0.05, 0.85, "1. 📈 Technology has the highest sales, but Furniture yields better profit.", fontsize=12)
plt.text(0.05, 0.75, "2. 🌎 West region is most profitable; Central struggles with low profit margins.", fontsize=12)
plt.text(0.05, 0.65, "3. 💸 High discounts negatively impact profit—especially in Furniture.", fontsize=12)
plt.text(0.05, 0.55, "4. 👥 Consumer segment drives the highest sales.", fontsize=12)
plt.text(0.05, 0.45, "5. ⏱️ Profitability shows seasonal spikes—plan promotions accordingly.", fontsize=12)
pdf.savefig()
plt.close()

# Save the PDF
pdf.close()

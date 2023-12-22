import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# Set a seed for reproducibility
np.random.seed(42)
# Create a dummy dataset
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
products = ['Running Shoes', 'Casual Sneakers', 'Basketball Shoes']
promotions = ['No Promotion', 'Discount', 'Buy One Get One Free']
sales_data = []
for date in date_range:
    for product in products:
        sales = np.random.randint(50, 500)
        promotion = np.random.choice(promotions)
        sales_data.append({
            'Date': date,
            'Product': product,
            'Promotion': promotion,
            'Sales': sales
        })
sales_df = pd.DataFrame(sales_data)
# Save the dummy data to an Excel file
file_path = 'dummy_sales_data.xlsx'
sales_df.to_excel(file_path, index=False)
# Open the file using the default application
try:
    os.system(f'start excel "{file_path}"')  # For Windows
except:
    try:
        os.system(f'open -a "Microsoft Excel" "{file_path}"')  # For MacOS
    except:
        print(f'Please open the file manually: {file_path}')
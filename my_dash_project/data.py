import pandas as pd

data0 = pd.read_csv('data/daily_sales_data_0.csv')
data1 = pd.read_csv('data/daily_sales_data_1.csv')
data2 = pd.read_csv('data/daily_sales_data_2.csv')

sales_data = pd.concat([data0, data1, data2], ignore_index=True)

pink_morsels_data = sales_data[sales_data['product'] == 'pink morsel'].copy()

pink_morsels_data['price'] = pink_morsels_data['price'].replace(r'[\$,]', '', regex=True).astype(float)
sales = pink_morsels_data['price'] * pink_morsels_data['quantity']

data = {
    "Sales": sales,
    "date": pink_morsels_data['date'],
    "region": pink_morsels_data['region']
}

df = pd.DataFrame(data)
df.to_csv("data/pink_morsels_data.csv", index=False)
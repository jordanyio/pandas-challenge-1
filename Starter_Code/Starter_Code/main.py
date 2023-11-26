import pandas as pd

df = pd.read_csv('Resources/client_dataset.csv')

df.head()

df.columns

df.describe()

mean_cost = df["unit_cost"].mean()
mean_price = df["unit_price"].mean()
mean_weight = df["unit_weight"].mean()

num_floating_points = 4
print(f'The mean cost is ${round(mean_cost, num_floating_points)}, the mean price is ${round(mean_price, num_floating_points)}, the mean weight is {round(mean_weight, num_floating_points)} lbs')

df_test = df["category"].value_counts()
df_test.head(3)

df_test = df[["category","subcategory"]].value_counts().head(1)
df_test

df_test = df[["client_id", "first", "last"]].value_counts()
df_test.head(5)

df_series = df["client_id"].value_counts().head(5)
list = df_series.index.to_list()
list

my_value = list[0]
results = df.loc[df["client_id"] == my_value]

results["qty"].sum()

client_1 = 33615
client_2 = 66037


df['line_subtotal'] = df['unit_price'] * df['qty']
result_df = df.groupby('client_id')[['line_subtotal', 'unit_price', 'qty']].sum().reset_index()

#result = result_df[result_df['client_id'].isin([client_1, client_2])]
result = result_df[(result_df['client_id'] == client_1) | (result_df['client_id'] == client_2)]
result

df['shipping_price'] = df.apply(lambda row: row['unit_weight'] * 7 if row['unit_weight'] > 50 else row['unit_weight'] * 10, axis=1)
df

df['total_price'] = (df['line_subtotal'] + df['shipping_price']) * 1.0925
df

df['line_cost'] = ((df['unit_cost']  + df['shipping_price']) * df['qty']) 

df['line_profit'] = df['total_price'] - df['line_cost']
df

order_num1 = 2742071
order_num2 = 2173913
order_num3 = 6128929

order_num1_total = df.loc[df['order_id'] == order_num1, "total_price"].sum()
order_num2_total = df.loc[df['order_id'] == order_num2, "total_price"].sum()
order_num3_total = df.loc[df['order_id'] == order_num3, "total_price"].sum()

print(f"Order {order_num1} total: ${order_num1_total:.2f}")
print(f"Order {order_num2} total: ${order_num2_total:.2f}")
print(f"Order {order_num3} total: ${order_num3_total:.2f}")


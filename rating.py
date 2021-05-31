import pandas as pd

df = pd.read_csv("mobil_telefoner.csv")
filtered_df = df[df["product_price"] > 1000]

filename = "rating.csv"
headers = "product_name,product_rating,product_price\n"
f = open(filename, "w")
f.write(headers)

for index, item in enumerate(filtered_df.values):
    if index > 1:
        name = item[0]
        rating = (float(item[1]) + float(item[2]) + float(item[3]) + float(item[4]) + float(item[5])) / 5
        price = float(item[6])
        f.write(str(name) + "," + str(rating) + "," + str(price) + "\n") 

f.close()
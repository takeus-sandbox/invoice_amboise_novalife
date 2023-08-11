import csv, os
import pandas as pd
import data

data.items_table = []

print("Atlas Transport Calculator")

while True:
    user_input = input("Add Item (y/n) ")
    if user_input.lower() == "y":
        
        item_id = input("Item ID = ")
        item_qa = input("Quantity = ")
        data.items_table.append((item_id,item_qa))

    else:
        print(data.items_table)
        break

total = 0
for item in data.items_table:
    total += int(data.items[int(item[0])][1]) * int(item[1])
print(total)

with open("articles.csv", "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["article", "quantite", "prix unitaire", "prix"])

    for item in data.items_table:
        writer.writerow([
                data.items[int(item[0])][0],
                int(item[1]),
                data.items[int(item[0])][1],
                int(data.items[int(item[0])][1]) * int(item[1])
            ])
    writer.writerow(["",""])
    writer.writerow(["Total", total])

try: 
    os.remove("articles.xlsx")
except:
    pass

df = pd.read_csv("articles.csv")
df.columns = ["article", "quantité", "prix unitaire", "prix"]
df.to_excel("articles.xlsx", index=False)

try: 
    os.remove("articles.csv")
except:
    pass
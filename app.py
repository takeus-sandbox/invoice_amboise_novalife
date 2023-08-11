import csv, os
import pandas as pd
import data

items_table = [] # Tuple with ID & Quantity

os.system('cls')
print("""====
Atlas Transport Calculator
Version : V1.1
Dev & Support : Jack Pack (Livreur)
====
""")

while True:
    user_input = input("Add Item (y/n) ")
    if user_input.lower() == "y":
        
        item_id = input("Item ID = ")
        item_qa = input("Quantity = ")
        items_table.append((item_id,item_qa))

    else:
        #print(items_table)
        break

## Total Calculation
total_price = 0
total_quantity = 0

for item in items_table:
    total_price += int(data.items[int(item[0])][1]) * int(item[1])
    total_quantity += int(item[1])

#print(total_price)
#print(total_quantity)
#print(total_quantity/float(data.item_stack),"/",int(data.storage_total))

## CSV Creation
with open("invoice.csv", "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["Article", "Amount", "Unit Price", "Total"])

    for item in items_table:
        writer.writerow([
                data.items[int(item[0])][0],
                int(item[1]),
                data.items[int(item[0])][1],
                int(data.items[int(item[0])][1]) * int(item[1])
        ])
    writer.writerow([""])
    writer.writerow(["Total",total_quantity,"", total_price])
    writer.writerow([""])
    writer.writerow([""])
    writer.writerow(["Items Stack", (total_quantity/int(data.item_stack))])
    writer.writerow(["Transport", (total_quantity/int(data.item_stack))/data.storage_total])

## Excel Conversion
try: 
    os.remove("invoice.xlsx")
except:
    pass

df = pd.read_csv("invoice.csv")
df.columns = ["Article", "Amount", "Unit Price", "Total"]

df.to_excel("invoice.xlsx", index=False)

try: 
    os.remove("invoice.csv")
except:
    pass
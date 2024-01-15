import pytest
import datetime
import csv
from functions import *
from rich.console import Console
import argparse


# Terminal invoer voor pytest: 
"$ python -m pytest"
"18,Grapes,200,14-01-2024,1.5,22-01-2024"

article_id = 1
prijs = 12.00
aantal = 10

print(type(article_id))
print(type(prijs))
print(type(aantal))
# id;product_name;quantity;sales_price;expiration_date


"""def sell_article():
    sales_append = {}
    # Lezen van de CSV
    with open('inventory.csv', mode='r+', newline='') as file:
        reader = csv.DictReader(file, delimiter=",")
        rows = list(reader)

    # Aanpassen id,product_name,quantity,buy_price,sales_price,expiration_date
        for row in rows:
            if row["id"] == str(article_id):
                if int(row["quantity"]) > aantal:
                    row["quantity"] = int(row['quantity']) - aantal
                    print(f"You've sold {aantal} {row["product_name"]}")
                    sales_append = {"id": row["id"],
                                    "product_name": row["product_name"],
                                    "quantity": aantal,
                                    "buy_price": row["buy_price"],
                                    "sales_price": prijs,
                                    "sale_date": today_formatted,
                                    "expiration_date": row["expiration_date"]}
                break

            if aantal >= int(row['quantity']):
                print(f"You've sold the last amount of {row['product_name']}: {row['quantity']}")
                sales_append = {"id": row["id"],
                                "product_name": row["product_name"],
                                "quantity": row['quantity'],
                                "buy_price": row["buy_price"],
                                "sales_price": prijs,
                                "sale_date": today_formatted,
                                "expiration_date": row["expiration_date"]}
                rows.remove(row)
                break

            else:
                print(f"The item you want to sell is not in stock!")
                break  

        file.seek(0)
        file.truncate()

        writer = csv.DictWriter(file, fieldnames= reader.fieldnames, delimiter=",")
        writer.writeheader()
        writer.writerows(rows)

        if sales_append != {}:
            with open("sales.csv", mode="a", newline="") as output:
                writer = csv.DictWriter(output, fieldnames = ["id","product_name",
                                                          "quantity","buy_price",
                                                          "sales_price","sale_date",
                                                          "expiration_date"], delimiter=",")
                writer.writerow(sales_append)
    
    return"""


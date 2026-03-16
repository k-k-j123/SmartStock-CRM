import requests
import random
from faker import Faker
import time

fake = Faker()

BASE = "http://localhost:8080/api"

customers = []
products = []

# -------------------
# CREATE CUSTOMERS
# -------------------
def seed_customers(n=50):

    for _ in range(n):

        phone = fake.msisdn()[0:10]

        data = {
            "name": fake.name(),
            "phone": phone,
            "email": fake.email()
        }

        requests.post(f"{BASE}/customer", json=data)

        customers.append(phone)

    print("Customers created:", len(customers))


# -------------------
# CREATE PRODUCTS
# -------------------
def seed_products(n=40):

    product_catalog = {
        "Electronics": [
            "Smartphone",
            "Bluetooth Speaker",
            "Laptop Charger",
            "Power Bank",
            "USB Cable",
            "LED Monitor",
            "Wireless Mouse",
            "Wireless Keyboard"
        ],

        "Grocery": [
            "Basmati Rice",
            "Cooking Oil",
            "Sugar",
            "Salt",
            "Green Tea",
            "Instant Noodles",
            "Coffee Powder",
            "Milk Powder"
        ],

        "Stationery": [
            "Ball Pen",
            "Notebook",
            "Highlighter",
            "Marker Pen",
            "A4 Paper Pack",
            "Sticky Notes",
            "Stapler",
            "Correction Pen"
        ],

        "Peripherals": [
            "Gaming Mouse",
            "Mechanical Keyboard",
            "USB Hub",
            "External Hard Drive",
            "Webcam",
            "Laptop Stand",
            "Cooling Pad",
            "HDMI Cable"
        ]
    }

    for _ in range(n):

        category = random.choice(list(product_catalog.keys()))
        name = random.choice(product_catalog[category])

        cost = random.randint(10, 200)

        data = {
            "name": name,
            "category": category,
            "costPrice": cost,
            "sellingPrice": cost + random.randint(5, 80),
            "stockQuantity": random.randint(50, 200),
            "lowStockThreshold": 10
        }

        r = requests.post(f"{BASE}/product", json=data)

        if r.status_code == 200:
            products.append(r.json()["id"])

    print("Products created:", len(products))
# -------------------
# SIMULATE SALES
# -------------------
def simulate_sales(n=200):

    for _ in range(n):

        items = []

        for _ in range(random.randint(1,3)):

            items.append({
                "productId": random.choice(products),
                "quantity": random.randint(1,5)
            })

        data = {
            "customerPhone": random.choice(customers),
            "items": items
        }

        requests.post(f"{BASE}/sales", json=data)

        time.sleep(0.2)

    print("Sales created:", n)


# -------------------
# MAIN
# -------------------
if __name__ == "__main__":

    seed_customers(30)
    seed_products(20)

    simulate_sales(300)

    print("Simulation finished")
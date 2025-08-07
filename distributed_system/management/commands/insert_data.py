from django.core.management.base import BaseCommand
from distributed_system.models import User, Product, Order
from django.db import transaction
import threading

class Command(BaseCommand):
    help = "Insert data concurrently into multiple databases"

    def handle(self, *args, **kwargs):
        users_data = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
            {"name": "Charlie", "email": "charlie@example.com"},
            {"name": "David", "email": "david@example.com"},
            {"name": "Eve", "email": "eve@example.com"},
            {"name": "Frank", "email": "frank@example.com"},
            {"name": "Grace", "email": "grace@example.com"},
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Henry", "email": "henry@example.com"},
            {"name": "Jane", "email": "jane@example.com"},
        ]

        products_data = [
            {"name": "Laptop", "price": 1000.00},
            {"name": "Smartphone", "price": 700.00},
            {"name": "Headphones", "price": 150.00},
            {"name": "Monitor", "price": 300.00},
            {"name": "Keyboard", "price": 50.00},
            {"name": "Mouse", "price": 30.00},
            {"name": "Laptop", "price": 1000.00},
            {"name": "Smartwatch", "price": 250.00},
            {"name": "Gaming Chair", "price": 500.00},
            {"name": "Earbuds", "price": -50.00},
        ]

        orders_data = [
            {"user_id": 1, "product_id": 1, "quantity": 2},
            {"user_id": 2, "product_id": 2, "quantity": 1},
            {"user_id": 3, "product_id": 3, "quantity": 5},
            {"user_id": 4, "product_id": 4, "quantity": 1},
            {"user_id": 5, "product_id": 5, "quantity": 3},
            {"user_id": 6, "product_id": 6, "quantity": 4},
            {"user_id": 7, "product_id": 7, "quantity": 2},
            {"user_id": 8, "product_id": 8, "quantity": 0},
            {"user_id": 9, "product_id": 1, "quantity": -1},
            {"user_id": 10, "product_id": 11, "quantity": 2},
        ]

        def insert_users():
            for u in users_data:
                try:
                    if not u.get("name") or not u.get("email"):
                        raise ValueError("Invalid user data")
                    User.objects.using("users_db").create(**u)
                except Exception as e:
                    print(f"User insert error: {u} -> {e}")

        def insert_products():
            for p in products_data:
                try:
                    if p["price"] <= 0:
                        raise ValueError("Invalid price")
                    Product.objects.using("products_db").create(**p)
                except Exception as e:
                    print(f"Product insert error: {p} -> {e}")

        def insert_orders():
            for o in orders_data:
                try:
                    if o["quantity"] <= 0:
                        raise ValueError("Invalid quantity")
                    Order.objects.using("orders_db").create(**o)
                except Exception as e:
                    print(f"Order insert error: {o} -> {e}")

        threads = [
            threading.Thread(target=insert_users),
            threading.Thread(target=insert_products),
            threading.Thread(target=insert_orders),
        ]

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print("✅ Insertions completed.")


🧪 Distributed System Simulation (Django Assessment)
This project demonstrates a simple simulation of a distributed system using Django where three types of data — Users, Products, and Orders — are stored in separate SQLite databases. The insertion of records into each database is done concurrently using threads to simulate real-world distributed data operations.

📦 Features
Separate SQLite databases for:

Users → users.db

Products → products.db

Orders → orders.db

Concurrency using Python's threading module to simulate simultaneous inserts.

Application-level validation (e.g., price > 0, quantity > 0, name/email present).

One simple management command to run the entire simulation.

Clear logging of successful and failed inserts.

📁 Models
Model	Fields	Database
Users	id, name, email	users.db
Products	id, name, price	products.db
Orders	id, user_id, product_id, quantity	orders.db

⚙️ How to Run
Install requirements and setup Django environment.

Apply migrations to each individual database:


python manage.py migrate --database=users_db
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db
Run the command to insert records concurrently:


python manage.py insert_data
🧾 Sample Output

✅ Inserted user: {'name': 'Alice', 'email': 'alice@example.com'}
❌ Product insert error: {'name': 'Earbuds', 'price': -50.0} -> Invalid price
❌ Order insert error: {'user_id': 8, 'product_id': 8, 'quantity': 0} -> Invalid quantity
✅ All insertions attempted.

📝 Notes
No authentication or API endpoints are used — everything runs through a management command.

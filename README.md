# 🛒 Shop Management System (SQLAlchemy + SQLite)

##  Overview

This project is a simple database system built using Python and SQLAlchemy ORM.
It models a shop where users can place orders for products.

---

##  Technologies Used

* Python
* SQLAlchemy (ORM)
* SQLite

---

##  Database Structure

###  User

* id (Primary Key)
* name
* email (unique)

###  Product

* id (Primary Key)
* name
* price

###  Order

* id (Primary Key)
* user_id (Foreign Key → User)
* product_id (Foreign Key → Product)
* quantity
* status (Boolean → shipped or not)

---

##  Relationships

* One User → Many Orders
* One Product → Many Orders
* Each Order belongs to one User and one Product

---

##  Features

* Create database using SQLite
* Define tables using SQLAlchemy ORM
* Insert sample data (User, Product, Order)
* Query all **not shipped orders**
* Count total number of orders per user

---

## ▶ How to Run

1. Install dependencies:

```
pip install sqlalchemy
```

2. Run the script:

```
python RelationalDB-Python.py
```

3. The database file `shop.db` will be created automatically.

---

##  Example Output

```
--- Not Shipped Orders ---
Order 1 is NOT shipped

--- Orders Per User ---
Yousef has 2 orders
```

---

## 🎥 Presentation Notes

* Explain the purpose of the system
* Describe the database tables and relationships
* Show how data is inserted
* Demonstrate queries and results

---

## 👤 Author

GitHub: https://github.com/AbdelrahmanYousef9266/

from sqlalchemy import create_engine, String, ForeignKey, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, relationship

engine = create_engine("sqlite:///shop.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    orders: Mapped[list["Order"]] = relationship(back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)

    order_items: Mapped[list["Order"]] = relationship(back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["User"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship(back_populates="order_items")


Base.metadata.create_all(engine)


# inserting data
user1 = User(name="Yousef", email="Yousef@test.com")
product1 = Product(name="Laptop", price=1000)

session.add_all([user1, product1])
session.commit()

order1 = Order(user_id=user1.id, product_id=product1.id, quantity=2, status=False)
order2 = Order(user_id=user1.id, product_id=product1.id, quantity=1, status=True)

session.add_all([order1, order2])
session.commit()


print("\n--- Not Shipped Orders ---")
not_shipped_orders = session.query(Order).filter(Order.status == False).all()

for order in not_shipped_orders:
    print(f"Order {order.id} is NOT shipped")


print("\n--- Orders Per User ---")
order_counts = (
    session.query(User.name, func.count(Order.id))
    .join(Order)
    .group_by(User.id)
    .all()
)

for name, count in order_counts:
    print(f"{name} has {count} orders")
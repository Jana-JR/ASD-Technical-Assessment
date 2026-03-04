"""
Demonstrates SalesOrder usage including:
- Successful order creation
- Validation handling for invalid quantity and price
"""

from sales_order import SalesOrder
from exceptions import InvalidQuantityError, InvalidPriceError


def main() -> None:

    print("=== Sales Order Demo ===\n")

    order = SalesOrder(order_id="001", customer_name="janarthanan")
    order.add_item("Laptop", quantity=1, price=999.99)
    order.add_item("Mouse", quantity=2, price=29.99)
    order.add_item("USB drive", quantity=3, price=15.00)

    print(order.get_order_summary())

    # --- Invalid quantity ---
    print("\n--- Error: zero quantity ---")
    try:
        order.add_item("Keyboard", quantity=0, price=49.99)
    except InvalidQuantityError as e:
        print(f"Caught InvalidQuantityError: {e}")

    # --- Negative price ---
    print("\n--- Error: negative price ---")
    try:
        order.add_item("Monitor", quantity=1, price=-5.00)
    except InvalidPriceError as e:
        print(f"Caught InvalidPriceError: {e}")


if __name__ == "__main__":
    main()

from exceptions import InvalidQuantityError, InvalidPriceError


class SalesOrder:
    """Represents a simple sales order with items and total calculation."""

    def __init__(self, order_id: str, customer_name: str) -> None:
        """
        Initialise a new SalesOrder.

        Args:
            order_id: Unique identifier for the order.
            customer_name: Name of the customer placing the order.
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self._items: list[dict] = []

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """
        Add an item to the order.

        Args:
            name: Name of the item.
            quantity: Number of units (must be > 0).
            price: Unit price (must be >= 0).

        Raises:
            InvalidQuantityError: If quantity is not greater than zero.
            InvalidPriceError: If price is negative.
        """
        if quantity <= 0:
            raise InvalidQuantityError(f"Quantity must be greater than zero, Current value: {quantity}.")
        if price < 0:
            raise InvalidPriceError(f"Price cannot be negative, Current value: {price}.")

        self._items.append({"name": name, "quantity": quantity, "price": price})

    def calculate_total(self) -> float:
        """Return the total cost of all items in the order."""
        return sum(item["quantity"] * item["price"] for item in self._items)

    def get_order_summary(self) -> str:
        """Return a formatted string summary of the order."""
        lines = [
            f"Order ID : {self.order_id}",
            f"Customer : {self.customer_name}",
            "-" * 35,
        ]
        for item in self._items:
            subtotal = item["quantity"] * item["price"]
            lines.append(f"  {item['name']} x{item['quantity']} @ ${item['price']:.2f} = ${subtotal:.2f}")
        lines.append("-" * 35)
        lines.append(f"Total    : ${self.calculate_total():.2f}")
        return "\n".join(lines)

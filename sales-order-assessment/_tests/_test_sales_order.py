import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from sales_order import SalesOrder
from exceptions import InvalidQuantityError, InvalidPriceError


class TestSalesOrder(unittest.TestCase):

    def test_valid_order_total_and_summary(self):
        """A correctly built order should compute the right total and include customer name in summary """
        order = SalesOrder(order_id="001", customer_name="Jana")
        order.add_item("Widget", quantity=3, price=10.00)
        order.add_item("Gadget", quantity=1, price=25.50)

        self.assertAlmostEqual(order.calculate_total(), 55.50)
        summary = order.get_order_summary()
        self.assertIn("Jana", summary)
        self.assertIn("001", summary)

    def test_invalid_quantity_raises_error(self):
        """Adding item with quantity <= 0 should raise InvalidQuantityError """
        order = SalesOrder(order_id="002", customer_name="Afi")
        with self.assertRaises(InvalidQuantityError):
            order.add_item("Widget", quantity=0, price=5.00)

    def test_invalid_price_raises_error(self):
        """Adding item with negative price should raise InvalidPriceError """
        order = SalesOrder(order_id="003", customer_name="Kumar")
        with self.assertRaises(InvalidPriceError):
            order.add_item("Widget", quantity=2, price=-1.00)


if __name__ == "__main__":
    unittest.main()

class InvalidQuantityError(ValueError):
    """Raised when an item quantity is not greater than zero."""


class InvalidPriceError(ValueError):
    """Raised when an item price is negative."""

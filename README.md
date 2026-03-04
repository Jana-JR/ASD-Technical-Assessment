# ASD-Technical-Assessment

## Sales Order Assessment — Part 1

A simplified Sales Order system built with Python OOP.

### Prerequisites

- Python 3.8 or higher
- No external packages required

### Project Structure

```
sales-order-assessment/
├── src/
│   ├── exceptions.py   # Custom validation exceptions
│   ├── sales_order.py  # SalesOrder class
│   └── demo.py         # Runnable demo with error cases
└── _tests/
    └── _test_sales_order.py
```

### Running the Solution

```bash
python sales-order-assessment/src/demo.py
```

### Running the Tests

```bash
python sales-order-assessment/_tests/_test_sales_order.py -v
```

### Design Decisions

- **Items stored as plain dicts** — a separate `Item` class would be over-engineering for this scope.
- **Two custom exceptions** (`InvalidQuantityError`, `InvalidPriceError`) — kept distinct because the validation rules are semantically different, making error handling at the call site clearer.
- **`unittest`** — built-in, no install step needed.

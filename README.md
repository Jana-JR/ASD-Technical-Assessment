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


## Part 2 – Workflow and Business Logic Design

### 1. Workflow Description

To maintain financial control, orders exceeding $5,000 require manager approval before confirmation.

#### Standard Orders (≤ $5,000)

1. User creates order.  
2. System validates items and calculates total.  
3. Order is automatically confirmed.  
4. Customer receives confirmation notification.  

#### High-Value Orders (> $5,000)

1. User creates order.  
2. System calculates total.  
3. If total exceeds $5,000:  
   - Status is set to Pending Approval.  
   - Manager is notified.  
4. Manager reviews order details.  
5. Manager either:  
   - Approves → Order is confirmed.  
   - Rejects → Order is marked rejected and customer is notified.  

This ensures oversight without slowing down standard transactions.

---

### 2. Sequence of Steps

1. Order creation and validation  
2. Total calculation  
3. Threshold check  
4. If below threshold → Confirm  

5. If above threshold →  
   - Set status to Pending Approval  
   - Notify manager  
   - Await decision  

6. Manager approves or rejects  
7. System updates status and notifies customer  

---

### 3. Clarifying Questions

1. Is the $5,000 threshold configurable?  
2. Is approval single-level or multi-level?  
3. Is there a time limit for approval?  
4. Can rejected orders be edited and resubmitted?  
5. Should approval actions be logged for auditing?  

---

### 4. Risks and Challenges

- Approval delays – May slow order processing.  
- Hardcoded threshold – Reduces flexibility.  
- Notification failure – Manager may not receive alert.  
- Lack of audit logs – Reduces accountability.  

---

## Part 3 – Structured Problem Decomposition

### 1. Initial Requirement Clarification

Before starting implementation, I would clarify a few important points to avoid rework later:

1. What format is the Excel file provided in (.xlsx or .csv)?  
2. What exact fields are included in the file?  
3. What is the new custom field (data type, required or optional, validation rules)?  
4. How should duplicate customers be handled — merged, rejected, or updated?  
5. In what format should the sales report be generated (PDF, Excel or should be shown in dashboard view)?  
6. Should total sales include only confirmed orders or all orders?  

---

### 2. Implementation Approach

#### A. Import 5,000 Customer Records

**Step 1 –Analyze the Data**

- Examine the Excel structure.  
- Identify mandatory vs optional fields.  
- Map columns to the existing database schema.  

**Step 2 – Data Validation**

- Validate email format and required fields.  
- Check for duplicates (by email or customer ID).  
- Handle missing values.  

**Step 3 – Processing Strategy**

Since 5,000 records is a moderate volume, I would:

- Process records in batches to avoid high memory usage.  
- Use transactions to maintain consistency.  
- Log failed records separately for review.  

**Step 4 – Import Summary**

After processing:

- Display total records processed.  
- Number successfully imported.  
- Number failed with reasons.  

---

#### B. Add Custom Field to Customer Profile

**Step 1 – Database Change**

- Add a new column with proper data type.  
- Define whether it allows null values or requires a default.  

**Step 2 – Backend Update**

- Update the customer model.  
- Extend validation logic to include the new field.  

**Step 3 – API and UI Update**

- Update create/update endpoints.  
- Modify forms to include the new field.  

**Step 4 – Backward Compatibility**

- Ensure existing customers are not affected negatively.  
- Provide default values if required.  

---

#### C. Generate Total Sales Report per Customer

**Step 1 – Define Business Logic**

- Confirm that only approved/confirmed orders are included.  
- Group totals by customer.  

**Step 2 – Query Implementation**

- Use database aggregation (SUM with GROUP BY).  
- Add indexing if performance becomes an issue.  

**Step 3 – Output Format**

- Provide downloadable Excel or PDF.  
- Optionally allow dashboard visualization.  

**Step 4 – Performance optimization**

- Use pagination for large datasets.  
- caching if report is frequently requested.  

---

## Part 4 – Professional Reflection

### 1. Most Challenging Technical Issue

One of the most challenging issues I faced was improving the responsiveness of a real-time AI voice call system during my work on the Kural AI project. Users were experiencing a noticeable delay (around 15–20 seconds) before hearing the first AI greeting, and in some cases, calls would disconnect right after the greeting played.  

At first, it was frustrating because the system involved multiple components AI response generation, speech processing, and logging and it wasn’t clear where the delay was coming from. I initially focused on the AI generation time, but after tracing the flow more carefully, I realized that several independent operations were running one after another instead of in parallel. This was increasing the time before the caller heard any response.  

I gradually restructured parts of the flow so that independent tasks could run concurrently, and implimented a fallback greeting to reduce the time-to-first-audio. After these changes, the delay reduced significantly and call stability improved.

---

### 2. How I Approach Learning a New Technology

When learning a new technology, I prefer to start with the fundamentals instead of immediately following step-by-step tutorials. I try to understand the core problem the technology is solving and how it fits into a real system with help of AI tools.  

After that, I build a small working example to test my understanding. For example, when learning a new backend framework, I usually create a simple CRUD API first. This helps me understand routing, validation, and error handling in a practical way.  

Once I’m comfortable with the basics, I try to apply it in a bit more realistic scenario, such as integrating authentication or connecting it with a database. I’ve found that learning by building small but complete pieces helps me retain concepts better than just reading documentation.

---

### 3. If I Cannot Resolve a Technical Issue After Two Hours

If I cannot resolve an issue after spending around two hours, I avoid continuing without direction.  

First, I step back and review the problem from the beginning. I check whether I misunderstood any requirement or made assumptions. Then, I simplify the issue as much as possible and try to isolate the failing part.  

If I still cannot identify the root cause, I review official documentation or look for similar issues discussed by others. Before asking for help, I make sure I can clearly explain: What I expected to happen, What actually happened, What I have already tried.  

When I do ask for help, I try to make it efficient for the other person by sharing logs or a minimal reproducible example. I believe this shows respect for their time and also helps me learn faster.

---

### 4. Where I See My Professional Development in the Next Three Years

In the next three years, I aim to become a strong backend-focused engineer who understands not only how to implement features, but also why certain design decisions are made.  

I want to deepen my knowledge in areas such as system performance, API design, and security. I’m also interested in improving my understanding of how systems behave in production environments, especially around reliability and scalability.  

Long term, I would like to take more responsibility in designing solutions rather than only implementing assigned tasks. My goal is to grow into someone who can contribute thoughtfully to technical discussions and system decisions.

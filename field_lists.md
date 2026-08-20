<h1 align="center">Order States</h1>

---
#### Order Placed
- event_id
- order_id
- customer_id
- restaurant_id
- event_timestamp
- ingestion_timestamp
- items: [ { item_id, quantity, unit_price }, ... ]
- order_total
- discount_amount
- final_amount
- payment_mode

#### Order Accepted (by Hotel)
- event_id
- order_id
- restaurant_id
- acceptance_status
- event_timestamp
- ingestion_timestamp

#### Food Prepared
- event_id
- order_id
- restaurant_id
- status
- event_timestamp
- ingestion_timestamp
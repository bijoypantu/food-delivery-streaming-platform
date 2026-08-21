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
- delivery_location: { lat, long }

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
- event_timestamp
- ingestion_timestamp

#### Driver Assigned
- event_id
- order_id
- driver_id
- customer_id
- driver_response_status (accepted/rejected/timed_out)
- event_timestamp
- ingestion_timestamp

#### order_picked_up
- event_id
- order_id
- driver_id
- event_timestamp
- ingestion_timestamp

#### order_delivered
- event_id
- order_id
- driver_id
- customer_id
- event_timestamp
- ingestion_timestamp
- delivery_status

#### payment_made
- event_id
- order_id
- event_timestamp
- ingestion_timestamp
- payment : [ { payment_method, status, amount }, ... ]

#### order_cancelled
- event_id
- order_id
- event_timestamp
- ingestion_timestamp
- order_status
- refund_status
- cancelled_by (customer/restaurant/driver/system)
- cancellation_reason

<h1 align="center">Driver Activity</h1>

#### driver_location:
- event_id
- driver_id
- event_timestamp
- ingestion_timestamp
- latitude
- longitude
- speed

#### driver_shift_started:
  - event_id
  - driver_id
  - event_timestamp
  - ingestion_timestamp

#### driver_shift_ended:
  - event_id
  - driver_id
  - event_timestamp
  - ingestion_timestamp
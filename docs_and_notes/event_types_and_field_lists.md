# Kafka Event Topics

<h1 align="center">order_events</h1>

#### event_type: "order_placed"
- event_id
- order_id
- session_id
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

#### event_type: "order_accepted"
- event_id
- order_id
- restaurant_id
- acceptance_status
- event_timestamp
- ingestion_timestamp

#### event_type: "food_prepared"
- event_id
- order_id
- restaurant_id
- event_timestamp
- ingestion_timestamp

#### event_type: "driver_assigned"
- event_id
- order_id
- driver_id
- customer_id
- driver_response_status (accepted/rejected/timed_out)
- event_timestamp
- ingestion_timestamp

#### event_type: "order_picked_up"
- event_id
- order_id
- driver_id
- event_timestamp
- ingestion_timestamp

#### event_type: "order_delivered"
- event_id
- order_id
- driver_id
- customer_id
- event_timestamp
- ingestion_timestamp
- delivery_status

#### event_type: "payment_made"
- event_id
- order_id
- event_timestamp
- ingestion_timestamp
- payment : [ { payment_method, status, amount }, ... ]

#### event_type: "order_cancelled"
- event_id
- order_id
- event_timestamp
- ingestion_timestamp
- order_status
- refund_status
- cancelled_by (customer/restaurant/driver/system)
- cancellation_reason

<h1 align="center">driver_location</h1>

#### event_type: driver_location:
- event_id
- driver_id
- event_timestamp
- ingestion_timestamp
- latitude
- longitude
- speed

<h1 align="center">driver_shift_events</h1>

#### event_type: driver_shift_started:
- event_id
- driver_id
- event_timestamp
- ingestion_timestamp

#### event_type: driver_shift_ended:
- event_id
- driver_id
- event_timestamp
- ingestion_timestamp

<h1 align="center">app_events</h1>

#### event_type: "app_open"
- event_id
- session_id
- customer_id
- event_timestamp
- ingestion_timestamp

#### event_type: "search"
- event_id
- session_id
- customer_id
- search_query
- event_timestamp
- ingestion_timestamp

#### event_type: "add_to_cart"
- event_id
- session_id
- customer_id
- item_id
- quantity
- event_timestamp
- ingestion_timestamp

#### event_type: "remove_from_cart"
- event_id
- session_id
- customer_id
- item_id
- quantity
- event_timestamp
- ingestion_timestamp

#### event_type: "checkout_started"
- event_id
- session_id
- customer_id
- restaurant_id
- items: [{ item_id, quantity, unit_price }]
- total_price
- event_timestamp
- ingestion_timestamp
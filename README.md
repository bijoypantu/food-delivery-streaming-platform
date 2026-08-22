# Food Delivery Streaming Platform

A real-time streaming data platform simulating the backend of a food delivery service (Zomato/Blinkit-style) — built to go beyond the batch-only, single-machine architecture of my first project ([ecommerce-data-warehouse](https://github.com/bijoypantu/ecommerce-data-warehouse)) and gain hands-on experience with streaming ingestion, table-format internals, and declarative transformation.

## Why this project

My first project covered batch ETL end-to-end (Medallion architecture, SCD Type 2, Airflow orchestration, audit-driven data quality). This project deliberately targets what that one didn't: **streaming ingestion (Kafka), ACID table formats (Delta Lake), cloud-native storage (MinIO), declarative transformation (dbt), and data lineage (OpenLineage)** — while carrying forward the medallion thinking, event-driven design, and audit discipline from project 1.

## Architecture

```
Data Simulator (Python)
        ↓
     Kafka (KRaft mode, 4 topics)
        ↓
Spark Structured Streaming (watermarking, dedup)
        ↓
Delta Lake — Bronze (raw events) → Silver (validated, deduped)
        ↓
dbt — Gold layer (fact/dimension models, tests)
        ↓
Postgres — Warehouse / BI layer
```

Supporting services: **Airflow** (orchestrates dbt runs and batch jobs alongside the always-on streaming job) and **OpenLineage + Marquez** (lineage tracking across all layers).

## Domain model

Three simultaneous, semi-independent business processes are simulated:
- **Order fulfillment** — placed → hotel accepted → food prepared → driver assigned → picked up → delivered (or cancelled at any stage before pickup)
- **Driver activity** — shift start/end, continuous GPS telemetry, delivery acceptance/rejection, earnings, ratings
- **App/customer behaviour** — sessions, search, cart actions, checkout, funnel conversion

Full event schemas, the order state machine, and 41 business questions mapped to fact-table grains are documented in [`/designs`](./designs).

## Kafka topics

| Topic | Event types | Frequency |
|---|---|---|
| `order_events` | order_placed, order_accepted, food_prepared, driver_assigned, order_picked_up, order_delivered, payment_made, order_cancelled | Per order, irregular |
| `driver_location` | driver_location (GPS pings) | Every 3–5 sec per active driver |
| `driver_shift_events` | driver_shift_started, driver_shift_ended | ~2x per driver per day |
| `app_events` | app_open, search, add_to_cart, remove_from_cart, checkout_started | Per session, irregular |

Every event carries `event_id`, `event_type`, `event_timestamp`, and `ingestion_timestamp` — the dual-timestamp pattern is what enables late/out-of-order event handling in Silver via per-transition watermarks.

## Tech stack

- **Languages/runtimes**: Python 3.12, Java 17
- **Streaming**: Apache Kafka (KRaft mode, no Zookeeper), Spark Structured Streaming
- **Storage**: Delta Lake, MinIO *(planned)*
- **Transformation**: dbt *(planned)*
- **Warehouse**: PostgreSQL 16
- **Orchestration**: Apache Airflow *(planned)*
- **Observability**: OpenLineage + Marquez *(planned)*
- **Infra**: Docker Compose, WSL2 (Ubuntu 26.04)

## Project status

| Phase | Description | Status |
|---|---|---|
| 0 | Planning — event schemas, state machine, business questions, docker-compose skeleton | ✅ Complete |
| 1 | Data simulator (Python event generator) | 🔄 In progress |
| 2 | Kafka producers | ⬜ Not started |
| 3 | Spark Structured Streaming — Bronze ingestion | ⬜ Not started |
| 4 | Silver layer — watermarking, dedup, state validation | ⬜ Not started |
| 5 | dbt — Gold layer models + tests | ⬜ Not started |
| 6 | Warehouse load (Gold → Postgres) | ⬜ Not started |
| 7 | Airflow orchestration | ⬜ Not started |
| 8 | OpenLineage + Marquez observability | ⬜ Not started |
| 9 | Testing | ⬜ Not started |
| 10 | Documentation & polish | ⬜ Not started |

## Design docs

See [`/designs`](./designs) for the order state machine, system architecture diagram, and the full business-questions-to-grain mapping.

## Local setup

```bash
git clone git@github.com:bijoypantu/food-delivery-streaming-platform.git
cd food-delivery-streaming-platform
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker compose up -d
```

Requires: Python 3.12, Java 17 (JDK), Docker with Compose.
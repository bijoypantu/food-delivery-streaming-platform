# Kafka
### docker-compose
Kafka needs to know - 
- how it identifies itself
- how it stores its own metadata
- how other things reach it

The concepts you need before touching the compose file

1. Broker — a running Kafka instance. You'll run exactly one (a "single-node cluster") — fine for a personal project, real production systems run several for redundancy.

2. **KRaft mode needs a** `KAFKA_PROCESS_ROLES` — since there's no separate Zookeeper, the broker has to know it's playing both the "broker" (handles data) and "controller" (manages cluster metadata) roles itself. You'll set this to `broker, controller`.

3. **Listeners** — this is the part that trips everyone up first time. Kafka needs to define which network addresses it listens on, and critically, the address depends on who's asking — a container talking to Kafka from inside Docker's internal network needs a different address than your Python code running from WSL (outside Docker) trying to reach in. This is why Kafka configs typically define two listeners: one internal (for container-to-container, e.g. kafka:9092) and one external (for your host machine, e.g. localhost:9093).

4. A cluster ID — KRaft mode requires a unique ID for the "cluster" (even a single-node one) generated once, usually via a UUID.
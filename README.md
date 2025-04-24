# kafka-python-logstash-pipeline
# 🔄 Kafka Pipeline Demo

This project is a simple demonstration of a Kafka data processing pipeline using:

- 🐍 **Python**: Produces JSON log data to a Kafka topic.
- 🧪 **Kafka**: Serves as the data transport layer.
- 📥 **Logstash**: Consumes Kafka logs, processes them, and writes them to a structured JSON file.
- 🛠️ **Python Consumer** (optional): Demonstrates how to consume and process Kafka logs in real time.

---

## 📊 Architecture

```mermaid
graph TD
  A[Python Producer] --> B[Kafka Topic]
  B --> C[Logstash]
  C --> D[Transformed JSON File]
  B --> E[Python Kafka Consumer (optional)]

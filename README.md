# 🔄 Kafka Python Logstash Pipeline

This project demonstrates a basic data pipeline:

- Python script acts as a Kafka **Producer**.
- **Kafka** (Dockerized) serves as the broker.
- **Logstash** reads from Kafka, transforms messages, and writes to a JSON file.
- A separate Python **Consumer** reads from Kafka (optional).

---

## 📁 Project Structure

```
kafka-python-logstash-pipeline/
├── producer/
│   └── producer.py
├── consumer/
│   └── consumer.py
├── logstash/
│   └── logstash.conf
├── data/
│   └── processed_logs.json
├── requirements.txt
├── .gitignore
├── architecture_diagram.png
└── README.md
```

---

## 🧰 Prerequisites

- Python 3.7+
- Docker & Docker Compose
- Logstash
- pip, virtualenv

---

## 🚀 Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/kafka-python-logstash-pipeline.git
cd kafka-python-logstash-pipeline
```

---

### 2️⃣ Install Python Dependencies

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3️⃣ Start Kafka and Zookeeper via Docker

Create a Docker network:

```bash
docker network create kafka-net
```

Start Zookeeper:

```bash
docker run -d --name zookeeper --network kafka-net \
  -e ALLOW_ANONYMOUS_LOGIN=yes \
  bitnami/zookeeper:latest
```

Start Kafka:

```bash
docker run -d --name kafka --network kafka-net \
  -e KAFKA_BROKER_ID=1 \
  -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e ALLOW_PLAINTEXT_LISTENER=yes \
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092 \
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  bitnami/kafka:latest
```

---

### 4️⃣ Create a Kafka Topic

Enter Kafka container:

```bash
docker exec -it kafka bash
```

Create the topic:

```bash
/opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic log-topic \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
```

Exit container:

```bash
exit
```

---

### 5️⃣ Run Python Producer

```bash
cd producer
python producer.py
```

> This sends JSON messages to Kafka topic `log-topic`.

---

### 6️⃣ Run Logstash Pipeline

Make sure Logstash is installed and run:

```bash
logstash -f logstash/logstash.conf
```

> This reads from Kafka and writes processed logs to `data/processed_logs.json`.

If plugins are missing:

```bash
bin/logstash-plugin install logstash-input-kafka
bin/logstash-plugin install logstash-output-file
```

---

### 7️⃣ Run Python Consumer (Optional)

```bash
cd consumer
python consumer.py
```

> Consumes and prints Kafka messages from topic `log-topic`.

---

## ✅ Sample Output

\`\`\`json
{
  "timestamp": "2025-04-24T12:10:00",
  "user": "charlie",
  "action": "upload",
  "file": "report.pdf",
  "tag": "file_activity"
}
\`\`\`

---

## 📦 .gitignore

\`\`\`gitignore
__pycache__/
*.py[cod]
*.log
*.bak
.env/
venv/
data/
.idea/
.vscode/
logstash/.logstash_history
\`\`\`

---

## 🖼️ Architecture Diagram

![Architecture Diagram](architecture_diagram.png)

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙋 Contributing

Want to extend this with Elasticsearch or Avro? Contributions are welcome!

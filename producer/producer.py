from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

logs = [
    {"timestamp": "2025-04-24T10:00:00", "user": "alice", "action": "login"},
    {"timestamp": "2025-04-24T10:10:00", "user": "charlie", "action": "upload", "file": "report.pdf"},
]

for log in logs:
    producer.send('log-topic', log)
    print(f"Produced: {log}")
    time.sleep(1)

producer.flush()

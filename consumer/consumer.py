from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'log-topic',
    bootstrap_servers='localhost:9092',
    group_id='python-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

for message in consumer:
    log = message.value
    print(f"Consumed: {log}")
    # Add real-time alerting / saving / filtering logic here

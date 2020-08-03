from kafka import KafkaProducer

producer=KafkaProducer(broker_server='localhost:9092')
producer.send(topic='test',value='geshuai')

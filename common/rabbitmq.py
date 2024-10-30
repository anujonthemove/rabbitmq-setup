import pika
import os

class RabbitMQ:
    def __init__(self):
        self.user = os.getenv('RABBITMQ_USER', 'admin')
        self.password = os.getenv('RABBITMQ_PASSWORD', 'admin')
        self.host = os.getenv('RABBITMQ_HOST', 'localhost')
        self.port = int(os.getenv('RABBITMQ_PORT', 5672))
        self.connection = None
        self.channel = None
        self.connect()

    def connect(self):
        credentials = pika.PlainCredentials(self.user, self.password)
        parameters = pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        print("Connected to RabbitMQ")

    def publish(self, exchange_name, queue_name, message, routing_key):
        # Queue declaration to ensure it exists (optional, as it's already in definitions.json)
        self.channel.queue_declare(queue=queue_name, durable=True)

        # Publish the message directly without redeclaring the exchange
        self.channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=message
        )
        print(f"Sent '{message}' to exchange '{exchange_name}' with routing key '{routing_key}'")

    def consume(self, queue_name, callback):
        # Declare the queue to ensure it exists with the correct durability setting
        self.channel.queue_declare(queue=queue_name, durable=True)

        def on_message(channel, method_frame, header_frame, body):
            callback(body)
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)

        self.channel.basic_consume(queue=queue_name, on_message_callback=on_message)
        print(f"Waiting for messages in '{queue_name}'. To exit press CTRL+C")
        self.channel.start_consuming()

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            print("Connection closed")
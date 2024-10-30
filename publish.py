from common.rabbitmq import RabbitMQ


def publish_test_message():
    rabbitmq = RabbitMQ()
    try:
        # Ensure the exchange and routing key match the binding in definitions.json
        rabbitmq.publish(
            exchange_name='test_exchange', 
            queue_name='test_task_queue', 
            message='Hello RabbitMQ!',
            routing_key='test_task'
        )
    except Exception as e:
        print(f"Failed to publish message: {e}")
    finally:
        rabbitmq.close()

if __name__ == "__main__":
    publish_test_message()

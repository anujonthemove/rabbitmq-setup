from common.rabbitmq import RabbitMQ

def callback(body):
    print(f"Received message: {body.decode()}")

def main():
    rabbitmq = RabbitMQ()
    try:
        rabbitmq.consume(queue_name='test_task_queue', callback=callback)
    except KeyboardInterrupt:
        print("Interrupted! Stopping the consumer...")
        rabbitmq.channel.stop_consuming()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        rabbitmq.close()

if __name__ == "__main__":
    main()

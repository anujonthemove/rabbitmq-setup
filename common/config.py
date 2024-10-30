import os

class Config:
    # RabbitMQ Config
    RABBITMQ_USER = os.getenv('RABBITMQ_DEFAULT_USER', 'admin')
    RABBITMQ_PASS = os.getenv('RABBITMQ_DEFAULT_PASS', 'admin')
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
    RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
    RABBITMQ_MANAGEMENT_PORT = int(os.getenv('RABBITMQ_MANAGEMENT_PORT', 15672))

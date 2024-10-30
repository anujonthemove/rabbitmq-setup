# Use the official RabbitMQ image with the management plugin
FROM rabbitmq:3.12-management

# Copy RabbitMQ configuration and definition files into the container
COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf
COPY definitions.json /etc/rabbitmq/definitions.json

# Enable the RabbitMQ management plugin
RUN rabbitmq-plugins enable --offline rabbitmq_management

# Set RabbitMQ to load definitions on startup
ENV RABBITMQ_SERVER_START_ARGS='--load-definitions /etc/rabbitmq/definitions.json'

# Expose required RabbitMQ ports (AMQP, Management UI)
EXPOSE 5672 15672

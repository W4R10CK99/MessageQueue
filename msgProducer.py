import pika


# creating connection params such as hostname, port, credentials etc.
#since I am using rabbitmq locally, localhost should do the job
connection_parameters = pika.ConnectionParameters('localhost')


#connection variable
connection = pika.BlockingConnection(connection_parameters)

#create variable to store a channel
#a connection can have number of channels
channel = connection.channel()


#declare a queue in the channel
#here we have named our channel to be letterbox
channel.queue_declare(queue='letterbox')



#every channel must go through a exchange first, here we have used the default exchange
#hence used blank value for exchange param
message = "This is our initial message!"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent message : {message}")

#close connection

connection.close()






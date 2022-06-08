
import random
from paho.mqtt import client as mqtt_client

class PublisherMQTT:

    def __init__(self):
        self.broker = 'broker.emqx.io'
        self.port = 1883
        self.topic = "python/mqtt"
        # generate client ID with pub prefix randomly
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.username = 'emqx'
        self.password = 'public'
        self.client = None

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

    def publish(self, msg: str):
        result = self.client.publish(self.topic, msg)
        status = result[0]
        topic = self.topic
        
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
            

    

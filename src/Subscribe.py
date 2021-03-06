
import random
from paho.mqtt import client as mqtt_client

subscribe_data = ""

class SubscribeMQTT:
    def __init__(self):
        self.broker = 'broker.emqx.io'
        self.port = 1883
        self.topic = "python/mqtt"
        # generate client ID with pub prefix randomly
        self.client_id = f'python-mqtt-{random.randint(0, 100)}'
        self.username = 'emqx'
        self.password = 'public'
        self.client = None
        
    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
                
        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)

    def get_data(self):
        global subscribe_data
        data = subscribe_data
        return data

    def clear_data(self):
        global subscribe_data
        subscribe_data = ""

    def subscribe(self):
        def on_message(client, userdata, msg):
            global subscribe_data
            subscribe_data = msg.payload.decode('utf8')
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        self.client.subscribe(self.topic)
        self.client.on_message = on_message
        # self.client.loop_start()

    def start(self):
        self.client.loop_start()
        
    def stop(self):
        self.client.loop_stop()

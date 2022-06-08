
import time

from Publish import PublisherMQTT

def x():
    foo = PublisherMQTT()
    foo.connect_mqtt()
    time.sleep(2)
    while True:
        a = input("entrada: ")
        if a == "salir": break
        foo.publish(a)

x()

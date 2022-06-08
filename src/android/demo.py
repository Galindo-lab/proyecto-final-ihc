
from Publish import PublisherMQTT

def x():
    foo = PublisherMQTT()
    foo.connect_mqtt()
    while True:
        a = input("entrada: ")
        if a != "salir":
            foo.publish(a)
        else:
            break

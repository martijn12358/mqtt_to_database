import paho.mqtt.client as mqtt
import _mysql_connector

broker = "eu.thethings.network"
port = 1883
username = ""
password = ""
sql_user = 'developer'
sql_password = 'PD@LORAWAN'
sql_host = '127.0.0.1'


def on_connect(client, userdata, flags, rc):
    """
    The callback for when the client receives a CONNACK response from the server.
    :param client: the client instance for this callback
    :param userdata: the private user data as set in Client() or user_data_set()
    :param flags: response flags sent by the broker
    :param rc: the connection result
    :return: void
    """
    if rc == 0:
        print("\nConnected with result code " + str(rc))
    else:
        print("\nFailed to connect, return code %d\n", rc)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("")

def on_message(client, userdata, msg):
    """
    The callback for when a PUBLISH message is received from the server.
    :param client: the client instance for this callback
    :param userdata: the private user data as set in Client() or user_data_set()
    :param msg: an instance of MQTTMessage. This is a class with members topic, payload, qos, retain.
    :return: void
    """
    print(msg.topic + " " + str(msg.payload))

def run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username, password)
    client.connect(broker, port, 60)
    client.loop_forever()


run()
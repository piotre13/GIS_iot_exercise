
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import json
import geopandas as gpd


class MonitorService:
    def __init__(self, id, broker_add, broker_port):
        self.id = id
        self.broker_add = broker_add
        self.broker_port = broker_port
    
    def start(self):
        self.client = mqtt.Client(callback_api_version = CallbackAPIVersion.VERSION2, client_id=self.id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker_add, self.broker_port)
        self.client.subscribe('earthquake_data')
        self.client.loop_start()

    def on_connect(self,client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")

    def on_message(self, client, userdata, msg):
        message = json.loads(msg.payload.decode())
        print(f"Received message: {message}")

if __name__ == "__main__":
    monitor_service = MonitorService(id='monitor_service_1', broker_add='broker.hivemq.com', broker_port=1883)
    monitor_service.start()

    while True:
        pass
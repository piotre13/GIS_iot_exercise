import geopandas as gpd
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import json
import time


class Collector:
    def __init__(self, data, id, broker_add, broker_port):
        self.data = gpd.read_file(data)
        self.id = id
        self.broker_add = broker_add
        self.broker_port = broker_port
    
    def start(self):
        body={}
        answer=requeste.post(ursl, body)
        #request to the catalog to get broker addr adn broker port and id
        self.client = mqtt.Client(callback_api_version = CallbackAPIVersion.VERSION2, client_id=self.id)
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker_add, self.broker_port)
        self.client.loop_start()

    def on_connect(self,client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")

    def run(self):
        data = self.data.sort_values(by='time')
        print(data.loc[:,['time', 'mag']].head())

        msg = {'time':None, 'mag':None, 'place':None, 'point':None}
        
        for index, row in self.data.iterrows():
            msg['time'] = row['time']
            msg['mag'] = row['mag']
            msg['place'] = row['place']
            msg['point'] = row['geometry'].wkt

            message = json.dumps(msg)
            self.client.publish(topic='earthquake_data', payload=message)
            time.sleep(5)




if __name__ == "__main__":
    collector = Collector(data='earthquake_data.json', id='collector_1', broker_add='broker.hivemq.com', broker_port=1883)
    collector.start()
    collector.run()

    while True:
        time.sleep(1)
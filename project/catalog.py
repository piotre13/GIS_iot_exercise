from flask import Flask, jsonify, request
import threading
import time
catalog = {
    "broker_address": "broker.hivemq.com",
    "broker_port": 1883,
    "main_topic": "earthquake_data",
    "collectors": []
}

app = Flask('project')

@app.route('/earthquake_catalog', methods=['GET'])
def get_catalog():
    return jsonify(catalog)


@app.route('/earthquake_catalog/collectors', methods=['POST'])
def add_collector():
    data = request.get_json()

    id = 'collector_' + str(len(catalog["collectors"]) + 1)
    topic = catalog["main_topic"] +'/'+data['area_name']
    new_collector = {
        "id": id,
        "area_name": data['area_name'],
        "topic": topic,
        "sensor_list": data['sensor_list']
        }

    catalog["collectors"].append(new_collector)

    answer = {
        "message": "Collector added successfully",
        "collector_id": id,
        "topic": topic,
        "broker_address": catalog["broker_address"],
        "broker_port": catalog["broker_port"]
    }
    return jsonify(answer)


t2 = threading.Thread(target=lambda: app.run(port=5001, use_reloader=False))
t2.daemon = True
t2.start()
time.sleep(1)
while True:
    time.sleep(1)
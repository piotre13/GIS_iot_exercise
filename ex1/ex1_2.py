senml_data = {
    'bn': 'urn:dev:ow:10e2073a01080063',
    'bt': 1.276020076001e+09,
    'e': [
        {'n': 'temperature', 'u': 'Cel', 'v': 23.5},
        {'n': 'humidity', 'u': '%RH', 'v': 60.0}
    ]
}



base_name = senml_data["bn"]
base_time = senml_data["bt"]

for record in senml_data['e']:


    if "v" in record:
        full_name = base_name + record.get("n", "")
        unit = record.get("u", "")
        value = record["v"]
        print(f"{full_name}: {value} {unit} at time {base_time}")
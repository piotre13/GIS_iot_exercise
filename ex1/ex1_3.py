geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Turin"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [7.6869, 45.0703]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Milan"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [9.1900, 45.4642]
            }
        }
    ]
}


for feature in geojson_data["features"]:
    name = feature["properties"]["name"]
    lon, lat = feature["geometry"]["coordinates"]
    print(f"{name}: latitude={lat}, longitude={lon}")
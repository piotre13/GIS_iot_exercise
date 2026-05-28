import requests
import json
import geopandas as gpd


# url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2015-01-01&endtime=2016-10-01'
# geojson_data = requests.get(url=url)
# print(geojson_data.status_code)
# if geojson_data.status_code == 200:
#     geojson_data = geojson_data.json()

# print(geojson_data)

# with open('earthquake_data.json', 'w') as f:
#     json.dump(geojson_data, f)


# japan = gpd.read_file('resources/Japan.json') 
# peru = gpd.read_file('resources/Peru.json')
# heartquakes = gpd.read_file('earthquake_data.json').to_crs(japan.crs)
# print(heartquakes.shape[0])




# heartquakes_japan=gpd.sjoin(heartquakes, japan, how='inner', predicate='intersects')
# heartquakes_peru=gpd.sjoin(heartquakes, peru, how='inner', predicate='intersects')

# print('Earthquakes in Japan:', heartquakes_japan.shape[0])
# print('Earthquakes in Peru:', heartquakes_peru.head())
# print('Earthquakes in Peru:', heartquakes_peru.shape[0])



# url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?latitude=36&longitude=138&maxradiuskm=1000&format=geojson'
# response = requests.get(url=url)
# print(response.status_code)
# if response.status_code == 200:
#     earthquake_data = response.json()
#     print(earthquake_data)

# print(len(earthquake_data['features']))
# with open('earthquake_data_japan.json', 'w') as f:
#     json.dump(earthquake_data, f)


japan_data = gpd.read_file('earthquake_data.json')

print(japan_data.head())
print(japan_data.columns)

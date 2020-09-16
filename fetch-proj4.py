import requests
import json
from tqdm import tqdm


tm3_zones = [
    46.2,
    47.1,
    47.2,
    48.1,
    48.2,
    49.1,
    49.2,
    50.1,
    50.2,
    51.1,
    51.2,
    52.1,
    52.2,
    53.1,
    53.2,
    54.1,
]
utm_zones_north = [
    "46N",
    "47N",
    "48N",
    "49N",
    "50N",
    "51N",
    "52N",
    "53N",
    "54N",
]

utm_zones_south = [
    "46S",
    "47S",
    "48S",
    "49S",
    "50S",
    "51S",
    "52S",
    "53S",
    "54S",
]

tm3_proj4_list = []
base_url = "https://www.spatialreference.org/ref/epsg"
for zone in tqdm(tm3_zones):
    url = f"{base_url}/dgn95-indonesia-tm-3-zone-{str(int(zone*10))}/proj4/"
    with requests.get(url) as response:
        response.raise_for_status()

        name = f"DGN95 / Indonesia TM-3 zone {zone}"
        tm3_proj4_list.append({"name": name, "ref": response.text})


"https://www.spatialreference.org/ref/epsg/32748/proj4/"

utm_proj4_list = []
for i, zone in tqdm(enumerate(utm_zones_north)):
    url = f"{base_url}/{32646 + i}/proj4/"
    with requests.get(url) as response:
        response.raise_for_status()

        name = f"WGS 84 / UTM zone {zone}"
        utm_proj4_list.append({"name": name, "ref": response.text})

for i, zone in tqdm(enumerate(utm_zones_south)):
    url = f"{base_url}/{32746 + i}/proj4/"
    with requests.get(url) as response:
        response.raise_for_status()

        name = f"WGS 84 / UTM zone {zone}"
        utm_proj4_list.append({"name": name, "ref": response.text})

proj4_list = {"tm3": tm3_proj4_list, "utm": utm_proj4_list}

with open("proj4.json", "w") as outfile:
    json.dump(proj4_list, outfile)

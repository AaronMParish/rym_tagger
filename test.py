from rymscraper import rymscraper, RymUrl
import pandas as pd
import json

network = rymscraper.RymNetwork()

artist_infos = network.get_artist_infos(name="Aaron Is Sarah")

print(json.dumps(artist_infos, indent=2, ensure_ascii=False))
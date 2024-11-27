#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from download_json import download_json

dl_json = download_json()
ids = ["E135023", "E234025", "E214024"]
for id in ids:
    print(id)
    json_text, error = dl_json.get_json(id)
    if json_text is None:
        print("\tJSON Error: " + error)
    else:
        print("\tJSON Ok ")
        json_object = json.loads(json_text)
        print("\t" + json_object["status"])

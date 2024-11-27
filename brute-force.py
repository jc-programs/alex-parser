#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from download_json import download_json

ids = ["E135023", "E234025", "E214024"]

letras = ["A", "E", "J", "S"]
anyos = ["024", "025"]
eventos = range(100,1000)

dl = download_json()
dl.set_use_sleep(False)
for letra in letras:
    for anyo in anyos:
        for evento in eventos:
            id = "%s%03d%s" % (letra, evento, anyo)
            json_text, error = dl.get_json(id)
            if json_text is None:
                print("\tJSON Error: " + error)
            else:
                print("\tJSON Ok ")
                json_object = json.loads(json_text)
                print("\t" + json_object["status"])


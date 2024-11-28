#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from download_json import download_json

letras = ["A", "E", "J", "S"]
anyos = ["024", "025"]
eventos = range(0,1000)

dl = download_json()
dl.set_use_sleep(False)
for letra in letras:
    for anyo in anyos:
        for evento in eventos:
            id = "%s%03d%s" % (letra, evento, anyo)
            json_text, error = dl.get_json(id)
            if json_text is None:
                print(id + " JSON Error: " + error)
            else:
                json_object = json.loads(json_text)
                print(id + " " + json_object["status"])


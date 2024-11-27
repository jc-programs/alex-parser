#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from download_html import download_html
from download_json import download_json

ids = ["E135023", "E234025", "E214024"]
dl_html = download_html()
dl_json = download_json()
for id in ids:
    html, error = dl_html.get_html(id)
    print(id)
    if html is None:
        print("\tHTML Error: " + error)
    else:
        print("\tHTML Ok")
        # print(html)
    json_text, error = dl_json.get_json(id)
    if json_text is None:
        print("\tJSON Error: " + error)
    else:
        print("\tJSON Ok ")
        # print(json_text)
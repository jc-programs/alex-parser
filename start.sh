#!/bin/bash

python3 -m venv env
. env/bin/activate
pip install pipreqs
pip install requests
pip install curl_cffi
pipreqs --force .

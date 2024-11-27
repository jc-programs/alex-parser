

from os import makedirs
from os.path import isdir, isfile, dirname, realpath
from pathlib import Path
from curl_cffi import requests as cureq
from random import randint
from time import sleep

class download_json:
    _path = None
    _use_sleep = True

    def __init__(self):
        path = Path(dirname(realpath(__file__)))
        path_cache = path.joinpath( 'cache' )
        if not isdir( path_cache ):
            makedirs( path_cache )
        self._path = path_cache

    def set_use_sleep(self,use_sleep:bool):
        self._use_sleep = use_sleep

    def get_url(self,id:str) -> str:
        # https://contractorpass-api.firabarcelona.com/v1/event/showcode/E234025
        return "https://contractorpass-api.firabarcelona.com/v1/event/showcode/" + id

    def cache_file(self, id:str) -> str:
        return Path.joinpath( self._path, id + '.json' )

    def download(self, id:str, retry:int=3) -> list[str, str]:
        url = self.get_url(id)
        while retry > 0:
            retry -= 1
            r = cureq.get(url,impersonate="chrome")
            if self._use_sleep:
                sleep(randint(3,5))
            if r.status_code != 200:
                if r.status_code == 400:
                    return "{\"status\" : \"NO EXISTE\"}", ''
                    break
                if retry == 0:
                    return None, f"impossible to download json from: {url}"
            else:
                break
        return r.content.decode('utf-8', errors='ignore'), ''

    def get_json(self, id:str) -> list[str,str]:
        file = self.cache_file(id)
        if not isfile(file):
            json_text, error = self.download( id )
            if json_text is None:
                return None, error
            with open(file,'w') as file:
                file.write( json_text )
        else:
            with open(file,'rb') as file:
                json_text = file.read()
        return json_text, ''

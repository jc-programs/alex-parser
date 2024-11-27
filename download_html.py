

from os import makedirs
from os.path import isdir, isfile, dirname, realpath
from pathlib import Path
import requests
from random import randint
from time import sleep

class download_html:
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
        # https://contractorpass.firabarcelona.com/WEB/E135023/passes
        return "https://contractorpass.firabarcelona.com/WEB/" + id + "/passes"

    def cache_file(self, id:str) -> str:
        return Path.joinpath( self._path, id + '.html' )

    def get_download_headers(self) -> dict:
        return {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }

    def download(self, id:str, retry:int=3) -> list[str, str]:
        url = self.get_url(id)
        while retry > 0:
            retry -= 1
            r = requests.get(url,headers=self.get_download_headers())
            if self._use_sleep:
                sleep(randint(3,5))
            if r.status_code != 200:
                if retry == 0:
                    return None, f"impossible to download html from: {url}"
            else:
                break
        return r.content.decode('utf-8', errors='ignore'), ''

    def get_html(self,id) -> list[str,str]:
        file = self.cache_file(id)
        if not isfile(file):
            html, error = self.download( id )
            if html is None:
                return None, error
            with open(file,'w') as file:
                file.write( html )
        else:
            with open(file,'rb') as file:
                html = file.read()
        return html, ''

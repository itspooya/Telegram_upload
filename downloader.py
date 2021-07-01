import requests
import re
from requests.exceptions import RequestException
import urllib
import shutil

def get_file_size(url):
    if url.lower().startswith('http'):
        req = urllib.request.Request(url,method="HEAD")
    else:
        raise ValueError from None
    with urllib.request.urlopen(req) as fil:
        if fil.status==200:
            return fil.headers['Content-Length']
        else:
            raise "ERROR Getting File"

        return len(fil.content)

def download(url):
    try:
        with requests.get(url,stream=True) as r:

            fname = ''
            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = url.split("/")[-1]
            with open("{}".format(fname), "wb") as f:
                shutil.copyfileobj(r.raw, f)
    except RequestException as e:
        print(e)
    return fname

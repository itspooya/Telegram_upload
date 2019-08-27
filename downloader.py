import requests
import re
from requests.exceptions import RequestException


def download(url):
    try:
        with requests.get(url) as r:

            fname = ''
            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = url.split("/")[-1]
    except RequestException as e:
        print(e)
    with open("{}".format(fname),"wb") as f:
        f.write(r.content)
    return fname
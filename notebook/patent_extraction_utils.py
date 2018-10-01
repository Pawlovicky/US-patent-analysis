import requests
from bs4 import BeautifulSoup
import urllib
import os

def download_all_links(lnk, target_dir):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko"\
               "/20100101 Firefox/57.0",}
    rr = requests.get(lnk, headers=headers)
    html = rr.content
    soup = BeautifulSoup(html, "html.parser")
    urls = [x.get('href') for x in soup.find_all('a') 
            if '.zip' in x.get('href')]
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    [urllib.request.urlretrieve(lnk + x, target_dir + x) for x in urls]
    

import requests
from bs4 import BeautifulSoup as bs
def soup_collector(item_id, item_type):
    url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=" + item_id + "&db=" + item_type + "&report=genbank&extrafeat=null&conwithfeat=on&retmode=html&tool=portal&withmarkup=on&maxdownloadsize=1000000"
    data = requests.get(url)
    soup = bs(data.content, 'html.parser')

    #killing javascripts and stylesheets
    for script in soup(["script", "style"]):
        script.decompose()
    return soup.text


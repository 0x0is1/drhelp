import requests
import urllib.parse
import random
from bs4 import BeautifulSoup as bs

def search_id_list(name, filter1, filter2, category_type):
    term = urllib.parse.quote(name)

    cookies = {
        'ncbi_sid': 'CE8C4638E6FC4D21_099'+str(random.randint(0000, 100000))+'SID',
    }
    requests.get('https://www.ncbi.nlm.nih.gov/'+ category_type +'/?term=' + term, cookies=cookies)



    headers = {
        'Host': 'www.ncbi.nlm.nih.gov',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '5091',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }

    data = 'EntrezSystem2.PEntrez.'+ filter1 + '.'+ filter2 + '_ResultsPanel.'+ filter2 +'_DisplayBar.Presentation=uilist&EntrezSystem2.PEntrez.'+ filter1 +'.'+ filter2 +'_ResultsPanel.Entrez_Pager.CurrPage=1&EntrezSystem2.PEntrez.DbConnector.LastQueryKey=1&EntrezSystem2.PEntrez.DbConnector.Cmd=displaychanged'

    response = requests.post('https://www.ncbi.nlm.nih.gov/'+ category_type, headers=headers, cookies=cookies, data=data, verify=True)
    soup = bs(response.content, 'html.parser')
    print(soup.text)

def search_detail(name, category_type):
    term = urllib.parse.quote(name)
    url = 'https://www.ncbi.nlm.nih.gov/' + category_type +'/?term=' + term + '&report=docsum&format=text'
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    print(soup.text)

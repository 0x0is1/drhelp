from bs4 import BeautifulSoup as bs
import requests
from stem_loop import feature_stem_loop
from gene import feature_gene
from peptide import feature_peptide
from cds import feature_cds
from source import feature_source

def data_collector(sample_id, sample_type, report_type, doc_type):
    
    if doc_type == 'html':
        #do stuff 
        genefeature = feature_gene(sample_id, sample_type)
        slfeature = feature_stem_loop(sample_id, sample_type)
        pfeature = feature_peptide(sample_id, sample_type)
        cfeature = feature_cds(sample_id, sample_type)
        sofeature = feature_source(sample_id, sample_type)
        comment = comment(sample_id, sample_type)
        return genefeature, slfeature, pfeature, cfeature, sofeature, comment

    else:
        url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=" + sample_id + "&db=" + sample_type + "&report=" + report_type +"&extrafeat=null&conwithfeat=on&retmode="+doc_type+"&tool=portal&maxdownloadsize=1000000"
        data = requests.get(url)
        soup = bs(data.content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        return soup, url


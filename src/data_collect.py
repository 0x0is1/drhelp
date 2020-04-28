from bs4 import BeautifulSoup as bs
import requests
from name_collect import name_collector
from get_comment import comment
from stem_loop import feature_stem_loop
from gene import feature_gene
from peptide import feature_peptide
from cds import feature_cds
from source import feature_source
from options import *
from sequence import chain_sequence
from intro import intro

def data_collector(sample_id, sample_type, report_type, doc_type, req):
    
    if doc_type == 'html':
        #do stuff
        if req == "intro":
            return intro(sample_id, sample_type)
        if req == "name":
            return name_collector(sample_id, sample_type)
        if req == "gene":
            return feature_gene(sample_id, sample_type)
        if req == "stem-loop":
            return feature_stem_loop(sample_id, sample_type)
        if req == "peptide":
            return feature_peptide(sample_id, sample_type)
        if req == "cds":
            return feature_cds(sample_id, sample_type)
        if req == "source":
            return feature_source(sample_id, sample_type)
        if req == "comment":
            return comment(sample_id, sample_type)
        if req == "sequence":
            return chain_sequence(sample_id, sample_type)
        else:
            print('Invalid parameter supplied!')
    
    else:
        url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=" + sample_id + "&db=" + sample_type + "&report=" + report_type +"&extrafeat=null&conwithfeat=on&retmode="+doc_type+"&tool=portal&maxdownloadsize=1000000"
        data = requests.get(url)
        soup = bs(data.content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        return soup, url

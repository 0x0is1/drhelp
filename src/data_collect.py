from bs4 import BeautifulSoup as bs
import requests
from get_comment import comment
from stem_loop import feature_stem_loop
from gene import feature_gene
from peptide import feature_peptide
from cds import feature_cds
from source import feature_source
from options import *
from sequence import chain_sequence
sample_id = 1798174254 #SARS_CoV-2 sample id
#sample_id = 16555694
sample_type = "nuccore" #nucleotide
report_type = "genbank"
doc_type = "html"

def data_collector(sample_id, sample_type, report_type, doc_type, req):
    
    if doc_type == 'html':
        #do stuff
        def genefeature(): feature_gene(sample_id, sample_type),
        def slfeature(): feature_stem_loop(sample_id, sample_type),
        def pfeature(): feature_peptide(sample_id, sample_type),
        def cfeature(): feature_cds(sample_id, sample_type),
        def sofeature(): feature_source(sample_id, sample_type),
        def comments(): comment(sample_id, sample_type),
        def sequence(): chain_sequence(sample_id, sample_type)
        if req == "gene":
            return genefeature()
        if req == "stem-loop":
            return pfeature()
        if req == "peptide":
            return pfeature()
        if req == "cds":
            return cfeature()
        if req == "source":
            return cfeature()
        if req == "comment":
            return comments()
        if req == "sequence":
            return sequence()
        else:
            print('Unknown parameter supplied!')
    
    else:
        url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=" + sample_id + "&db=" + sample_type + "&report=" + report_type +"&extrafeat=null&conwithfeat=on&retmode="+doc_type+"&tool=portal&maxdownloadsize=1000000"
        data = requests.get(url)
        soup = bs(data.content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        return soup, url

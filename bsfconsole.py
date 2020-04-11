import requests
from bs4 import BeautifulSoup as bs
import os
import time

#iterator = 0

#class sample_types:
#todo


#default data provided
sample_id = 1798174254 #SARS_CoV-2 sample id
#sample_id = 16555694
sample_type = "nuccore" #nucleotide
report_type = "genbank"
doc_type = "json"

def visualize():
    print("todo stuffs for visualizing")


def soup_collector(item_id, item_type):
    url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=" + item_id + "&db=" + item_type + "&report=genbank&extrafeat=null&conwithfeat=on&retmode=html&tool=portal&withmarkup=on&maxdownloadsize=1000000"
    data = requests.get(url)
    soup = bs(data.content, 'html.parser')

    #killing javascripts and stylesheets
    for script in soup(["script", "style"]):
        script.decompose()
    return soup

def name_collector(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_type = soup.findAll('a')
    
    #unwanted till now START
    try:
        sample_info_name1 = sample_info_type[0].get('name').split('_')[1].strip()
        sample_info_name2 = sample_info_type[0].get('name').split('_')[2].strip()
        sample_info_name = sample_info_name1 + "_" + sample_info_name2
    except:
        sample_info_name = sample_info_type[0].get('name').split('_')[1].strip()
    return sample_info_name
    #END
#intro

def intro(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)
    
    try:
        raw_intro = soup.findAll('a', {"name":'comment_' + sample_info_name})[0]        
        intro7 = raw_intro.previousSibling
        intro6 = raw_intro.previousSibling.previousSibling
        intro5 = raw_intro.previousSibling.previousSibling.previousSibling
        intro4 = raw_intro.previousSibling.previousSibling.previousSibling.previousSibling
        intro3 = raw_intro.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling
        intro2 = raw_intro.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling
        intro1 = raw_intro.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling
        intro = str(intro1) + str(intro2) + str(intro3) + str(intro4) + str(intro5) + str(intro6) + str(intro7)
        return intro 
    except:
        pass

def comment(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)
    
    
    try:
        raw_intro = soup.findAll('a', {"href":'https://www.ncbi.nlm.nih.gov/RefSeq/'})[0]
        intro7 = raw_intro.nextSibling
        intro6 = raw_intro.nextSibling.nextSibling
        intro5 = raw_intro.nextSibling.nextSibling.nextSibling
        intro4 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling
        intro3 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling
        intro2 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling
        intro1 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling
        intro = str(intro7) + str(intro6) + str(intro5) + str(intro4) + str(intro3) + str(intro2) + str(intro1)
        return intro
    except:
        pass
       

#    intro = str(intro1) + str(intro2) + str(intro3) + str(intro4) + str(intro5) + str(intro6) + str(intro7)

#    comment
##   __TODO__
    
#feature
##    feature PART1
def feature_source(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)
    iterator = 0
    while True:
        source = soup.find('span', {"id": "feature_" + sample_info_name + "_source_" + str(iterator)})   
        if source == None:
            break
        return source.text
        iterator += 1

##    feature PART2
def feature_gene(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)
    iterator = 0
    while True:
        gene = soup.find('span', {"id": "feature_" + sample_info_name + "_gene_" + str(iterator)})
        if gene == None:
            break
        return gene.text
        iterator += 1



## feature PART3
def feature_cds(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)    
    iterator = 0
    while True:
        cds = soup.find('span', {"id": "feature_" + sample_info_name + "_CDS_" + str(iterator)})
        if cds == None:
            break
        return cds.text
        iterator += 1

def feature_peptide(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)
    iterator = 0
    while True:
        source = soup.find('span', {"id": "feature_" + sample_info_name + "_mat_peptide_" + str(iterator)})   
        if source == None:
            break
        return source.text
        iterator += 1

def feature_stem_loop(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)
    iterator = 0
    while True:
        stem_loop = soup.find('span', {"id": "feature_" + sample_info_name + "_stem_loop_" + str(iterator)})   
        if stem_loop == None:
            break
        return stem_loop.text
        iterator += 1
#    return comment, feature, intro ,url

'''
    well, you can keep the item type as variable but for any "special case purpose", i defined all separately
'''






def show_options():
    print("todo stuffs")




def data_collector(sample_id, sample_type, report_type, doc_type):
    
    if doc_type == 'html':
        #do stuff 
        feature = feature(sample_id, sample_type)
        comment = comment(sample_id, sample_type)
        return comment, feature
        
    else:
        url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=" + sample_id + "&db=" + sample_type + "&report=" + report_type +"&extrafeat=null&conwithfeat=on&retmode="+doc_type+"&tool=portal&maxdownloadsize=1000000"
        data = requests.get(url)
        soup = bs(data.content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        return soup, url

def formal():
        print('Welcome to the Bio-samples framework')
        print('Brought to you by 0x0is1 (github.com/0x0is1)')
        print('With the support of National Center for BioTechnology Information')
        print('(https://www.ncbi.nlm.nih.gov)')
        print('')
        print('Enter commands to interact with Framework')
        print('Type Help to see available commands')

def main():

    formal()
    while True:
        raw_command = input("> ")

        try:
            command, details = raw_command.split(" ")
            print(command)
            print(details)

        except:
            command = raw_command
        
        data, url = data_collector(str(sample_id), str(sample_type), str(report_type), str(doc_type))

        cases = {
            0:"exit",
            1:"cls",
            2:"get",
            3:"help",
            4:"set",
            5:"visualize",
            6: "ftp"
        }


        if command == "":
            print('No command supplied. type help to see all commands')

        if command == cases[0]:
            exit(0)

        if command == cases[1]:
            os.system('clear')
            formal()

        if command == cases[2]:
            print(data)

        if command == cases[5]:
            print (url)   
            os.system('firefox-esr ' + url) #to be improved         

        else:
            os.system(command)
        

if __name__ == "__main__":
    #main()
    print(comment(str(sample_id), str(sample_type)))
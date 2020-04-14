from soup import soup_collector
from name_collect import name_collector
## feature PART3
def feature_cds(spl_id, spl_type):
    def cds(spl_id_dup, spl_type_dup):
        soup = soup_collector(spl_id, spl_type)
        sample_info_name = name_collector(spl_id, spl_type)    
        iterator = 0
        while True:
            cds = soup.find('span', {"id": "feature_" + sample_info_name + "_CDS_" + str(iterator)})
            if cds == None:
                break
            print(cds.text)
            iterator += 1
    value = cds(spl_id, spl_type)
    return value

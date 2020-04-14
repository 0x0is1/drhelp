from soup import soup_collector
from name_collect import name_collector
## feature PART1
def feature_source(spl_id, spl_type):
    def source(spl_id_dup, spl_type_dup):
        soup = soup_collector(spl_id, spl_type)
        sample_info_name = name_collector(spl_id, spl_type)
        iterator = 0
        while True:
            source = soup.find('span', {"id": "feature_" + sample_info_name + "_source_" + str(iterator)})   
            if source == None:
                break
            print(source.text)
            iterator += 1
    value = source(spl_id, spl_type)
    return value

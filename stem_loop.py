from soup import soup_collector
from name_collect import name_collector

## feature PART5
def feature_stem_loop(spl_id, spl_type):
    def stem(spl_id_dup, spl_type_dup):
        soup = soup_collector(spl_id, spl_type)
        sample_info_name = name_collector(spl_id, spl_type)
        iterator = 0
        while True:
            stem_loop = soup.find('span', {"id": "feature_" + sample_info_name + "_stem_loop_" + str(iterator)})   
            if stem_loop == None:
                break
            print(stem_loop.text)
            iterator += 1
    value = stem(spl_id, spl_type)
    return value

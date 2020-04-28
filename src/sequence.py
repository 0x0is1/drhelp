from soup import soup_collector
from name_collect import name_collector

def chain_sequence(spl_id, spl_type):
    def sequence(spl_id_dup, spl_type_dup):
        soup = soup_collector(spl_id, spl_type)
        sample_info_name = name_collector(spl_id, spl_type)
        iterator = 1
        while True:
            source = soup.find('span', {"id": sample_info_name + "_" + str(iterator)})   
            if source == None:
                break
            iterator += 60            
            print(iterator, source.text)

    value = sequence(spl_id, spl_type)
    return value

'''
    well, you can keep the item type as variable but for any "special case purpose", i defined all separately
'''


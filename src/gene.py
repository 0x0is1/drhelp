from soup import soup_collector
from name_collect import name_collector
## feature PART2
def feature_gene(spl_id, spl_type):
    def gene(spl_id_dup, spl_type_dup):
        soup = soup_collector(spl_id, spl_type)
        sample_info_name = name_collector(spl_id, spl_type)
        iterator = 0
        while True:
            gene = soup.find('span', {"id": "feature_" + sample_info_name + "_gene_" + str(iterator)})
            if gene == None:
                break
            print(gene.text)
            iterator += 1
    value = gene(spl_id, spl_type)
    return value

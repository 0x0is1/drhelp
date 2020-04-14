from soup import soup_collector
from name_collect import name_collector
#comment
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


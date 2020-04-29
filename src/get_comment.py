from soup import soup_collector
from name_collect import name_collector
#comment
def comment(spl_id, spl_type):
    soup = soup_collector(spl_id, spl_type)
    sample_info_name = name_collector(spl_id, spl_type)
    
    
    try:
        raw_intro = soup.find('a', {"href":'https://www.ncbi.nlm.nih.gov/RefSeq/'})
        intro7 = raw_intro.nextSibling
        intro6 = raw_intro.nextSibling.nextSibling
        #intro5 = raw_intro.nextSibling.nextSibling.nextSibling
        #intro4 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling
        #intro3 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling
        #intro2 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling
        #intro1 = raw_intro.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling
        intro = str(intro7) + str(intro6)
        return intro
    except:
        print('Oops something went wrong...')

from soup import soup_collector
from name_collect import name_collector
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

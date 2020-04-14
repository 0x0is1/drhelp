from soup import soup_collector
from name_collect import name_collector
from data_collect import data_collector
from formal import formal
from visualize import visualize
import os
from default import default_data
def main_function():

    formal()
    while True:
        raw_command = input("> ")

        try:
            command, details = raw_command.split(" ")
            print(command)
            print(details)

        except:
            command = raw_command
 
        cases = {0:"exit",1:"cls",2:"get",3:"help",4:"set",5:"visualize",6: "ftp",7: "show options"}

           ###############
        try:
            genefeature, slfeature, pfeature, cfeature, sofeature, comment = data_collector(str(default_data.sample_id), str(default_data.sample_type), str(default_data.report_type), str(default_data.doc_type))

        except:
            data, url = data_collector(str(default_data.sample_id), str(default_data.sample_type), str(default_data.report_type), str(default_data.doc_type))

        if command == None:
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
            visualize(url)                     

        else:
            os.system(command)
        

from soup import soup_collector
from name_collect import name_collector
from data_collect import data_collector
from formal import formal
from visualize import visualize
import os
import random
from default_data import default_data
user = 'user@'+str(random.randint(4000, 9999))+'> '
cases = {0:"exit",1:"cls",2:"get",3:"help",4:"set",5:"visualize",6: "ftp",7: "show options"}
containers = {1:"id=", 2:"type=", 3:"report=", 4:"doc="}
def main_function():
    formal()
    while True:
        command = list(map(str, input(user).split()))
        if command[0] == cases[4]:
            for i in range(4):
                for j in range(len(command)):
                    try:
                        if containers[i] in command[j]:
                            arg1 = command[j].split('=')
                            print(arg1[1])
                    except:
                            pass
                


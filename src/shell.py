from soup import soup_collector
from name_collect import name_collector
from data_collect import data_collector
from formal import formal
from visualize import visualize
import os
import random
from default_data import default_data
from options import *

user = 'user@'+str(random.randint(4000, 9999))+'> '


def get_det(command):
    info = data_collector(values[1], values[2], values[3], values[4], command)
    print(info)

def set_det(command):
    for i in range(1,5):
        for j in range(len(command)):
            try:
                if set_options[i] in command[j]:
                    arg1 = command[j].split('=')
                    values[i] = arg1[1]
            except:
                    pass

def check_fetch():
    print('TODO')

def main_function():
    formal()
    while True:
        command = list(map(str, input(user).split()))
        if command[0] == cases[4]:
            set_det(command)
            print(set_options)
            print(values)
        if command[0] == cases[0]:
            exit(0)
        if command[0] == cases[3]:
            print(cases)
        if command[0] == cases[1]:
            os.system('clear')
        if command[0] == cases[2]:
            try: 
                get_det(command[1]) 
            except: 
                print('args not provided') 
                pass
        if command[0] == cases[5]:
            print("todo")
        if command[0] == cases[6]:
            check_fetch()
        else:
            print()

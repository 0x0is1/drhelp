try:
    import requests
    from bs4 import BeautifulSoup as bs
    import os
    import time
    import argparse
    import sys
    from formal import formal
    from soup import soup_collector
    from name_collect import name_collector
except:
    print('Required dependecies might not be installed')
    print('install by typing "pip install -r requirements.txt"')

if __name__ == "__main__":
    #main()
    try:
        if sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print('BSFramework v0.2')
    except:
            formal()
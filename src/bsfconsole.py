import sys
from shell_manager import main_function

if __name__ == "__main__":
   #main()
    try:
        if sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print('BSFramework v0.2')
    except:
            main_function()
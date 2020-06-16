import sys
from shell_manager import main_function
from formal import formal
if __name__ == "__main__":
   #main()
    try:
        if sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print(formal())
            print('BSFramework v0.6')
        if sys.argv[1] == "--shell":
            main_function()
    except:
            print('Oops! Something went wrong!')
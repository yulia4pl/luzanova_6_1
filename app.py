#python3 app.py add 9 5
#python3 app.py sub 9 5
#python3 app.py mul 9 5

import sys

if __name__ == "__main__":

    try:
        if len(sys.argv) != 4:
            print(sys.argv)
            raise NameError("Enter 4 paramenrs: program name, command add/sub/mul, number1, number2")
        print(sys.argv)
       
        if (sys.argv[1] == "add"):
            print(int(sys.argv[2]) + int(sys.argv[3]))
        elif sys.argv[1] == "sub":
            print(int(sys.argv[2]) - int(sys.argv[3]))
        elif sys.argv[1] == "mul":
            print(int(sys.argv[2]) * int(sys.argv[3]))           
        else:
            print("Unknown command. It can be add/sub/mul.")                
    
    except Exception as err:
        print(err)
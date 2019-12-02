import sys
from .funcmodule import *
import PyInquirer
from examples import custom_style_1

def main():
    try:
        while True:
            clear()
            q = [
                {
                    'type': 'list',
                    'name': 'option',
                    'message': 'Choose your option below',
                    'choices': [
                        "Teachers login",
                        "Students login",
                        "Students Create Account",
                        "Exit"
                    ]
                }
            ]
            ans = PyInquirer.prompt(q, style=custom_style_1)

            if ans['option'] == "Teachers login":
                teacher_login()
                clear()

            elif ans['option'] == "Students login":
                std_login()
                clear()

            elif ans['option'] == "Students Create Account":
                new_user()
                clear()
            
            else:
                break
    
    except KeyError:
        pass

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
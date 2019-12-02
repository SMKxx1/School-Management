import pandas
import pymysql
import datetime
import hashlib
import sys
import os
import time
import platform 
import PyInquirer
import bcrypt
from termcolor import cprint
from pyfiglet import figlet_format as asci
from examples import custom_style_1, custom_style_2, custom_style_3
import random

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "1234",
    database = "sclmgt"
)

c = conn.cursor()

def encoder(password):
    password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    password = password.decode()
    return password

def std_code():
    salt = bcrypt.gensalt().decode()
    all_salt = pandas.read_sql("select std_code from students_account;", conn)
    while salt not in all_salt:
        salt = bcrypt.gensalt().decode()
    return salt

def student_verification(email):
    find_user = (f"select * from students_account where email like '{email}';")
    c.execute(find_user)
    try:
        a = tuple(tuple(c.fetchall())[0])[1]
    except IndexError:
        a = ""
    if a == email:
        return False
    else:
        return True

def students_pass_verify(email, password):
    c.execute(f"select password from students_account where email = '{email}';")
    check = tuple(c.fetchone())[0]
    return bcrypt.checkpw(password.encode(), check.encode())   

def teacher_verification(email):
    find_user = (f"select * from teachers_account where email like '{email}';")
    c.execute(find_user)
    try:
        a = tuple(tuple(c.fetchall())[0])[1]
    except IndexError:
        a = ""
    if a == email:
        return False
    else:
        return True

def teacher_pass_verify(email, password):
    c.execute(f"select password from teachers_account where email = '{email}';")
    check = tuple(c.fetchone())[0]
    return bcrypt.checkpw(password.encode(), check.encode())    

def new_user():
    clear()
    password = ''
    pass_again = ' '
    print("Press 'ctrl + c' to exit")
    try:
        while True:
            q = [
                {
                    'type':'input',
                    'name':'email',
                    'message':'Please enter a email: '
                }
            ]
            answer = PyInquirer.prompt(q, style=custom_style_1)
            email = answer['email']
            if student_verification(email) == False:
                print("Email already registered")
                input()
            else:
                break
        q = [
            {
                'type':'input',
                'name':'name',
                'message':'Enter your name: '
            },
            {
                'type':'input',
                'name':'CLASS',
                'message':'Enter your class: '
            },
            {
                'type':'input',
                'name':'sec',
                'message':'Enter your sec: '
            },
            {
                'type':'input',
                'name':'phone',
                'message':'Enter your phone: '
            },
        ]
        answer = PyInquirer.prompt(q, style=custom_style_1)
        name = answer['name']
        CLASS = answer['CLASS']
        sec = answer['sec']
        phone = answer['phone']
        while password != pass_again:
            q = [
                {
                    'type':'password',
                    'name':'password',
                    'message':'Enter your password: '
                },
                {
                    'type':'password',
                    'name':'pass_again',
                    'message':'Please re-enter your password: '
                }
            ]
            answer = PyInquirer.prompt(q, style=custom_style_1)
            password = answer['password']
            pass_again = answer['pass_again']
            if password != pass_again:
                print("Passwords did not match. Please try again.")
        pass_again = ' '
        password = encoder(password)
        command = f"insert into students_account values(NULL, '{email}', '{name}', '{CLASS}', '{sec}','{phone}','{password}', NULL, 0, NULL);"
        c.execute(command)
        print("User has been created")
        time.sleep(1)
        conn.commit()
    except KeyError:
        print()

    except KeyboardInterrupt:
        print()

def question_builder():
    try:
        q = [
            {
                'type':'checkbox',
                'qmark':'😃',
                'message': 'Select question types:',
                'name': 'question_types',
                'choices': [
                    {'name': 'One Word'},
                    {'name': 'MCQ'},
                    {'name': 'True or False'},
                    {'name': 'Para'}
                ]
            }
        ]
        answer = PyInquirer.prompt(q, style=custom_style_1)
        total_marks = 0
        questions = []

        if 'One Word' in answer['question_types']:
            # {'asdas': {'asd': '21'}, 'asdsA': {'zxc': '31'}}
            clear()
            cprint("One Word Questions", 'red')
            q = [
                {
                    'type':'input',
                    'name':'quantity',
                    'message': 'Enter the amount of questions: ',
                    'validate': lambda x: x.isdigit()
                }
            ]
            ans = PyInquirer.prompt(q, style=custom_style_1)
            one_word_questions = {}
            for i in range(1, int(ans['quantity']) + 1):
                
                q = [
                    {
                        'type':'input','name':'marks',
                        'message':f'Enter the marks for question no {i}:',
                        'validate': lambda x: x.isdigit()
                    }
                ]
                marks = PyInquirer.prompt(q, style=custom_style_1)
                
                q = [
                    {
                        'type':'input',
                        'name':'question',
                        'message':f'Enter the question:'
                    }
                ]
                ques = PyInquirer.prompt(q, style=custom_style_1)
                
                q = [
                    {
                        'type':'input',
                        'name':'answer',
                        'message':f'Enter the answer:'
                    }
                ]
                ans = PyInquirer.prompt(q, style=custom_style_1)
                
                dic = {ans['answer']: marks['marks']}
                one_word_questions[ques['question']] = dic

                total_marks += int(marks['marks'])
            questions.append({"One Word": one_word_questions})

        if 'MCQ' in answer['question_types']:
            # {'Q1': {'A1': {'marks': '2', 'choices': ['C1', 'C2']}}, 'Q2': {'A2': {'marks': '4', 'choices': ['C1', 'C2', 'C3']}}}
            clear()
            cprint("MCQ Questions", 'red')
            q = [
                {
                    'type':'input',
                    'name':'quantity',
                    'message': 'Enter the amount of questions: ',
                    'validate': lambda x: x.isdigit()
                }
            ]
            ans = PyInquirer.prompt(q, style=custom_style_1)
            MCQ_questions = {}
            for i in range(1, int(ans['quantity']) + 1):

                q = [
                    {
                        'type':'input',
                        'name':'marks',
                        'message':f'Enter the marks for question no {i}:',
                        'validate': lambda x: x.isdigit()
                    }
                ]
                marks = PyInquirer.prompt(q, style=custom_style_1)
                
                q = [
                    {
                        'type':'input',
                        'name':'question',
                        'message':f'Enter the question:'
                    }
                ]
                ques = PyInquirer.prompt(q, style=custom_style_1)

                q = [
                    {
                        'type':'input',
                        'name':'answer',
                        'message':f'Enter the answer:'
                    }
                ]
                ans = PyInquirer.prompt(q, style=custom_style_1)

                q = [
                    {
                        'type':'input',
                        'name':'choices',
                        'message':f'Enter the amount of choices:',
                        'validate': lambda x: x.isdigit()
                    }
                ]
                choice_no = PyInquirer.prompt(q, style=custom_style_1)
                choices = []
                for i in range(1, int(choice_no['choices']) + 1):
                    q = [
                        {
                            'type':'input',
                            'name':'choice',
                            'message':f'Enter the choice {i}:'
                        }
                    ]
                    choice = PyInquirer.prompt(q, style=custom_style_1)
                    choices.append(choice['choice'])
                
                dic = {str(ans['answer']): {'marks': marks['marks'], 'choices': choices}}
                MCQ_questions[ques['question']] = dic
                total_marks += int(marks['marks'])
            questions.append({"MCQ": MCQ_questions})
            
        if 'True or False' in answer['question_types']:
            # [{'Q1': {True: '1'}, 'Q2': {True: '1'}, 'Q3': {False: '3'}}]
            clear()
            cprint("True or False Questions", 'red')
            q = [
                {
                    'type':'input',
                    'name':'quantity',
                    'message': 'Enter the amount of questions:',
                    'validate': lambda x: x.isdigit()
                }
            ]
            ans = PyInquirer.prompt(q, style=custom_style_1)
            t_f_questions = {}
            for i in range(1, int(ans['quantity']) + 1):
                
                q = [
                    {
                        'type':'input',
                        'name':'marks',
                        'message':f'Enter the marks for question no {i}:',
                        'validate': lambda x: x.isdigit()
                    }
                ]
                marks = PyInquirer.prompt(q, style=custom_style_1)
                
                q = [
                    {
                        'type':'input',
                        'name':'question',
                        'message':f'Enter the question:'
                    }
                ]
                ques = PyInquirer.prompt(q, style=custom_style_1)
                
                q = [
                    {
                        'type':'confirm',
                        'name':'answer',
                        'message':f'Enter the answer:'
                    }
                ]
                ans = PyInquirer.prompt(q, style=custom_style_1)
                
                dic = {ans['answer']: marks['marks']}
                t_f_questions[ques['question']] = dic

                total_marks += int(marks['marks'])
            questions.append({"True or False": t_f_questions})

        if 'Para' in answer['question_types']:

            clear()
            cprint("Para Questions", 'red')
            q = [
                {
                    'type':'input',
                    'name':'quantity',
                    'message': 'Enter the amount of questions: ',
                    'validate': lambda x: x.isdigit()
                }
            ]
            ans = PyInquirer.prompt(q, style=custom_style_1)
            para_questions = {}
            for i in range(1, int(ans['quantity']) + 1):

                q = [
                    {
                        'type':'input',
                        'name':'marks',
                        'message':f'Enter the marks for question no {i}:',
                        'validate': lambda x: x.isdigit()
                    }
                ]
                marks = PyInquirer.prompt(q, style=custom_style_1)
                
                q = [
                    {
                        'type': 'editor',
                        'name': 'question',
                        'message': 'Please type the question',
                        'default': 'Please type the question Below',
                        'eargs': {
                            'editor': 'default',
                            'ext': '.py'
                        }
                    }
                ]
                ques = PyInquirer.prompt(q, style=custom_style_1)
                ques['question'] = ques['question'][31:]
                
                q = [
                    {
                        'type': 'input',
                        'name': 'quantity',
                        'message': 'Enter the amount of keywords:',
                        'validate': lambda x: x.isdigit()
                    }
                ]
                ans = PyInquirer.prompt(q, style=custom_style_1)

                keywords = []

                for i in range(1, int(ans['quantity']) + 1):
                    q = [
                        {
                            'type': 'input',
                            'name': 'keyword',
                            'message': f'Enter the keyword {i}:'
                        }
                    ]
                    kw = PyInquirer.prompt(q, style=custom_style_1)
                    keywords.append(kw['keyword'])


                dic = {'marks': marks['marks'], 'keywords': keywords}
                para_questions[ques['question']] = dic
                total_marks += int(marks['marks'])
            questions.append({"Para": para_questions})
        return questions, total_marks

    except KeyError:
        pass

def std_login():
    c = conn.cursor()
    try:
        while True:
            clear()
            q = [
                {
                    'type':'input',
                    'name':'email',
                    'message':'Please enter your email:',
                    'validate': lambda x: not student_verification(x)
                }
            ]

            ans = PyInquirer.prompt(q, style=custom_style_1)
            email = ans['email']

            q = [
                {
                    "type":"password",
                    "name":"password",
                    "message":"Please enter your password: "
                }
            ]
            answer = PyInquirer.prompt(q, style=custom_style_1)
            password = answer['password']
            c.execute(f"select password from students_account where email = '{email}';")
            check = tuple(c.fetchone())[0]
            if bcrypt.checkpw(password.encode(), check.encode()) == False:
                print("Invalid Username or Password. Try again")
                input()
            else:
                colores = ['red','blue','green','cyan','yellow','white']
                random_color = colores[random.randint(0,5)]
                cprint(asci('W e l c o m e B a c k ! ! !', '3-d'), random_color)
                c.execute(f"update students_account set log = log + 1 where email = '{email}';")
                conn.commit()
                input()
                clear()
                break

    except KeyboardInterrupt:
        clear()

def teacher_login():
    c = conn.cursor()
    try:
        while True:
            clear()
            q = [
                {
                    'type':'input',
                    'name':'email',
                    'message':'Please enter your email:',
                    'validate': lambda x: not teacher_verification(x)
                }
            ]

            ans = PyInquirer.prompt(q, style=custom_style_1)
            email = ans['email']

            q = [
                {
                    "type":"password",
                    "name":"password",
                    "message":"Please enter your password: ",
                    "validate": lambda x: teacher_pass_verify(email, x)
                }
            ]
            answer = PyInquirer.prompt(q, style=custom_style_1)
            password = answer['password']
            c.execute(f"select subject from teachers_account where email = '{email}';")
            subject = tuple(c.fetchone())[0]
            teacher_function(subject)
            input()
            clear()
            break

    except KeyboardInterrupt:
        clear()
    
    except KeyError:
        clear()

def teacher_function(subject):
    clear()
    colores = ['red','blue','green','cyan','yellow','white']
    random_color = colores[random.randint(0,5)]
    cprint(asci('W e l c o m e B a c k ! ! !', '3-d'), random_color)
    try:
        while True:
            q = [
                {
                    'type': 'list',
                    'name': 'option',
                    'message': 'Please choose your option below',
                    'choices': [
                        'Create questions',
                        'Check questions',
                        'See students performances',
                        'Exit'
                    ]
                }
            ]
            ans = PyInquirer.prompt(q, style=custom_style_1)
            
            if ans['option'] == 'Create questions':
                date = datetime.datetime.now()
                question, total_marks = question_builder()
                c.execute(f"""insert into questions values (NULL, '{subject}', "{question}", '{total_marks}', '{date}');""")
                conn.commit()
                clear()
            
            elif ans['option'] == 'Check questions':
                cprint("Yet to be coded...", "red")
                input()
                clear()
            
            elif ans['option'] == 'See students performances':
                cprint("Yet to be coded...", "red")
                input()
                clear()
            
            else:
                break

    except KeyboardInterrupt:
        pass

    except TypeError:
        pass

    except KeyError:
        pass
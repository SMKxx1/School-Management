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
from termcolor import colored
import pyfiglet
from examples import custom_style_1, custom_style_2, custom_style_3

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
            print(colored("One Word Questions", 'red'))
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
            print(colored("MCQ Questions", 'red'))
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
            print(colored("True or False Questions", 'red'))
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
            print(questions)

        if 'Para' in answer['question_types']:

            clear()
            print(colored("Para Questions", 'red'))
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
                            'message': 'Enter the keyword:'
                        }
                    ]
                    kw = PyInquirer.prompt(q, style=custom_style_1)
                    keywords.append(kw['keyword'])


                dic = {'marks': marks['marks'], 'keywords': keywords}
                para_questions[ques['question']] = dic
                total_marks += int(marks['marks'])
            questions.append({"Para": para_questions})
        print(questions)

    except KeyError:
        pass

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
            answer = PyInquirer.prompt(q)
            email = answer['email']
            if user_verification(email) == False:
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
        answer = PyInquirer.prompt(q)
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
            answer = PyInquirer.prompt(q)
            password = answer['password']
            pass_again = answer['pass_again']
            if password != pass_again:
                print("Passwords did not match. Please try again.")
        pass_again = ' '
        password = encoder(password)
        command = f"insert into students_account values(NULL, '{email}', '{name}', '{CLASS}', '{sec}','{phone}','{password}', NULL, 0);"
        c.execute(command)
        print("User has been created")
        time.sleep(1)
        conn.commit()
        conn.close()
    except KeyError:
        print()

    except KeyboardInterrupt:
        print()

def user_verification(email):
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

def std_login():
    c = conn.cursor()
    try:
        while True:
            clear()
            email = input("Please enter your email: ")
            if user_verification(email) == True:
                pass
            else:
                q = [
                    {
                        "type":"password",
                        "name":"password",
                        "message":"Please enter your password: "
                    }
                ]
                answer = PyInquirer.prompt(q)
                password = answer['password']
                c.execute(f"select password from students_account where email = '{email}';")
                check = tuple(c.fetchone())[0]
                if bcrypt.checkpw(password.encode(), check.encode()) == False:
                    print("Invalid Username or Password. Try again")
                    input()
                else:
                    print("You are Logged In!!!")
                    c.execute(f"update students_account set log = log + 1 where email = '{email}';")
                    conn.commit()
                    input()
                    clear()
                    break

    except KeyboardInterrupt:
        clear()
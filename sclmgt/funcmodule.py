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
from tabulate import tabulate
import matplotlib.pyplot as plt

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


def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


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
                'name':'phone',
                'message':'Enter your phone: '
            },
        ]
        answer = PyInquirer.prompt(q, style=custom_style_1)
        name = answer['name']
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
        command = f"insert into students_account values(NULL, '{email}', '{name}','{phone}','{password}', NULL, 0, NULL);"
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
        questions = {}
        if answer['question_types'] != []:
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
                if int(ans['quantity']) != 0:
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
                    questions["One Word"] = one_word_questions

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
                if int(ans['quantity']) != 0:
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
                    questions["MCQ"] = MCQ_questions
                
            if 'True or False' in answer['question_types']:
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
                if int(ans['quantity']) != 0:
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
                    questions["True or False"] = t_f_questions

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
                if int(ans['quantity']) != 0:
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
                    questions["Para"] = para_questions
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
                clear()
                colores = ['red','blue','green','cyan','yellow','white']
                random_color = colores[random.randint(0,5)]
                cprint(asci('W e l c o m e B a c k ! ! !', '3-d'), random_color)
                c.execute(f"UPDATE students_account set log = log + 1 where email = '{email}';")
                conn.commit()
                c.execute(f"SELECT name from students_account where email = '{email}'")
                name = c.fetchone()[0]
                std_function(email, name)
                clear()
                break

    except KeyboardInterrupt:
        clear()


def std_function(email, name):
    try:
        while True:
            q = [
                {
                    'type': 'list',
                    'name': 'options',
                    'message': 'Please choose your option below',
                    'choices': [
                        'Check Questions',
                        'Take a Test',
                        'See previous Reports',
                        'Logout'
                    ]
                }
            ]
            answer = PyInquirer.prompt(q, style = custom_style_1)
            
            if answer['options'] == 'Check Questions':

                df = pandas.read_sql("SELECT subject, count(*) from questions GROUP BY subject;", conn)
                print(tabulate(df, headers = ['Subjects', 'Number or Tests'], tablefmt='fancy_grid', showindex = False))
                input()
                clear()

            elif answer['options'] == 'Take a Test':

                q = [
                    {
                        'type': 'list',
                        'name': 'options',
                        'message': 'Please choose your Subject',
                        'choices': [
                            'English',
                            'Maths',
                            'Social',
                            'Computers',
                            'Business'
                        ]
                    }
                ]

                answer = PyInquirer.prompt(q, style = custom_style_1)
                question_paper(answer['options'], email, name)
            
            elif answer['options'] == 'See previous Reports':
                df = pandas.read_sql(f"SELECT * from marks where email = '{email}'", conn)
                df2 = pandas.DataFrame(columns=['id','date_time','name','email','subject','report','marks'])
                q = [
                    {
                        'type': 'checkbox',
                        'qmark': '😃',
                        'name': 'subjects',
                        'message': 'Please choose your Subject',
                        'choices': [
                            {'name': 'English'},
                            {'name': 'Maths'},
                            {'name': 'Social'},
                            {'name': 'Computers'},
                            {'name': 'Business'}
                        ]
                    }
                ]
                answer = PyInquirer.prompt(q, style = custom_style_1)
                if 'Computers' in answer['subjects']:
                    if 'Computers' in df['subject'].to_string():
                        df2 = df2.append(df[df['subject'] == 'Computers'], ignore_index=True, sort=False)
                
                if 'Maths' in answer['subjects']:
                    if 'Maths' in df['subject'].to_string():
                        df2 = df2.append(df[df['subject'] == 'Maths'], ignore_index=True, sort=False)
                
                if 'English' in answer['subjects']:
                    if 'English' in df['subject'].to_string():
                        df2 = df2.append(df[df['subject'] == 'English'], ignore_index=True, sort=False)
                
                if 'Social' in answer['subjects']:
                    if 'Social' in df['subject'].to_string():
                        df2 = df2.append(df[df['subject'] == 'Social'], ignore_index=True, sort=False)
                
                if 'Business' in answer['subjects']:
                    if 'Business' in df['subject'].to_string():
                        df2 = df2.append(df[df['subject'] == 'Business'], ignore_index=True, sort=False)

                for i in df2['report']:
                    i = eval(i)
                    report_card(i)



            elif answer['options'] == 'Logout':
                break
    
    except KeyboardInterrupt:
        pass


def question_paper(subject, email, name):
    paper = pandas.read_sql(f"SELECT * FROM questions WHERE subject = '{subject}';", conn)

    if len(paper) == 0:
        print("No Tests available")

    else:
        paper = pandas.read_sql(f"SELECT * FROM questions WHERE subject = '{subject}';", conn)
        lst = []
        for i in range(len(paper)):
            a = tabulate(paper.loc[i:i, ['id', 'total_marks', 'date_time']],showindex=True, tablefmt='plain')
            a = a.split('  ')
            a = "{0:>3}    {1:>11}    {2:>26}".format(a[0], a[2], a[3])
            lst.append(a)
        q = [
            {
                'type':'list',
                'name':'question paper',
                'message':" {0:>3}    {1:>11}    {2:>26}".format("ID", "Total Marks", "Date and Time"),
                'choices': lst
            }
        ]

        ans = PyInquirer.prompt(q, style = custom_style_1)
        idx = int((ans['question paper'])[:10])
        question = eval(paper.loc[idx]['question'])
        check_dic = {}
        marks = 0
        q_dic = {'One Word': False, 'MCQ': False, 'True or False': False, 'Para': False}
        lis = ['One Word', 'MCQ', 'True or False', 'Para']

        for f in question:
            for i in lis:
                if i in f:
                    q_dic[i] = True

        if q_dic['One Word'] == True:
            check_dic['One Word'] = {}
            if question.__class__ == tuple:
                one_word = question[0]['One Word']
            else:
                one_word = question['One Word']
            for i in one_word:
                q = [
                    {
                        'type': 'input',
                        'name': 'ans',
                        'message': i
                    }
                ]
                answer = PyInquirer.prompt(q, style = custom_style_1)
                a = str(one_word[i].keys())[12:-3]
                if answer['ans'].lower() == a.lower():
                    if question.__class__ == tuple:
                        marks += int(question[0]['One Word'][i][a])
                        check_dic['One Word'][i] = [True, int(question[0]['One Word'][i][a])]
                    else:
                        marks += int(question['One Word'][i][a])
                        check_dic['One Word'][i] = [True, int(question['One Word'][i][a])]

                else:
                    if question.__class__ == tuple:
                        check_dic['One Word'][i] = [False, int(question[0]['One Word'][i][a])]
                    else:
                        check_dic['One Word'][i] = [False, int(question['One Word'][i][a])]
                
        if q_dic['MCQ'] == True:
            check_dic['MCQ'] = {}
            if question.__class__ == tuple:
                mcq = question[1]['MCQ']
            else:
                mcq = question['MCQ']

            for i1 in mcq:    
                for i2 in mcq[i1]:
                    correct_answer = i2
                    temporary_list = []
                    for i3 in mcq[i1][i2]:
                        temporary_list.append(mcq[i1][i2][i3])
                    questions_marks, choices = int(temporary_list[0]), temporary_list[1]
                
                choices.append(correct_answer)
                choices = scrambled(choices)

                q = [
                    {
                        'type': 'list',
                        'name': 'ans',
                        'message': i1,
                        'choices': choices
                    }
                ]
                answer = PyInquirer.prompt(q, style = custom_style_1)
                if answer['ans'] == correct_answer:
                    marks += questions_marks
                    check_dic['MCQ'][i1] = [True, questions_marks]
                else:
                    check_dic['MCQ'][i1] = [False, questions_marks]
            
        if q_dic['True or False'] == True:
            check_dic['True or False'] = {}
            if question.__class__ == tuple:
                tf = question[2]['True or False']
            else:
                tf = question['True or False']
            
            for i1 in tf:
                for i2 in tf[i1]:
                    correct_answer = i2
                    temporary_marks = int(tf[i1][i2])
                
                q = [
                    {
                        'type': 'confirm',
                        'name': 'ans',
                        'message': i1,
                    }
                ]
                answer = PyInquirer.prompt(q, style = custom_style_1)
                if answer['ans'] == correct_answer:
                    marks += temporary_marks
                    check_dic['True or False'][i1] = [True, temporary_marks]
                else:
                    check_dic['True or False'][i1] = [False, temporary_marks]
        
        if q_dic['Para'] == True:
            check_dic['Para'] = {}
            if question.__class__ == tuple:
                para = question[3]['Para']
            else:
                para = question['Para']

            for i1 in para:
                temporary_marks = int(para[i1]['marks'])
                keywords = para[i1]['keywords']

                q = [
                    {
                        'type': 'editor',
                        'name': 'ans',
                        'message': i1,
                        'default': i1,
                        'eargs': {
                            'editor':'default',
                            'ext':'.py'
                        }
                    }
                ]

                answer = PyInquirer.prompt(q, style = custom_style_1)
                answer['ans'] = answer['ans'][(len(i1) + 1):]

                correct = True

                for i in keywords:
                    if i.lower() not in answer['ans'].lower():
                        correct = False
                
                if correct == True:
                    marks += temporary_marks
                    check_dic['Para'][i1] = [True, temporary_marks]
                else:
                    check_dic['Para'][i1] = [False, temporary_marks]

        date = datetime.datetime.now()
        check_dic['Total Marks'] = marks
        c.execute(f"""INSERT INTO marks values (Null, '{date}', '{name}','{email}', "{subject}", "{check_dic}", {marks});""")
        conn.commit()
        report_card(check_dic)


def report_card(check_dic):
    marks = check_dic['Total Marks']
    del check_dic['Total Marks']
    df_dic = {}
    questions = []
    marks_earned = []
    correct = []
    question_type = []
    total_marks = 0
    correct_count = 0
    total_correct = 0
    
    for i1 in check_dic:
        for i2 in check_dic[i1]:
            question_type.append(i1)
            questions.append(i2)
            if check_dic[i1][i2][0] == True:
                marks_earned.append(int(check_dic[i1][i2][1]))
                correct.append("Correct")
                correct_count += 1 
            else:
                marks_earned.append(0)
                correct.append("Wrong")
            total_correct += 1
            total_marks += int(check_dic[i1][i2][1])
    
    df = pandas.DataFrame({"Questions": questions, "Type": question_type, "Correct / Wrong": correct, "Marks Earned": marks_earned})
    footer = {"Questions": "Total", "Type": "","Correct / Wrong": f"{correct_count} / {total_correct}", "Marks Earned": f"{marks} / {total_marks}"}
    df = df.append(footer, ignore_index = True, sort = False)
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    graph(marks, total_marks)


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
                        'See students performances',
                        'Logout'
                    ]
                }
            ]
            ans = PyInquirer.prompt(q, style=custom_style_1)
            
            if ans['option'] == 'Create questions':
                date = datetime.datetime.now()
                try:
                    question, total_marks = question_builder()
                    c.execute(f"""insert into questions values (NULL, '{subject}', "{question}", '{total_marks}', '{date}');""")
                    conn.commit()
                except:
                    pass
                clear()
            
            elif ans['option'] == 'See students performances':
                df = pandas.read_sql(f"SELECT * from marks where subject = '{subject}';", conn)
                for i, f in zip(df['report'], df['name']):
                    i = eval(i)
                    print(f)
                    report_card(i)
                
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

def graph(marks, total_marks):
    wrong = total_marks - marks
    plt.pie([wrong, marks], explode=[0.3,0], labels=['Wrong', 'Correct'], autopct='%0.0f%%', colors=['r','g'])
    font = {'family': 'serif',
        'color':  'k',
        'weight': 'normal',
        'size': 16,
        }
    plt.title(f"Marks scored: {marks} out of {total_marks}", fontdict=font)
    plt.show()
    
# import win32.win32clipboard as wc
# import os
# import time

# clear = lambda: os.system('cls')
# while True:
#     wc.OpenClipboard()
#     a = wc.GetClipboardData()
#     l = []
#     for i in a:
#         if i.isdigit():
#             l.append(i)
#     print(round((int(''.join(l)) * 52.57 / 100000),2))
#     wc.CloseClipboard()
#     time.sleep(0.5)
#     clear()

# [{'One Word': {'Who is the ceo of apple?': {'tim cook': '2'}, 'Name the co-founder of apple': {'steve paul jobs': '1'}}}, 
# {'MCQ': {'Who made the iphone?': {'Apple': {'marks': '4', 'choices': ['Samsung', 'Sony', 'Google']}}}}, 
# {'True or False': {'Iphone runs iOS': {True: '1'}}}, 
# {'Para': {'Write a short note on Steve Paul Jobs': {'marks': '5', 'keywords': ['Drop out', 'Apple', 'Next', 'iPhone', 'Mac']}}}]
# import pandas
# import pymysql
# import datetime
# import hashlib
# import sys
# import os
# import time
# import platform 
# import PyInquirer
# import bcrypt
# from termcolor import cprint
# from pyfiglet import figlet_format as asci
# from examples import custom_style_1, custom_style_2, custom_style_3
# import random
# from tabulate import tabulate
# import ast

# conn = pymysql.connect(
#     host = "localhost",
#     port = 3306,
#     user = "root",
#     passwd = "1234",
#     database = "sclmgt"
# )

# tdic = {'hello': 'hi'}

# c = conn.cursor()

# subject = "Computers"

# def scrambled(orig):
#     dest = orig[:]
#     random.shuffle(dest)
#     return dest

# def report_card(check_dic, marks):
#     df_dic = {}
#     questions = []
#     marks_earned = []
#     correct = []
#     question_type = []
#     total_marks = 0
#     correct_count = 0
#     total_correct = 0
    
#     for i1 in check_dic:
#         for i2 in check_dic[i1]:
#             question_type.append(i1)
#             questions.append(i2)
#             if check_dic[i1][i2][0] == True:
#                 marks_earned.append(int(check_dic[i1][i2][1]))
#                 correct.append("Correct")
#                 correct_count += 1 
#             else:
#                 marks_earned.append(0)
#                 correct.append("Wrong")
#             total_correct += 1
#             total_marks += int(check_dic[i1][i2][1])
    
#     df = pandas.DataFrame({"Questions": questions, "Type": question_type, "Correct / Wrong": correct, "Marks Earned": marks_earned})
#     footer = {"Questions": "Total", "Type": "","Correct / Wrong": f"{correct_count} / {total_correct}", "Marks Earned": f"{marks} / {total_marks}"}
#     df = df.append(footer, ignore_index = True, sort = False)
#     print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

# def std_function(email):
#     try:
#         while True:
#             q = [
#                 {
#                     'type': 'list',
#                     'name': 'options',
#                     'message': 'Please choose your option below',
#                     'choices': [
#                         'Check Questions',
#                         'Take a Test',
#                         'See previous Reports',
#                         'Logout'
#                     ]
#                 }
#             ]
#             answer = PyInquirer.prompt(q, style = custom_style_1)
            
#             if answer['options'] == 'Check Questions':

#                 df = pandas.read_sql("SELECT subject, count(*) from questions GROUP BY subject;", conn)
#                 print(tabulate(df, headers = ['Subjects', 'Number or Tests'], tablefmt='fancy_grid', showindex = False))
#                 input()

#             elif answer['options'] == 'Take a Test':

#                 q = [
#                     {
#                         'type': 'list',
#                         'name': 'options',
#                         'message': 'Please choose your Subject',
#                         'choices': [
#                             'English',
#                             'Maths',
#                             'Social',
#                             'Computers',
#                             'Business'
#                         ]
#                     }
#                 ]

#                 answer = PyInquirer.prompt(q, style = custom_style_1)
            
#             elif answer['options'] == 'See previous Reports':
#                 df = pandas.read_sql(f"SELECT * from marks where email = '{email}'", conn)
#                 df2 = pandas.DataFrame(columns=['id','date_time','email','subject','report','marks'])
#                 q = [
#                     {
#                         'type': 'checkbox',
#                         'qmark': '😃',
#                         'name': 'subjects',
#                         'message': 'Please choose your Subject',
#                         'choices': [
#                             {'name': 'English'},
#                             {'name': 'Maths'},
#                             {'name': 'Social'},
#                             {'name': 'Computers'},
#                             {'name': 'Business'}
#                         ]
#                     }
#                 ]
#                 answer = PyInquirer.prompt(q, style = custom_style_1)
#                 if 'Computers' in answer['subjects']:
#                     if 'Computers' in df['subject'].to_string():
#                         df2 = df2.append(df[df['subject'] == 'Computers'], ignore_index=True, sort=False)
                
#                 if 'Maths' in answer['subjects']:
#                     if 'Maths' in df['subject'].to_string():
#                         df2 = df2.append(df[df['subject'] == 'Maths'], ignore_index=True, sort=False)
                
#                 if 'English' in answer['subjects']:
#                     if 'English' in df['subject'].to_string():
#                         df2 = df2.append(df[df['subject'] == 'English'], ignore_index=True, sort=False)
                
#                 if 'Social' in answer['subjects']:
#                     if 'Social' in df['subject'].to_string():
#                         df2 = df2.append(df[df['subject'] == 'Social'], ignore_index=True, sort=False)
                
#                 if 'Business' in answer['subjects']:
#                     if 'Business' in df['subject'].to_string():
#                         df2 = df2.append(df[df['subject'] == 'Business'], ignore_index=True, sort=False)

#                 for i in df2['report']:
#                     i = eval(i)
#                     report_card(i, 13)
                        

#             elif answer['options'] == 'Logout':
#                 break
    
#     except KeyError:
#         pass

# # std_function("shahad.mustafa003@gmail.com")
# c.execute(f"SELECT name from students_account where email = 'shahad.mustafa003@gmail.com'")
# name = c.fetchone()[0]
# print(name)

# def qpp():
#     paper = pandas.read_sql(f"SELECT * FROM questions WHERE subject = '{subject}';", conn)
#     if len(paper) == 0:
#         print("No question papers made")
#     else:
#         paper = pandas.read_sql(f"SELECT * FROM questions WHERE subject = '{subject}';", conn)
#         lst = []
#         for i in range(len(paper)):
#             a = tabulate(paper.loc[i:i, ['id', 'total_marks', 'date_time']],showindex=True, tablefmt='plain')
#             a = a.split('  ')
#             a = "{0:>3}    {1:>11}    {2:>26}".format(a[0], a[2], a[3])
#             lst.append(a)
#         q = [
#             {
#                 'type':'list',
#                 'name':'question paper',
#                 'message':" {0:>3}    {1:>11}    {2:>26}".format("ID", "Total Marks", "Date and Time"),
#                 'choices': lst
#             }
#         ]
#         ans = PyInquirer.prompt(q, style = custom_style_1)
#         idx = int((ans['question paper'])[:10])
#         question = eval(paper.loc[idx]['question'])
#         check_dic = {}
#         marks = 0
#         q_dic = {'One Word': False, 'MCQ': False, 'True or False': False, 'Para': False}
#         lis = ['One Word', 'MCQ', 'True or False', 'Para']
#         for f in question:
#             for i in lis:
#                 if i in f:
#                     q_dic[i] = True
#         if q_dic['One Word'] == True:
#             check_dic['One Word'] = {}
#             if question.__class__ == tuple:
#                 one_word = question[0]['One Word']
#             else:
#                 one_word = question['One Word']
#             for i in one_word:
#                 q = [
#                     {
#                         'type': 'input',
#                         'name': 'ans',
#                         'message': i
#                     }
#                 ]
#                 answer = PyInquirer.prompt(q, style = custom_style_1)
#                 a = str(one_word[i].keys())[12:-3]
#                 if answer['ans'].lower() == a.lower():
#                     if question.__class__ == tuple:
#                         marks += int(question[0]['One Word'][i][a])
#                         check_dic['One Word'][i] = [True, int(question[0]['One Word'][i][a])]
#                     else:
#                         marks += int(question['One Word'][i][a])
#                         check_dic['One Word'][i] = [True, int(question['One Word'][i][a])]

#                 else:
#                     if question.__class__ == tuple:
#                         check_dic['One Word'][i] = [False, int(question[0]['One Word'][i][a])]
#                     else:
#                         check_dic['One Word'][i] = [False, int(question['One Word'][i][a])]                  
    
#         if q_dic['MCQ'] == True:
#             check_dic['MCQ'] = {}
#             if question.__class__ == tuple:
#                 mcq = question[1]['MCQ']
#             else:
#                 mcq = question['MCQ']

#             for i1 in mcq:    
#                 for i2 in mcq[i1]:
#                     correct_answer = i2
#                     temporary_list = []
#                     for i3 in mcq[i1][i2]:
#                         temporary_list.append(mcq[i1][i2][i3])
#                     questions_marks, choices = int(temporary_list[0]), temporary_list[1]
                
#                 choices.append(correct_answer)
#                 choices = scrambled(choices)

#                 q = [
#                     {
#                         'type': 'list',
#                         'name': 'ans',
#                         'message': i1,
#                         'choices': choices
#                     }
#                 ]
#                 answer = PyInquirer.prompt(q, style = custom_style_1)
#                 if answer['ans'] == correct_answer:
#                     marks += questions_marks
#                     check_dic['MCQ'][i1] = [True, questions_marks]
#                 else:
#                     check_dic['MCQ'][i1] = [False, questions_marks]

#         if q_dic['True or False'] == True:
#             check_dic['True or False'] = {}
#             if question.__class__ == tuple:
#                 tf = question[2]['True or False']
#             else:
#                 tf = question['True or False']
            
#             for i1 in tf:
#                 for i2 in tf[i1]:
#                     correct_answer = i2
#                     temporary_marks = int(tf[i1][i2])
                
#                 q = [
#                     {
#                         'type': 'confirm',
#                         'name': 'ans',
#                         'message': i1,
#                     }
#                 ]
#                 answer = PyInquirer.prompt(q, style = custom_style_1)
#                 if answer['ans'] == correct_answer:
#                     marks += temporary_marks
#                     check_dic['True or False'][i1] = [True, temporary_marks]
#                 else:
#                     check_dic['True or False'][i1] = [False, temporary_marks] 

#         if q_dic['Para'] == True:
#             check_dic['Para'] = {}
#             if question.__class__ == tuple:
#                 para = question[3]['Para']
#             else:
#                 para = question['Para']

#             for i1 in para:
#                 temporary_marks = int(para[i1]['marks'])
#                 keywords = para[i1]['keywords']

#                 q = [
#                     {
#                         'type': 'editor',
#                         'name': 'ans',
#                         'message': i1,
#                         'default': i1,
#                         'eargs': {
#                             'editor':'default',
#                             'ext':'.py'
#                         }
#                     }
#                 ]

#                 answer = PyInquirer.prompt(q, style = custom_style_1)
#                 answer['ans'] = answer['ans'][(len(i1) + 1):]

#                 correct = True

#                 for i in keywords:
#                     if i.lower() not in answer['ans'].lower():
#                         correct = False
                
#                 if correct == True:
#                     marks += temporary_marks
#                     check_dic['Para'][i1] = [True, temporary_marks]
#                 else:
#                     check_dic['Para'][i1] = [False, temporary_marks]

# report_card({'One Word': {'Who is the ceo of apple?': [True, 2], 'Name the co-founder of apple': [False, 1]}, 'MCQ': {'Who made the iphone?': [False, 4]}, 'True or False': {'Iphone runs iOS': [True, 1]}, 'Para': {'Write a short note on Steve Paul Jobs': [True, 5]}}, 8)

# {'One Word': {'Who is the ceo of apple?': [True, 2], 'Name the co-founder of apple': [False, 1]}, 
# 'MCQ': {'Who made the iphone?': [False, 4]}, 
# 'True or False': {'Iphone runs iOS': [True, 1]}, 
# 'Para': {'Write a short note on Steve Paul Jobs': [True, 5]}}


# {'One Word': {'Who is the ceo of apple?': {'tim cook': '2'}, 'Name the co-founder of apple': {'steve paul jobs': '1'}}}, 
# {'MCQ': {'Who made the iphone?': {'Apple': {'marks': '4', 'choices': ['Samsung', 'Sony', 'Google']}}}}, 
# {'True or False': {'Iphone runs iOS': {True: '1'}}}, 
# {'Para': {'Write a short note on Steve Paul Jobs': {'marks': '5', 'keywords': ['Drop out', 'Apple', 'Next', 'iPhone', 'Mac']}}}

# paper = pandas.read_sql(f"SELECT * FROM questions WHERE subject = '{subject}';", conn)

# lst = []

# for i in range(len(paper)):
#     a = tabulate(paper.loc[i:i, ['id', 'total_marks', 'date_time']],showindex=True, tablefmt='plain')
#     a = a.split('  ')
#     a = str("{0:>3}    {1:>11}    {2:>26}".format(a[0], a[2], a[3]))
#     lst.append(a)

# q = [
#     {
#         'type':'list',
#         'name':'question paper',
#         'message':" {0:>3}    {1:>11}    {2:>26}".format("ID", "Total Marks", "Date and Time"),
#         'choices': lst
#     }
# ]
# ans = PyInquirer.prompt(q)

# a = str(ans['question paper'])
# a = a[4]
# print(a)
# question = eval(paper.loc[0]['question'])
# print(question)
# q_dic = {'One Word': False, 'MCQ': False, 'True or False': False, 'Para': False}
# lis = ['One Word', 'MCQ', 'True or False', 'Para']

# for f in question:
#     for i in lis:
#         if i in f:
#             q_dic[i] = True

# print(q_dic)

# t_dic = {'One Word': {'Who is the ceo of apple?': {'tim cook': '2'}, 'Name the co-founder of apple': {'steve paul jobs': '1'}}}

# print(question[0]['One Word'])

# q = [
#     {
#         'type':'checkbox',
#         'qmark':'😃',
#         'message': 'Select question types:',
#         'name': 'question_types',
#         'choices': [
#             {'name': 'One Word'},
#             {'name': 'MCQ'},
#             {'name': 'True or False'},
#             {'name': 'Para'}
#         ]
#     }
# ]
# answer = PyInquirer.prompt(q, style=custom_style_1)
# questions = {}
# if answer['question_types'] == []:
#     print("sucess")

# else:
#     print(answer)

# try:
#     a = input()
#     print(a)
# except:  
#     print('hello')
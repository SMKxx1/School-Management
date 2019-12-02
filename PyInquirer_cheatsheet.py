# -*- coding: utf-8 -*-
"""
* Editor prompt example
"""
import PyInquirer
from examples import custom_style_2, custom_style_1, custom_style_3

# checkbox
# questions = [
#     {
#         'type': 'checkbox',
#         'qmark': '😃',
#         'message': 'Select toppings',
#         'name': 'toppings',
#         'choices': [ 
#             {
#                 'name': 'Ham'
#             },
#             {
#                 'name': 'Ground Meat'
#             },
#             {
#                 'name': 'Bacon'
#             },
#             {
#                 'name': 'Mozzarella',
#                 'checked': True
#             },
#             {
#                 'name': 'Cheddar'
#             },
#             {
#                 'name': 'Parmesan'
#             },
#             {
#                 'name': 'Mushroom'
#             },
#             {
#                 'name': 'Tomato'
#             },
#             {
#                 'name': 'Pepperoni'
#             },
#             {
#                 'name': 'Pineapple'
#             },
#             {
#                 'name': 'Olives',
#                 'disabled': 'out of stock'
#             },
#             {
#                 'name': 'Extra cheese'
#             }
#         ],
#     }
# ]

# rawlist
# questions = [
#     {
#         'type': 'rawlist',
#         'name': 'theme',
#         'message': 'What do you want to do?',
#         'choices': [
#             'Order a pizza',
#             'Make a reservation',
#             'Ask opening hours',
#             'Talk to the receptionist'
#         ]
#     },
#     {
#         'type': 'rawlist',
#         'name': 'size',
#         'message': 'What size do you need',
#         'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#         'filter': lambda val: val.lower()
#     }
# ]

# expand
# questions = [
#     {
#         'type': 'expand',
#         'message': 'Conflict on `file.js`: ',
#         'name': 'overwrite',
#         'default': 'a',
#         'choices': [
#             {
#                 'key': 'y',
#                 'name': 'Overwrite',
#                 'value': 'overwrite'
#             },
#             {
#                 'key': 'a',
#                 'name': 'Overwrite this one and all next',
#                 'value': 'overwrite_all'
#             },
#             {
#                 'key': 'd',
#                 'name': 'Show diff',
#                 'value': 'diff'
#             },
#             PyInquirer.Separator(),
#             {
#                 'key': 'x',
#                 'name': 'Abort',
#                 'value': 'abort'
#             }
#         ]
#     }
# ]

# when
# questions = [
#     {
#         'type': 'confirm',
#         'name': 'bacon',
#         'message': 'Do you like bacon?'
#     },
#     {
#         'type': 'input',
#         'name': 'favorite',
#         'message': 'Bacon lover, what is your favorite type of bacon?',
#         'when': lambda answers: answers['bacon']
#     },
#     {
#         'type': 'confirm',
#         'name': 'pizza',
#         'message': 'Ok... Do you like pizza?',
#         'default': False,  # only for demo :)
#         'when': lambda answers: not answers['bacon']
#     },
#     {
#         'type': 'input',
#         'name': 'favorite',
#         'message': 'Whew! What is your favorite type of pizza?',
#         'when': lambda answers: answers.get('pizza', False)
#     }
# ]


# List
# def get_delivery_options(answers):
#     options = ['bike', 'car', 'truck']
#     if 'size' in answers:
#         if answers['size'] == 'jumbo':
#             options.append('helicopter')
#     return options


# questions = [
#     {
#         'type': 'list',
#         'name': 'theme',
#         'message': 'What do you want to do?',
#         'choices': [
#             'Order a pizza',
#             'Make a reservation',
#             PyInquirer.Separator(),
#             'Ask for opening hours',
#             {
#                 'name': 'Contact support',
#                 'disabled': 'Unavailable at this time'
#             },
#             'Talk to the receptionist'
#         ]
#     },
#     {
#         'type': 'list',
#         'name': 'size',
#         'message': 'What size do you need?',
#         'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#         'filter': lambda val: val.lower(),
#         'when': lambda answers: answers['theme'] == 'Order a pizza'
#     },
#     {
#         'type': 'list',
#         'name': 'delivery',
#         'message': 'Which vehicle you want to use for delivery?',
#         'when': lambda answers: answers['theme'] == 'Order a pizza',
#         'choices': get_delivery_options
#     },
# ]

# questions = [
#     {
#         'type': 'editor',
#         'name': 'bio',
#         'message': 'Please write a short bio of at least 3 lines.',
#         'default': 'Hello World',
#         'eargs': {
#             'editor':'default',
#             'ext':'.py'
#         }
#     }
# ]

questions = [
                    {
                        'type': 'input',
                        'name': 'keywords',
                        'message': 'Enter the amount of keywords',
                        'validate': lambda x: x.isdigit()
                    }
                ]

answers = PyInquirer.prompt(questions, style=custom_style_3)
print(answers)
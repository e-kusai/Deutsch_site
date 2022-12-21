import dash

import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import Input, Output, State, callback

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("На главную", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Урок 1", href="/pages/lesson1"),
                dbc.DropdownMenuItem("Урок 2", href="/pages/lesson2"),
            ],
            nav=True,
            in_navbar=True,
            label="Теория ",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Урок 1", href="#"),
                dbc.DropdownMenuItem("Урок 2", href="/pages/test2"),
            ],
            nav=True,
            in_navbar=True,
            label="Практика ",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Текст 1", href="/pages/text1"),
                dbc.DropdownMenuItem("Текст 2", href="/pages/text2"),
            ],
            nav=True,
            in_navbar=True,
            label="Тексты ",
        ),


    ],
    brand="Практика: урок 1",
    brand_href="#",
    color="primary",
    dark=True,
)
  


task1=html.Div(
    [
        dcc.Markdown('''
            #### № 1: заполните пропуски
            ____ Stuhl  und ____ Tasche

        '''),
         dbc.RadioItems(
            options=[
                {"label": "das, die", "value": 1},
                {"label": "das, der", "value": 2},
                {"label": "der, das", "value": 3},
                {"label": "der, die", "value": 4},
            ],
            value=0,
            id="task01",
        ),
        ],
        style={'margin-bottom':'20px'}
    )

task2=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 2: Найдите предложение с ошибкой
        '''),
        dbc.RadioItems(
            options=[
                {"label": "Sie ist gut", "value": 1},
                {"label": "Der Stuhle sind braun", "value": 2},
                {"label": "Ich bin Student", 'value': 3},
                {"label": "Das ist eine Lampe", "value": 4},
            ],
            value=0,
            id="task02",
        ),
        ] ,
        style={'margin-bottom':'20px'}
    )

task3=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 3: Заполните пропуски
            Ihr ____ schön und wir ____ groß
        '''),
        dbc.RadioItems(
            options=[
                {"label": "seid, sind", "value": 1},
                {"label": "sind, sind", "value": 2},
                {"label": "bist, seid", 'value': 3},
                {"label": "sind, seid", "value": 4},
            ],
            value=0,
            id="task03",
        ),
        ] ,
        style={'margin-bottom':'20px'}
    )


task4=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 4: Продолжите предложение
            Das Kind ist ___
        '''),
        dbc.Checklist(
            options=[
                {"label": "alt", "value": 1},
                {"label": "gelb", "value": 2},
                {"label": "klein", 'value': 3},
                {"label": "schlecht", "value": 4},
            ],
            value=[],
            id="task04",
        ),
        ] ,
        style={'margin-bottom':'20px'}
    )

task5=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 5: Переведите на немецкий язык
            Этот цветок красный
        '''),
        dbc.Input(id="task05", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ] ,
        style={'margin-bottom':'20px'}
    )

task6=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 6: Переведите на немецкий язык
            Это ваза. Ваза желтая.
        '''),
        dbc.Input(id="task06", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ] ,
        style={'margin-bottom':'20px'}
    )

task7=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 7: Переведите на немецкий язык
            Это моя книга. Она интересная.
        '''),
        dbc.Input(id="task07", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task8=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 8: Переведите на немецкий язык
            Эта картина новая
        '''),
        dbc.Input(id="task08", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task9=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 9: Переведите на немецкий язык
            Вы учитель?
        '''),
        dbc.Input(id="task09", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task10=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 10: Переведите на немецкий язык
            Эта газета интересная?
        '''),
        dbc.Input(id="task010", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}

    )

task11=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 11: Опишите предмет на картинке
            _Пример: Dieser Computer ist schwarz_
        '''),
         html.Img(src='../assets/pencil1.jpg', alt='eeerr', width='200px', height='200px', style={'margin':'20px'}),
        dbc.Input(id="task011", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ] ,
        style={'margin-bottom':'20px'}
    )


modal = html.Div(
    [   
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle( id='score0')),
                dbc.ModalBody(
                    [
                        html.Img(src='../assets/cat.jpg', width='100%', height='100%', style={'align':'center'})
                        ]
                              ),
               
            ],
            id="modal0",
            is_open=False,
        ),
    ]
)



layout=html.Div(
    [
        html.Div(
            [
                navbar
                ]
            ),
        html.Div(
            [
                task1,
                html.P(id="res01"),
                task2,
                html.P(id="res02"),
                task3,
                html.P(id="res03", style={'background-color':'BlanchedAlmond'}),
                task4,
                html.P(id="res04", style={'background-color':'BlanchedAlmond'}),
                task5,
                html.P(id="res05", style={'background-color':'BlanchedAlmond'}),
                task6,
                html.P(id="res06", style={'background-color':'BlanchedAlmond'}),
                task7,
                html.P(id="res07", style={'background-color':'BlanchedAlmond'}),
                task8,
                html.P(id="res08", style={'background-color':'BlanchedAlmond'}),
                task9,
                html.P(id="res09", style={'background-color':'BlanchedAlmond'}),
                task10,
                html.P(id="res010", style={'background-color':'BlanchedAlmond'}),
                task11,
                html.P(id="res011", style={'background-color':'BlanchedAlmond'}),
                modal,
                dbc.Button("Подвести итоги", id="res_button0", n_clicks=0),
               
                html.Span(id="example-output0", style={"verticalAlign": "middle", "margin-left":'30px', 'font-size':'20px'}),
                ] ,
            style={'padding':'20px'}
            )
        ]
    )






 #Функция для приведения всех строк к нормальному виду: нижний регистр, все точки и лишние пробелы удаляются
def normstring(st):
    st=str(st)
    st=st.lower()
    
    if st[-1]=='.' or st[-1]=='?':
        st=st[:-1]
    st=st.replace('.', ' ')
    while st.find('  ') != -1:
        st=st.replace('  ', ' ')
    st=st.strip(' ')
    return st

answer_list=[4,2,1,[3,4],'diese blume ist rot', 'das ist eine vase die vase ist gelb', 'das ist mein buch es ist interresant',
             'dieses bild ist neu', 'sind sie lehrer', 'ist diese zeitung interresant', 'dieser stift ist blau']

@callback(
    [Output("example-output0", "children"),
    Output("res01", "children"),
    Output("res02", "children"),
    Output("res03", "children"),
    Output("res04", "children"),
    Output("res05", "children"),
    Output("res06", "children"),
    Output("res07", "children"),
    Output("res08", "children"),
    Output("res09", "children"),
    Output("res010", "children"),
    Output("res011", "children"),
    Output("task01", "style"),
    Output("task02", "style"),
    Output("task03", "style"),
    Output("task04", "style"),
    Output("task05", "style"),
    Output("task06", "style"),
    Output("task07", "style"),
    Output("task08", "style"),
    Output("task09", "style"),
    Output("task010", "style"),
    Output("task011", "style"),
    Output("modal0", "is_open"),
    Output("score0", "children"),
    ],
    
    [Input("res_button0", "n_clicks")],
       
   
    [   State("task01", "value"),
        State("task02", "value"),
        State("task03", "value"),
        State("task04", "value"),
        State("task05", "value"),
        State("task06", "value"),
        State("task07", "value"),
        State("task08", "value"),
        State("task09", "value"),
        State("task010", "value"),
        State("task011", "value"),
        State("modal0", "is_open")
        ],
    
       prevent_initial_call=True
    
)

def on_button_click(n, t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11, is_open):
    success_style={'border':'2px groove green', 'border-radius':'5px'}
    error_style={'border':'2px groove red', 'border-radius':'5px'}
    success_message = ''
    err_message='Правильный ответ: '
    score=0

    if n is None:
        return "Not clicked."
    else:
        if t1 !=answer_list[0]:
            res1=err_message+str(answer_list[0])
            st1=error_style
        else:
            res1 = success_message
            st1=success_style
            score+=1

        if t2 !=answer_list[1]:
            res2=err_message+str(answer_list[1])
            st2=error_style
        else:
            res2 = success_message
            st2=success_style
            score+=1

        if t3 !=answer_list[2]:
            res3=err_message+str(answer_list[2])
            st3=error_style
        else:
            res3 = success_message
            st3=success_style
            score+=1

        if t4 !=answer_list[3]:
            res4=err_message+str(answer_list[3])
            st4=error_style
        else:
            res4 = success_message
            st4=success_style
            score+=1
 
        if normstring(t5) !=answer_list[4]:
            res5=err_message+str(answer_list[4])
            st5=error_style
        else:
            res5 = success_message
            st5= success_style
            score+=1

        if normstring(t6) !=answer_list[5]:
            res6=err_message+str(answer_list[5])
            st6=error_style
        else:
            res6 = success_message
            st6= success_style
            score+=1

        if normstring(t7) !=answer_list[6]:
            res7=err_message+str(answer_list[6])
            st7=error_style
        else:
            res7 = success_message
            st7= success_style
            score+=1

        if normstring(t8) !=answer_list[7]:
            res8=err_message+str(answer_list[7])
            st8=error_style
        else:
            res8 = success_message
            st8= success_style
            score+=1

        if normstring(t9) !=answer_list[8]:
            res9=err_message+str(answer_list[8])
            st9=error_style
        else:
            res9 = success_message
            st9= success_style
            score+=1

        if normstring(t10) !=answer_list[9]:
            res10=err_message+str(answer_list[9])
            st10=error_style
        else:
            res10 = success_message
            st10= success_style
            score+=1

        if normstring(t11) !=answer_list[10]:
            res11=err_message+str(answer_list[10])
            st11=error_style
        else:
            res11 = success_message
            st11= success_style
            score+=1
        if n:
            op=not is_open
        else:
            op=is_open


        return f'Ваш результат: {score} из 11', res1,res2,res3,res4,res5,res6,res7,res8,res9,res10,res11,st1,st2,st3,st4,st5,st6,st7,st8,st9,st10, st11, op, f'Ваш результат: {score} из 11'
          
         


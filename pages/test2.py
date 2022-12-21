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
                dbc.DropdownMenuItem("Урок 1", href="/pages/test1"),
                dbc.DropdownMenuItem("Урок 2", href="#"),
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
    brand="Практика: урок 2",
    brand_href="#",
    color="primary",
    dark=True,
)


task1=html.Div(
    [
        dcc.Markdown('''
            #### № 1: заполните пропуски
            ____ Tisch  und ____ Kinder

        '''),
         dbc.RadioItems(
            options=[
                {"label": "die, das", "value": 1},
                {"label": "das, der", "value": 2},
                {"label": "der, die", "value": 3},
                {"label": "der, das", "value": 4},
            ],
            value=0,
            id="task1",
        ),
        ],
        style={'margin-bottom':'20px'}
    )


task2=html.Div(
    [
        dcc.Markdown('''
        ---
       #### № 2: Выберите существительные, форма множнственного числа которых совпадает с формой единственного числа

        '''),
         dbc.Checklist(
            options=[
                {"label": "der Student", "value": 1},
                {"label": "der Lehrer", "value": 2},
                {"label": "der Wagen", "value": 3},
                {"label": "die Tasche", "value": 4},
                {"label": "das Mädchen", "value": 5},
                {"label": "das Bild", "value": 6},
                {"label": "die Blume", "value": 7},
                {"label": "das Zimmer", "value": 8},
                {"label": "das Haus", "value": 9},
            ],
            value=0,
            id="task2",
        ),
        ],
        style={'margin-bottom':'20px'}
    )


task3=html.Div(
    [
        dcc.Markdown('''
        ---
       #### № 3: заполните пропуски определенными и неопределенными артиклями  
       _Если на месте пропуска не должно быть артикля, в ответе поставьте знак "-"_  
       
       Das ist ____ Vase. ____ Vase ist blau.

        '''),
       dbc.Input(id="task3", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task4=html.Div(
    [
        dcc.Markdown('''
        ---
       #### № 4: заполните пропуски определенными и неопределенными артиклями  
        _Если на месте пропуска не должно быть артикля, в ответе поставьте знак "-"_  
        
        Das sind ____ Bilder. ____ Bilder sind alt.

        '''),
       dbc.Input(id="task4", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task5=html.Div(
    [
        dcc.Markdown('''
        ---
       #### № 5: заполните пропуски определенными и неопределенными артиклями
        _Если на месте пропуска не должно быть артикля, в ответе поставьте знак "-"_  
          
        Das ist ____ Sportler. ____ Sportler ist gut.

        '''),
       dbc.Input(id="task5", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task6=html.Div(
    [
        dcc.Markdown('''
        ---
       #### № 6: образуйте уменьшительно ласкательную форму с помощью суффикса -chen
            
       Die Tasche - ...

        '''),
       dbc.Input(id="task6", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task7=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 7: образуйте существительное женского рода
            
            Der Arbeiter - ...

        '''),
       dbc.Input(id="task7", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task8=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 8: Переведите на немецкий язык
            
            Эти карандаши серые

        '''),
       dbc.Input(id="task8", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task9=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 9: Переведите на немецкий язык
            
            Ваши газеты новые

        '''),
       dbc.Input(id="task9", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task10=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 10: Переведите на немецкий язык
            
            Его комнатка маленькая

        '''),
       dbc.Input(id="task10", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task11=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 11: Переведите на немецкий язык
            
            Твои учительницы хорошие?

        '''),
       dbc.Input(id="task11", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task12=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 12: Переведите на немецкий язык
            
           Этот человек - их работник

        '''),
       dbc.Input(id="task12", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )

task13=html.Div(
    [
        dcc.Markdown('''
            ---
            #### № 13: Переведите на немецкий язык
            
           Это её машины?

        '''),
       dbc.Input(id="task13", type="text", style={ 'border-radius':'5px', 'border':'1px solid gray'}),
        ],
        style={'margin-bottom':'20px'}
    )



answer_list=[3, [2,3,5,8], 'eine die', '- die', '- der', 'das taschen', 'die arbeiterin',
            'diese stifte sind grau', ['eure zeitungen sind neu', 'ihre zeitungen sind neu'],
            'sein zimmerchen ist klein', 'sind deine lehrerinnen gut', 'dieser mensch ist ihr arbeiter',
            'ist das ihre wagen']


modal = html.Div(
    [ 
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle( id='score')),
                dbc.ModalBody(
                    [
                        html.Img(src='../assets/cat.jpg', width='100%', height='100%', style={'align':'center'})
                        ]
                              ),
               
            ],
            id="modal",
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
                html.P(id="res1", style={'background-color':'BlanchedAlmond'}),
                task2,
                html.P(id="res2", style={'background-color':'BlanchedAlmond'}),
                task3,
                html.P(id="res3", style={'background-color':'BlanchedAlmond'}),
                task4,
                html.P(id="res4", style={'background-color':'BlanchedAlmond'}),
                task5,
                html.P(id="res5", style={'background-color':'BlanchedAlmond'}),
                task6,
                html.P(id="res6", style={'background-color':'BlanchedAlmond'}),
                task7,
                html.P(id="res7", style={'background-color':'BlanchedAlmond'}),
                task8,
                html.P(id="res8", style={'background-color':'BlanchedAlmond'}),
                task9,
                html.P(id="res9", style={'background-color':'BlanchedAlmond'}),
                task10,
                html.P(id="res10", style={'background-color':'BlanchedAlmond'}),
                task11,
                html.P(id="res11", style={'background-color':'BlanchedAlmond'}),
                task12,
                html.P(id="res12", style={'background-color':'BlanchedAlmond'}),
                task13,
                html.P(id="res13", style={'background-color':'BlanchedAlmond'}),
                modal,
                dbc.Button("Подвести итоги", id="res_button", n_clicks=0),
               
                html.Span(id="example-output00", style={"verticalAlign": "middle", "margin-left":'30px', 'font-size':'20px'}),
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


@callback(
    [Output("example-output00", "children"),
    Output("res1", "children"),
    Output("res2", "children"),
    Output("res3", "children"),
    Output("res4", "children"),
    Output("res5", "children"),
    Output("res6", "children"),
    Output("res7", "children"),
    Output("res8", "children"),
    Output("res9", "children"),
    Output("res10", "children"),
    Output("res11", "children"),
    Output("res12", "children"),
    Output("res13", "children"),
    Output("task1", "style"),
    Output("task2", "style"),
    Output("task3", "style"),
    Output("task4", "style"),
    Output("task5", "style"),
    Output("task6", "style"),
    Output("task7", "style"),
    Output("task8", "style"),
    Output("task9", "style"),
    Output("task10", "style"),
    Output("task11", "style"),
    Output("task12", "style"),
    Output("task13", "style"),
    Output("modal", "is_open"),
    Output("score", "children"),
    ],
    
    [Input("res_button", "n_clicks")],
       
   
    [   State("task1", "value"),
        State("task2", "value"),
        State("task3", "value"),
        State("task4", "value"),
        State("task5", "value"),
        State("task6", "value"),
        State("task7", "value"),
        State("task8", "value"),
        State("task9", "value"),
        State("task10", "value"),
        State("task11", "value"),
        State("task12", "value"),
        State("task13", "value"),
        State("modal", "is_open")
        ],
    
       prevent_initial_call=True
    
)

def on_button_click(n, t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13, is_open):
    success_style={'border':'2px groove green', 'border-radius':'5px'}
    error_style={'border':'2px groove red', 'border-radius':'5px'}
    success_message = ''
    err_message='Правильный ответ: '
    score=0

    if n is None:
        return "Not clicked.", '0',' ',' ',' ',' ',' ',' ', ' ',' ',' ', ' '
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

        if normstring(t3) !=answer_list[2]:
            res3=err_message+str(answer_list[2])
            st3=error_style
        else:
            res3 = success_message
            st3=success_style
            score+=1

        if normstring(t4) !=answer_list[3]:
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

        if normstring(t9) !=answer_list[8][0] or normstring(t9) !=answer_list[8][1]:
            res9=err_message+str(answer_list[8][0]+' или ' +answer_list[8][1])
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
        if normstring(t12) !=answer_list[11]:
            res12=err_message+str(answer_list[11])
            st12=error_style
        else:
            res12 = success_message
            st12= success_style
            score+=1
        if normstring(t13) !=answer_list[12]:
            res13=err_message+str(answer_list[12])
            st13=error_style
        else:
            res13 = success_message
            st13= success_style
            score+=1
        if n:
            op=not is_open
        else:
            op=is_open


        return f'Ваш результат: {score} из 13', res1,res2,res3,res4,res5,res6,res7,res8,res9,res10,res11, res12, res13, st1,st2,st3,st4,st5,st6,st7,st8,st9,st10, st11, st12, st13, op, f'Ваш результат: {score} из 13'
          
         


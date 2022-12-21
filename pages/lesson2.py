import dash

import dash_bootstrap_components as dbc
from dash import html, dcc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("На главную", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Урок 1", href="/pages/lesson1"),
                dbc.DropdownMenuItem("Урок 2", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Теория ",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Урок 1", href="/pages/test1"),
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
    brand="Теория: урок 2",
    brand_href="#",
    color="primary",
    dark=True,
)


rule1=dcc.Markdown('''
    ##  Образование множественного числа существительных  
    ##  
    ####     Мужской род (Maskulinum)
''')

PluM_table_header = [
    html.Thead(html.Tr([ html.Th(dcc.Markdown('''Принимают суффикс _-e_''')), 
                        html.Th(dcc.Markdown('''Принимают суффикс _-er_''')), 
                        html.Th(dcc.Markdown('''Принимают суффикс _-en_''', ))]), style={'background-color':'PaleTurquoise'} )
]

row1 = html.Tr([html.Td(dcc.Markdown(''' - ein Tisch - Tische \n - ein Stift - Stifte \n - ein Stuhl - Stuhle''')), 
                html.Td(dcc.Markdown(''' - ein Mann - Manner \n - ein Wald - Walder''')), 
                html.Td(dcc.Markdown(''' - ein Mensch - Menschen \n - ein Junge - Jungen \n - ein Student - Studenten'''))])

PluM_table_body = [html.Tbody([row1])]

PluM_table = dbc.Table(PluM_table_header + PluM_table_body, bordered=True, size='sm')

rule2=dcc.Markdown('''
    Многие существительные, приннимая суффиксы _-e_ и _-er_ принимают также Umlaut.  
    Формы единственного и множественного числа совпадают у существительных с суффиксами _-er_, _-el_, _-n_:  
    ###### > der Lehrer - die Lehrer  
    ###### > der Wagen - die Wagen

    #### Женский род (Femininum)
''')



PluF_table_header = [
    html.Thead(html.Tr([ html.Th(dcc.Markdown(''' Принимают суффикс _-en_''')), 
                        html.Th(dcc.Markdown('''Принимают суффикс _-e_ (и Umlaut)''') )]), style={'background-color':'Pink'} )
]

row1 = html.Tr([html.Td(dcc.Markdown(''' - eine Lampe - Lampen \n - eine Blume - Blumen \n - eine Vase - Vasen''')), 
                html.Td(dcc.Markdown (''' - Односложные существительные: \n - eine Hand - Hände \n - eine Nacht - Nächte''')), 
             ])

PluF_table_body = [html.Tbody([row1])]

PluF_table = dbc.Table(PluF_table_header + PluF_table_body, bordered=True, size='sm')


rule3=dcc.Markdown('''
   
    ####     Средний род (Neutrum)
''')

PluN_table_header = [
    html.Thead(html.Tr([ html.Th(dcc.Markdown('''Принимают суффикс _-e_''')), 
                        html.Th(dcc.Markdown('''Принимают суффикс _-er_''')), 
                        html.Th(dcc.Markdown('''Принимают суффикс _-s_''' ))]), style={'background-color':'PapayaWhip'} )
]

row1 = html.Tr([html.Td(dcc.Markdown(''' - ein Zeug - Zeuge''')), 
                html.Td(dcc.Markdown(''' - ein Kind - Kinder \n - ein Buch - Bücher \n - ein Haus - Häuser''')), 
                html.Td(dcc.Markdown(''' - ein Kino - Kinos \n - ein Hotel - Hotels \n - ein Foto - Fotos'''))])

PluN_table_body = [html.Tbody([row1])]

PluN_table = dbc.Table(PluN_table_header + PluN_table_body, bordered=True, size='sm')

rule4 = dcc.Markdown('''
     Существительные среднего рода, принимающие суффикс _-er_, принимают также Umlaut. Суффикс _-s_ принимают существительные иностранного происхождения.  
     Форма единственного и множественного числа в среднем роде совпадает у существительных с суффиксами _-er, -el, -n_:  
     ###### > das Mädchen - die Mädchen  
     ###### > das Zimmer - die Zimmer

     ## Образование уменьшительно-ласкательных существительных
     Образование уменьшительно-ласкатеьной формы производится обычно с помощью суффикса _-chen_, и реже - с помощью суффикса _-lein_.
    Корневые гласные _a, o, u_ при это приобретают _Umlaut_. Все существительные с суффиксом _-chen_ относятся к среднему роду и не 
    изменяются во множественном числе:
    ###### > der Tisch - das Tischen
    ###### > der Stuhl - das Stulchen
    ###### > die Blime - das Blumchen
    ###### > das Kind - das Kindchen

    ## Образование существительных женского рода, обозначающих лица по профессиональной, партийной или национальной принадлежности
    ###### _Обратите внимание - перед существительными обозначающими лица по профессиональной, партийной или национальной принадлежности, неопределенный артикль не употребляется - это невежливо!_
    Существительное женского рода образуется с помощью добавление суффикса _-in_ к существительному мужского рода.

    ###### > der Lehrer - die Lehrerin
    ###### > der Student - die Studentin

    Во множественном числе _-n_  удваивается
    ###### > die Lehrerin - die Lehrerinnen
    ###### > die Studentin - die Studentinnen

    ## Притяжательные местоимения 
    Они указывают на принадлежность предмета определенному лицу (мой, твой, их и т.п.) и изменяются по родам, числам и стоят перед определяемыми
    существительными: _mein Lehrer, deine Blume, sein Buch_

    
''')

Mest_table_header = [
    html.Thead(html.Tr([html.Th("Person"), html.Th("M",  style={'background-color':'PaleTurquoise'}), html.Th("F",  style={'background-color':'Pink'}), html.Th('Neutrum', style={'background-color':'PapayaWhip'}), html.Th("Plural"),]))
]

row1 = html.Tr([html.Td('ich'), html.Td("mein"), html.Td("meine"),  html.Td("mein"),  html.Td("meine")])
row2 = html.Tr([html.Td('du'), html.Td("dein"), html.Td("deine"),  html.Td("dein"),  html.Td("deine")])
row3 = html.Tr([html.Td('er'), html.Td("sein"), html.Td("seine"),  html.Td("sein"),  html.Td("seine")])
row4 = html.Tr([html.Td('sie'), html.Td("ihr"), html.Td("ihre"),  html.Td("ihr"),  html.Td("ihre")])
row5 = html.Tr([html.Td('es'), html.Td("sein"), html.Td("seine"),  html.Td("sein"),  html.Td("seine")])
row6 = html.Tr([html.Td('wir'), html.Td("unser"), html.Td("unsere"),  html.Td("unser"),  html.Td("unsere")])
row7 = html.Tr([html.Td('ihr'), html.Td("euer"), html.Td("eure"),  html.Td("euer"),  html.Td("eure")])
row8 = html.Tr([html.Td('sie'), html.Td("ihr"), html.Td("ihre"),  html.Td("ihr"),  html.Td("ihre")])
row9 = html.Tr([html.Td('Sie'), html.Td("Ihr"), html.Td("Ihre"),  html.Td("Ihr"),  html.Td("Ihre")])

Mest_table_body = [html.Tbody([row1, row2, row3, row4,row5, row6, row7, row8, row9])]

Mest_table = dbc.Table(Mest_table_header + Mest_table_body, bordered=True, size='sm')

rule5=dcc.Markdown('''
      ##  Вопросы
      Чтобы построить вопросительное предложение, необходимо соблюсти обратный порядок слов.  
      При прямом порядке на первом месте в предложении стоит подлежащее, а на стором сказуемое. При обратном порядке сказуемое ставится на 
      первое место, сказуемое на второе, а после них - все сторостепенные члены предложения.

      Пример:  
      ###### > Du bist gut - _Bist du_ gut?
      ###### > Ihre Tasche sind neu - _Sind_ ihre _Tashe_ neu?
''')

layout = html.Div(
    [
        html.Div(
            [
               html.Div(
               navbar
                    ) 
                ,
        html.Div(
            [
               rule1,
               PluM_table,
               rule2,
               PluF_table,
               rule3,
               PluN_table,
               rule4, 
               Mest_table,
               rule5
                 ],

                 style={'padding':'20px'}
             
             )
    ]
            )
        
        ]
    
    )
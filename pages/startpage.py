import dash
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go


dfl=pd.read_csv("assets/popular_languages.csv")
fig1=px.pie(dfl, values='summary', names='language')

dfc=pd.read_csv("assets/countries1.csv")
countries = list(dfc.iloc[:,0])
ge_speakers = list(dfc.iloc[:,1])
people = list(dfc.iloc[:,2])
percentage=[]
for i in range(len(countries)):
    percentage.append((ge_speakers[i]/people[i])*100)

fig2 = go.Figure(  data=[
    go.Bar(name='Процентное соотношение', x=countries, y=percentage)
    ]
  )

fig3 = px.histogram(dfc, x="country", y='speakersnum')
fig3.update_layout(bargap=0.2)

fig4 = go.Figure(  data=[
    go.Bar(name='Говорят по-немецки', x=countries, y=ge_speakers),
    go.Bar(name='Население страны', x=countries, y=people)
    ]
  )


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
    brand="DEUTSCH",
    brand_href="#",
    color="primary",
    dark=True,
)
  




card_theory = dbc.Card(
    [
        dbc.CardImg(src="assets/book.png", top=True),
        dbc.CardBody(
            [
                html.H4("Теория", className="card-title"),
                html.P(
                    "Теоретические материалы к каждому уроку "
                    "таблицы, правила и др.",
                    className="card-text",
                ),
               
                
                dbc.DropdownMenu(
                                 children=[
                                     dbc.DropdownMenuItem("Урок 1", href="/pages/lesson1"),
                                     dbc.DropdownMenuItem("Урок 2", href="/pages/lesson2"),    #####################
                                            ],
                           
                                 label="Теория к урокам",
                                 color="light"
                                 ),
                                    
            ] 
            
        ),
    ],
    color='dark',
    inverse=True,
    style={"width": "22rem"},
)


card_practice=dbc.Card(
   [
       dbc.CardImg(src="assets/write.jpg", top=True),
       dbc.CardBody(
          [
              html.H4("Практика", className="card-title"),
              html.P(
                  "Практические задания для проверки знаний к каждому уроку ",
                                 className="card-text", ),
              dbc.DropdownMenu(
                  children=[ 
                      dbc.DropdownMenuItem("Урок 1", href="/pages/test1"),      ###################
                      dbc.DropdownMenuItem("Урок 2", href="/pages/test2"),      #####################
                      ],
                  label="Задания к урокам",
                  color="light"
                  ),
           ]
           
           )
    ],
    color='dark',
    inverse=True,
    style={"width": "22rem"},
    )


card_text=dbc.Card(
   [
       dbc.CardImg(src="assets/reading.jpg", top=True),
       dbc.CardBody(
          [
              html.H4("Тексты", className="card-title"),
              html.P(
                  "Тексты для самостоятельного чтения и перевода ",
                                 className="card-text", ),
              dbc.DropdownMenu(
                  children=[  
                      dbc.DropdownMenuItem("Текст 1", href="/pages/text1"),      ###################
                      dbc.DropdownMenuItem("Текст 2", href="/pages/text2"),      #####################
                      ],
                  label="Тексты",
                  color="light"
                  ),

           ]
           
           )
    ],
    color='dark',
    inverse=True,
    style={"width": "22rem"},
 )



layout=html.Div(
    [
        html.Div(
            [
               html.Div(
                   [
                       navbar
                       ]
                   
                   ),
               html.Div(
                   [
                       dcc.Markdown('''
                         WIR LERNEN DEUTSCH 

                       
                        '''),   
                      ],
                      style={'background-image':'url(../assets/de_bg.png)', 'height':'200px','background-size': '100% 100%',  'text-align': 'center', 
                             'padding':'80px 150px 0px 150px', 'margin-bottom':'30px', 'font-size':'40px','font-weight':'700', 'font-family':'serif', 'font-stretch': 'ultra-expanded' }
                    ), 
               html.Div(
                   [
                      dbc.Row(
                          [ 
                              dbc.Col( [
                                   dcc.Markdown(''' 
                                         ## Для чего нужно изучать немецкий язык?
                                         ---
                                         #### Образование в Германии 
                                         Германия предлагает множество бесплатных образовательных программ для студентов со всего мира. Существуют специальные визы, дающие право на работу в стране. 
                                            Помимо этого, есть программы обучения по обмену как для школьников, так и для студентов.
                                            Германия спонсирует международные обмены. Например, в 2019 году  [Служба академических обменов DAAD](https://www.daad.ru/ru/) поддержала
                                           **более 145 000** учащихся, ученых, и студентов в их исследованиях и учебе. При этом __41,5%__ из них были иностранцами.

                                         #### Уровень технологий и науки
                                         Германия находится в ряду лидеров по экспорту высокотехнологичной продукции и вносит огромный вклад в развитие инноваций, а высокий уровень экономического 
                                         развития делает страну экномическим центром Европы.   
                                         Помимо этого, на территории Германии проводится множество международных выставок и ярмарок. Знание немецкого языка дает возможность работать в 
                                         самых современных всемирно известных команиях и принимать участие в передовых разработках, имея достойную заработную плату и престижную профессию.
                                         
                                         #### Популярность
                                         Немецкий язык, по различным данным, входит в 10-15 самых популярных языков в мире, на нем говорит _более 100 миллионов_ человек. При этом существует множество диалектов немецкого языка, 
                                         и число говорящих на них людей не входит в официальную статистику. В качестве официального языка немецкий используется в Германии, Австрии и Лихтенштейне,
                                        а одним из официальных признан в Швейцарии, Люксембурге, Италии и Бельгии. Также он признан языком национальных меньшинств в ряде стран. 
                                                

                                             ''')
                                  ],
                                      width=9,
                                      #style={'padding':'30px'}
                                  ),
                              dbc.Col(
                                  style={'background-image':'url(../assets/berlin.jpg)', 'background-size': '100% 100%', 'margin':'40px', 'box-shadow': '0 0 8px 8px white inset', 'border-radius':'15px'}, 
                                  

                                  )
                               
                               ]
                       
                            ),
                      dbc.Row(
                          [   dcc.Markdown('''
                                  ##  Cтатистика
                                  ---
                          '''),
                              dbc.Col(
                                  [   
                                      dcc.Markdown(''' 
                                     ##### Число людей, говорящих на немецком, в различных странах
                                  '''), 
                                       dbc.RadioItems(
                                           options=[
                                               {"label": "В процентах", "value": 1},
                                               {"label": "В числах", "value": 2},
                                               {"label": "В соотношении с населением страны", "value": 3},
                                               ],
                                           value=1,
                                           id="radioitems-inline-input",
                                           inline=True,
                                           ),

                                       dcc.Graph(id='graph2'),
                                       dcc.Markdown('''
                                     * _На графике представлены страны, в которых немецкий язык является официальным или признан языком национальных меньшинств_
                                     '''),
                                       
                             
                                      ],
                                      width=7,

                                  ),
                              dbc.Col(
                                  [
                                     dcc.Markdown(''' 
                                     ##### Распространение языков в мире
                                     #'''), 
                                      dcc.Dropdown(id='langs',
                                           options=['Первый язык (родной)', 'Второй язык', 'Общее число носителей'],
                                           value='Общее число носителей', clearable=False
                                           ),
                                      dcc.Graph(id='graph1'),
                                      ],
                                      width=5
                                  )

                          
                          ],
                            style={'margin-top':'50px', 'margin-bottom':'50px'}
                          ),


                      dbc.Row(
                          [   dcc.Markdown('''
                               ## Учебные материалы
                               ---
                                '''),
                              dbc.Col(card_theory, width="auto", style={'margin-bottom':'20px'} ),
                              dbc.Col(card_practice, width="auto"),
                              dbc.Col(card_text, width="auto"),
                              dcc.Markdown('''
                               Представленные теоретические и практичесчкие материалы разработаны на основе учебных пособий:
                               * Камянова Татьяна - Практический курс немецкого языка
                               * В.Завьялова, Л. Ильина - Практический курс немецкого языка для начинающих  
                                '''),
                            ],
                            style={'margin-bottom':'20px'}
                       
                       ),
                   ],
                   style={'padding':'30px'}
                 
                   )
               ]
            )
        ]
    )
@callback(
    Output("graph2", "figure"), 
    Input("radioitems-inline-input", "value"))
def generate_graph(radiovalue):
    
    if radiovalue==1:
        fig=fig2
    elif radiovalue==2:
        fig=fig3
    elif radiovalue==3:
        fig=fig4

    return fig


@callback(
    Output("graph1", "figure"), 
    Input("langs", "value"))

def generate_chart( langs):
     
    if langs=='Первый язык (родной)':
        langs='first'
    elif langs=='Второй язык':
        langs='second'
    elif langs == 'Общее число носителей':
         langs='summary'
    fig = px.pie(dfl, values=langs, names='language')
    return fig
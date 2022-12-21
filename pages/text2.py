import dash

import dash_bootstrap_components as dbc
from dash import html, dcc



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
                dbc.DropdownMenuItem("Текст 2", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Тексты ",
        ),


    ],
    brand="Текст 2",
    brand_href="#",
    color="primary",
    dark=True,
)


text=dcc.Markdown('''
    ## Im Übungsraum
    Hier ist ein Zimmer. Es ist ein Übungsraum. Er liegt oben. Der Übungsraum ist groß und hell. Hier gibt es drei Fenster. Die Fensster sind
    breit und hoch. Die Decke ist weiß. Die Wände sind hellgrün. Oben hängen sechs Lampen. Vorn hängt eine Tafel. Die Tafel ist schwarz.
    Rechts ist eine Tür. Die Tür ist braun. Darüber hängt eine Uhr. Die Uhr ist rund. Links hängen viele Tabellen und Bilder. Hier stehen auch
    viele Tische und Stühle.  
    Heute haben die Hörer drei Stunden Deutsch. Zuerst kommt det Gruppenälteste. Er öffnet das Fenster und lüftet das Zimmer. Er bringt ein 
    Stück Kreide und einen Lappen. Dann schreibt er das Datum an die Tafel. Jetzt ist alles in Ordnung.  
    Um 7 Uhr betreten die Hörer den Übungsraum. Da kommt der Lehrer und der Unterricht beginnt.  
    Die Hörer begrüßen den Lehrer, und der Lehrer sagt: "Guten Abend, nehmen Sie Platz! Sind heute alle anwesend?" fragt er. "Ja, heute sind
    alle Hörer anwesend, niemand fehlt", antwortet der Gruppenälteste. "Das ist gut. Zuerst prüfen wir die Hausaufgabe. Haben Sie für heute 
    Hausaufgaben, Herr Krylow?" - "Ja, wir haben heute eine Übersetzung." - "Ist sie schwer?" - "Nein, die Übersetzung ist nicht schwer. Der
    Text aber ist schwer. Einen Satz verstehe ich nicht", sagt Krylow.  
    "Kennen Sie die Wörter nicht?" fragt der Lehrer. "Brauchen Sie ein Wörterbuch?" - "Nein, ich brauche kein Wörterbuch, ich kenne  alle 
    Wörter, aber ich verstehe den Satz nicht." - "Und Sie, Oleg, verstehen Sie diesen Satz auch nicht?" - "Doch, ich verstehe den Satz." - 
    antwortet Oleg. - "Dann öffnen Sie das Buch und übersetzen Sie den Satz", sagt der Lehrer. Below öffnet das Buch, übersetzt den Satz und 
    erklärt die Regel. "Ist jetzt alles klar, Herr krylow?" - "Ja, danke, jetzt verstehe ich alles". - "Nun gut, lesen Sie den Text noch einmal,
    Oleg. Aber nicht so schnell bitte. Langsam, aber richtig. Sie lesen sehr leise. Lesen Sie laut. Beachten Sie die Aussprache!"  
    Viele Hörer lesen den Text, dann übersetzen sie diesen Text und beantworten einige Fragen zum Text. 
''')

layout= html.Div(
    [
        html.Div(navbar),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                text
                                ] ,
                             width=8
                            ),
                        dbc.Col(
                            style={'background-image':'url(../assets/students2.jpg)', 
                                    'margin':'20px', 'background-size': '100% 100%'}, 
                            
                            )
                        ]
                    ),
                dbc.Row(dcc.Markdown(''' 
                ---
                #### Словарь''')),
                dbc.Row(
                    [
                        dbc.Col(
                            [  
                                dcc.Markdown('''
                                  oben - _наверху_  
                                  vorn - _впереди_  
                                  rechts - _справа_  
                                  darüber - _над (чем-то)_  
                                  links - _слева_  
                                  in Ordnung - _в порядке_  
                                 
                                ''')
                                ],
                                width = 6
                            ),
                        dbc.Col(
                            [
                                dcc.Markdown('''
                                
                                  doch - _напротив (как ответ на вопрос)_  
                                  dann - _затем_  
                                  nun (gut) - _что ж_  
                                  beantworten - _отвечать_  
                                  Frage zum Text - _вопрос к тексту_  
                                  
                                ''')
                                ],
                                width=6
                            
                            )
                        ]
                    )
                ],
                style={"padding":"20px"}
            )
        ]
    
    )
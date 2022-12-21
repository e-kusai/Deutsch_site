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
                dbc.DropdownMenuItem("Текст 1", href="#"),
                dbc.DropdownMenuItem("Текст 2", href="/pages/text2"),
            ],
            nav=True,
            in_navbar=True,
            label="Тексты ",
        ),


    ],
    brand="Текст 1",
    brand_href="#",
    color="primary",
    dark=True,
)

text=dcc.Markdown('''
## Wir lernen Fremdsprachen
   Ich bin Ingenieur. Ich arbeite schon drei Jahre als Ingenieur. Ich arbeite nur am Tage. Die Arbeit beginnt um 8 Uhr morgens.
  Am Abend besuche ich einen Kursus für Fremdsprachen. Ich lerne Deutsch.  
 Ich gehe dreimal in der Woche zum Unterricht. Ich wohne nicht weit und gehe gewöhnlich zu Fuß. Der Unterricht beginnt um 7 Uhr abends.
 Um 10 Uhr ist er zu Ende.  
 Die Gruppe ist groß. Wir sind 20 Hörer. Es läutet. Der Lehrer kommt, und die Stunde beginnt. Der Lehrer sagt: "Guten Abend!" "Guten Abend!" 
 antworten wir. "Wer fehlt heute?" fragt er. Der Gruppenälteste antwortet: "Heute fehlen zwei Hörer. Wahrscheinlich sind sie krank."  
 Zuerst prüft der Lehrer die Hausaufgabe. Die Hausaufgabe ist heute leicht. Alle antworten gut. Wir sind immer sehr fleißig.  
 Wir lesen und übersetzen deutsche Texte. Die Texte sind gewöhnlich schwer. Aber wir lesen und übersetzen richtig. Nur einege Hörer machen 
 noch Fehler. Der Lehrer korrigiert, er sagt: "Sie lesen falsch. Lesen Sie, bitte, noch einmal!". Die Hörer lesen den Text noch einmal.  
 "Herr Below, kommen Sie an die Tafel!" sagt der Lehrer. Below kommt an die Tafel. Er schreibt, und wir schreiben auch.  
 Um halb 9 läutet es wieder. Die Stunde ist zu Ende. Die Pause beginnt.
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
                            style={'background-image':'url(../assets/students1.jpg)', 
                                   'background-size': '100% 100%', 'margin':'20px',}, 
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
                                  schon - _уже_  
                                  nur - _только_  
                                  am Tage (Abend) - _днем (вечером)_  
                                  um 8 Uhr (morgens, abends) - _в 8 утра (вечера)_  
                                  dreimal in der Woche - _три раза в неделю_  
                                  zu Fuß - _пешком_  
                                 
                                ''')
                                ],
                                width = 6
                            ),
                        dbc.Col(
                            [
                                dcc.Markdown('''
                                
                                  zu Ende - _кончается_  
                                  es läutet - _звенит звонок_  
                                  immer - _всегда_  
                                  noch - _еще_  
                                  an die Tafel - _к доске_  
                                  halb 9 - _половина 9_
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
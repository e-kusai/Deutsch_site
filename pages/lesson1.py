import dash

import dash_bootstrap_components as dbc
from dash import html, dcc



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("На главную", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Урок 1", href="#"),
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
    brand="Теория: урок 1",
    brand_href="#",
    color="primary",
    dark=True,
)

rule1 = dcc.Markdown('''
## Существительные  

В немецком языке существительные имеют ряд особенностей, которые необходимо запомнить:
* Все существительные пишутся с большой буквы
* Существительные разделяются по родам. Всего их 3 - мужской (_Maskulinum_), **женский** (_Femininum_) и средний (_Neutrum_)
* Перед существительными ставятся артикли (о них вы прочтете далее), которые зависят от рода и числа существительного  

Вот несколько существительных, которые следует выучить в этом уроке



''')


rule2 = dcc.Markdown('''
  Обратите внимание на то, что род существительных в русском языке и в немецком очень часто не совпадает. Есть ли какие-то способы, чтобы 
  различать существительные по родам, не запоминая все наизусть?
 #### Да, есть несколько способов  
  ##### 1. Значение  
  Опознать существительно по роду иногда помогает значение этого существительного.
 Например, слово _Mann (мужчина)_ по своему значению, очевидно, имеет мужской род. Слово _Frau (женщина)_, как легко догадаться, женского рода. 
 Однако слово  _Mädchen (девочка)_ подобной логике не поддается - это слово среднего рода!
  И все же, рассмотрим категории слов, значение которых всегда однозначно определяет их род 

''')

                 



Word_table_header = [
    html.Thead(html.Tr([html.Th("Maskulinum",  style={'background-color':'PaleTurquoise'}), html.Th("Femininum",  style={'background-color':'Pink'}), html.Th('Neutrum', style={'background-color':'PapayaWhip'})]))
]

row1 = html.Tr([html.Td('''Tisch (стол)'''), html.Td("Lampe (лампа)"), html.Td("Buch (книга)")])
row2 = html.Tr([html.Td("Stuhl (стул)"), html.Td("Tasche (сумка)"), html.Td("Bild (картина)")])
row3 = html.Tr([html.Td("Schrank (шкаф)"), html.Td("Blume (цветок)"), html.Td("Wort (слово)")])
row4 = html.Tr([html.Td("Stift (карандаш)"), html.Td("Vase (ваза)"), html.Td("Haus (дом)")])
row5 = html.Tr([html.Td('''Computer (компьютер)'''), html.Td("Straße (улица)"), html.Td("Zimmer (комната)")])
row6 = html.Tr([html.Td("Wagen (машина)"), html.Td("Übung (упражнение)"), html.Td("Kind (ребенок)")])
row7 = html.Tr([html.Td("Mensch (человек)"), html.Td("Zeitung (газета)"), html.Td("Mädchen (девочка)")])
row8 = html.Tr([html.Td("Lehrer (учитель)"), html.Td("Zeitschrift (журнал)"), html.Td("Spielzeug (игрушка)")])

Word_table_body = [html.Tbody([row1, row2, row3, row4,row5, row6, row7, row8])]

Word_table = dbc.Table(Word_table_header + Word_table_body, bordered=True, size='sm')

male_meanings=[ html.H5("Мужской род", style={'color':"blue"}),
                                 dcc.Markdown('''
                                  - лица мужского пола
                                  - стороны света
                                  - вермена года
                                  - названия месяцев
                                  - дни недели
                                  - камни и минералы
                                  - названия автомобильных марок
                                  - названия гор
                                  - названия озер
                                 ''')]

female_meanings=[ html.H5("Женский род", style={'color':'red'}),
                                  dcc.Markdown('''
                                  - лица женского пола, кроме _das Mädchen (девочка)_
                                  - название деревьев, кроме _der Ahorn (клен)_
                                  - названия деревьев, кроме _der Mohn (мак)_ _der Kaktus(кактус)_
                                  - названия ягод
                                  - названия фруктов и овощей, кроме _der Apfel (яблоко)_, _der Pfirsich (персик)_, _der Kohl (капуста)_ и _der Kürbis (тыква)_
                                  - большинство немецких рек, кроме _der Rhein_, _der Main_ и _der Neckar_
                                  ''') ]

male_form = [html.H5('Мужской род', style={'color':'blue'}),
             dcc.Markdown('''
             ###### Существительные с суффиксами:
             - _er_ - der Lehr_er_
             - _ler_ - der Sport_ler_
             - _ner_ - der Amerika_ner_
             - _ling_ - der Lehr_ling_
             - _s_ - der Fuch_s_

             ###### Иностранные слова (в осн. одушевленные) с суффиксами:
              - _ent_ - der Stud_ent_
              - _ant_ - der Labor_ant_
              - _ist_ - der Publiz_ist_
              - _et_ - der Po_et_
              - _ot_ - der Pil_ot_
              - _at_ - der Kandid_at_
              - _soph_ - der Philo_soph_
              - _nom_ - der Astro_nom_
              - _graph_ - der Photo_graph_
              - _eur_ - der Ingeni_eur_
              - _ier_ - der Pion_ier_
              - _ar_  - der Jibil_ar_
              - _är_ - der Sekret_är_
              - _or_ - der Dokt_or_

             ''')
             ]

female_form=[ html.H5('Женский род', style={'color':'red'}),
                dcc.Markdown('''
                  ###### Существительные с суффиксами:
                  - _in_ - die Student_in_ 
                  - _ung_ - die Üb_ung_  
                  - _heit_ - die Frei_heit_ 
                  - _keit_ - die Neuige_keit_ 
                  - _schaft_ - die Land_schaft_  
                  - _ei_ - die Maler_ei_  

                  ###### Иностранные слова с ударными суффиксами:

                  - _ie_ - die Chem_ie_
                  - _tät_ - die Universi_tät_
                  - _tion_ - die Sta_tion_
                  - _ur_ - die Kult_ur_
                  - _ik_ - die Phys_ik_
                  - _age_ - die Report_age_
                  - _ade_ - die Fass_ade_
                  - _anz_ - die Ambul_anz_
                  - _enz_ - die Exist_enz_





                ''')
              ]

neutrim_form = [html.H5("Средний род", style={'color':'green'}),
                dcc.Markdown('''
                ###### Существительные с суффиксами:
                - _chen_ - das Mäd_chen_
                - _lein_ - das Tisch_lein_
                - _(s)tel_ - das Fünf_tel_
                - _tum_ - das Eigen_tum_, НО не все
                - _nis_ - das Erlaub_nis_, НО не все

                 ###### Иностранные слова (предметы и абстрактные понятия), оканчивающиеся на:
                 - _(i)um_ - das Stad_ium_
                 - _ett_ - das Kabin_ett_
                 - _ment_  - das Doku_ment_
                 - _ma_ - das Dra_ma_
                 - _o_ - das Kin_o_

                  ###### Существительные с приставкой _Ge_:
                  - das *Ge*birge
                  - das *Ge*mälde
                ''')
                ]
rule3 = dcc.Markdown('''
 ##### 2. Форма слова
 Также определить род некоторых существительных можно ориентируясь на их форму - 
 о родовой принадлежности обычно говорят суффиксы существительных. Однако и здесь есть свои исключения
''')

rule4 = dcc.Markdown('''
    Итак, существуют некоторые признаки, по которым можно определить род некоторых существительных. 
    Однако далеко не все существительные немецкого языка имеют такие отличительные черты, которые 
    были перечислены выше. Поэтому в большинстве случаев род существительного - это просто то, что нужно запомнить.

    ## Артикли 
    В зависимости от рода и числа существительного, будет меняться и артикль перед ним

   - _Неопределенный артикль_ указывает на то, что предмет неизвестен, является одним из себе подобных
    или упоминается впервые.  
   - _Определенный артикль_ указывает на то, что речь идет о конкретном предмете или на то, что о нем ранее 
    упоминалось в контексте

''')

rule5=dcc.Markdown('''
## Указательные местоимения 

Это местоимения, которые переводятся на русский язык как _этот, эта, это, эти_. Они имеют, в зависимости от рода, те же окончания, что и определенный артикль

''')




Art_table_header = [
    html.Thead(html.Tr([html.Th(""), html.Th("Maskulinum",  style={'background-color':'PaleTurquoise'}), html.Th("Femininum",  style={'background-color':'Pink'}), html.Th('Neutrum', style={'background-color':'PapayaWhip'}), html.Th("Plural"),]))
]

row1 = html.Tr([html.Td('Неопределенный артикль'), html.Td('ein'), html.Td('eine'), html.Td("ein"), html.Td(" - ")])
row2 = html.Tr([html.Td('Определенный артикль'), html.Td('der '), html.Td("die"), html.Td("das"), html.Td("die")])


Art_table_body = [html.Tbody([row1, row2])]

Art_table = dbc.Table(Art_table_header + Art_table_body, bordered=True, size='sm')


Mest_table_header = [
    html.Thead(html.Tr([ html.Th("M",  style={'background-color':'PaleTurquoise'}), html.Th("F",  style={'background-color':'Pink'}), html.Th('N', style={'background-color':'PapayaWhip'}), html.Th("Plural"),]))
]

row1 = html.Tr([html.Td('dieser'), html.Td('diese'), html.Td('dieses'), html.Td("diese")])

Mest_table_body = [html.Tbody([row1])]

Mest_table = dbc.Table(Mest_table_header + Mest_table_body, bordered=True, size='sm')

rule6=dcc.Markdown('''
## Личные местоимения
''')

Per_table_header = [
    html.Thead(html.Tr([html.Th("Singular", style={'background-color':'PaleGreen'}),   html.Th("Plural", style={'background-color':'Thistle'}),]))
]

row1 = html.Tr([html.Td('ich (я) '), html.Td('wir (мы) ')])
row2 = html.Tr([html.Td('du ( ты)'), html.Td('ihr (вы)')])
row3 = html.Tr([html.Td('er (он), sie (она), es (оно)'), html.Td('sie (они), Sie (Вы)')])


Per_table_body = [html.Tbody([row1, row2, row3])]

Per_table = dbc.Table(Per_table_header + Per_table_body, bordered=True, size='sm')

rule7=dcc.Markdown('''
 Как и в русском, в немецком языке есть личное местоимение в вежливой форме - Sie (Вы). Это местоимение всегда пишется с большой буквы.
Оно используется как при обращении к одному человеку, так и 
 при обращении к группе лиц, к которым говорящий обращается на "Вы". Местоимение  ihr применяется только для обращения к 2 и более людями,
 с котрыми говорящий на "ты": к друзьям, детям, родственникам и т.п.

 ## Глагол sein

 Sein переводится как _быть_. Это глагол связка, он ставится в предложении на место сказуемого в том случае, если другого глагола нет. 
 Этот глагол меняет свою форму в зависимости от того, с каким личным местоимением употребляется.
''')

Sein_table_header = [
    html.Thead(html.Tr([html.Th("Singular", style={'background-color':'PaleGreen'}),   html.Th("Plural", style={'background-color':'Thistle'}),]))
]

row1 = html.Tr([html.Td(dcc.Markdown(''' ich - _bin_''')), html.Td(dcc.Markdown('''wir - _sind_'''))])
row2 = html.Tr([html.Td(dcc.Markdown(''' du - _bist_''')), html.Td(dcc.Markdown('''ihr - _seid'''))])
row3 = html.Tr([html.Td(dcc.Markdown('''er, sie, es - _ist_''')), html.Td(dcc.Markdown('''sie, Sie - _sind_'''))])


Sein_table_body = [html.Tbody([row1, row2, row3])]

Sein_table = dbc.Table(Sein_table_header + Sein_table_body, bordered=True, size='sm')

rule8=dcc.Markdown('''
    ## Словарь (прилагательные)
    Вот несколько слов, которые также необходимо выучить
     ##### groß - _большой_
     ##### klein - _маленький_
     ##### neu - _новый_
     ##### alt - _старый_
     ##### gut - _хороший, добрый_
     ##### schlecht - _плохой_
     ##### schön - _красивый_
     ##### interessant - _интересный_
     ##### weiß - _белый_ 
     ##### **schwarz** - _черный_
     ##### rot - _красный_
     ##### blau - _голубой, синий_
     ##### grün - _зеленый_
     ##### grau - _серый_
     ##### braun - _коричневый_
     ##### gelb - _желтый_
''')



layout=html.Div(
    [   
        html.Div(
               navbar
        ) ,

        html.Div(
            [   
                dbc.Row (
                    [
                        dbc.Col(
                               [  rule1,
                                  Word_table,
                                  rule2,
                                 
                                   ]
                            )
                        
                        
                        ]
                    
                    ),

                 dbc.Row (
                     [
                         dbc.Col( 
                             male_meanings,
                            
                             ),
                         dbc.Col(
                             female_meanings,  
                              
                             
                             ),
                        
                        
                         ]
                     ),

                 dbc.Row(
                     [
                         rule3,
                         dbc.Col(
                                male_form,
                             ),
                          dbc.Col(
                                female_form,
                             ),
                           dbc.Col(
                                neutrim_form,
                             )
                         ]
                     ),
                 dbc.Row(
                     [
                         rule4,
                         Art_table,
                         rule5,
                         Mest_table,
                         rule6,
                         Per_table, 
                         rule7,
                         Sein_table,
                         rule8
                         ]
                     )
                
                ] ,

                style={'padding':'20px'}
            )
        
        ]
    
    )





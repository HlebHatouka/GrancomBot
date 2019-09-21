import sqlite3

def get_creator(name):
    creator = """CREATE TABLE {0}
                     (id integer PRIMARY KEY,
                    question text,
                    answer text
                    ); """.format(name)
    return creator

def table_creation(connection, creator):
    table_cursor = connection.cursor()
    table_cursor.execute(creator)

def get_adder(name, id, question, answer):
    adder = """INSERT INTO {0}
            VALUES ( {1} , "{2}" , "{3}" );""".format(name, id, question, answer)
    return adder

def table_adding(connection, adder):
    table_cursor = connection.cursor()
    table_cursor.execute(adder)

def set_bel_greeting():
    greeting = '''Добра :-)\nУвядзіце каманду /help , каб даведацца больш, 
    або проста задайце пытанне.'''
    return greeting

def set_rus_greeting():
    greeting = '''Хорошо :-)\nВведите команду /help , чтобы узнать больше,
            или просто задайте вопрос.'''
    return greeting

def set_eng_greeting():
    greeting = '''Good :-)\nEnter the command /help to get more information
            or just ask me.'''
    return greeting

def set_bel_helping():
    helping = (
        'Я дапамагу Вам знайсці адказы на некаторыя пытанні!\n'
        'Увядзіце нумар пытання, што Вас цікавіць.\n\n' ,
        'Увядзіце каманду /exit , каб пакінуць выбар і задаць ўласнае пытанне.'
    )
    return helping

def set_rus_helping():
    helping = (
        'Я помогу Вам найти ответы на некоторые вопросы!\n'
        'Введите номер интересующего Вас вопроса.\n\n' ,
        'Введите команду /exit , чтобы оставить выбор и задать собственный вопрос.'
    )
    return helping

def set_eng_helping():
    helping = (
        'I can help you to find the answers to some questions!\n'
        'Enter the number of question that interests you.\n\n' ,
        'Enter the command /exit to leave choice menu and ask your own question.'
    )
    return helping

def set_bel_error():
    error = '''Увядзіце нумар пытання або /exit , каб выйсці
        і задаць сваё ўласнае пытанне!'''
    return error

def set_rus_error():
    error = '''Введите номер вопроса или /exit , чтобы выйти
            и задать свой собственный вопрос!'''
    return error

def set_eng_error():
    error = '''Enter the number of question or /exit to leave
            and ask your own question!'''
    return error

def set_bel_questions():
    questions = (
        '1. Якія скутары ў вас можна набыць?',
        '2. Якія дакуманты вы даяце?',
        '3. Дзе вы знаходзіцеся, дзе паглядзець мотатэхніку?',
        '4. Ці даяце вы гарантыю на мотатэніку, якую прадаяце?',
        '5. Ці можна ў вас замовіць тэхніку, якой у вас няма на сайце і як доўга чакаць дастаўкі з Японіі?',
        '6. Ці можаце вы дапамагчы набыць новую або аднавіць старую батарэю для электраскутара Yamaha?',
        '7. Чым японскія электраскутары б/у лепшыя за новых кітайскіх?',
    )
    return questions

def set_bel_answers():
    answers = (
        "Кампанія ГРАНКАМ прадае толькі якасныя "+
            "скутары і матацыклы японскіх брэндаў, прывезеныя непасрэдна з японскага рынку.",
        "Пры продажу пакупнік атрымоўвае ўсе неабходныя "+
            "дакуманты для пастаноўкі на ўлік у ДАІ (калі яна патрабуецца), "+
            "а менавіта: дамова куплі-продажу, арыгінальную мытную дэкларацыю, "+
            "пасведчанне бяспекі транспартнага сродка і на мотатэхніку "+
            "з рухавікамі не больш за 100 куб. см рахунак-даведку.",
        "На дадзены момант склады знаходзяцца ў г. Мінску "+
            "на тэрыторыі базы «Белгасганд» па вул. Платонава, 34.",
        "Так, мы прадаем тэхніку ў належным стане, "+
            "падрыхтаваную да продажу і даем гарантыю на схаваныя "+
            "дэфекты, якія не выявілі. У дамове куплі-продажу "+
            "прапісаныя ўмовы гарантыі.",
        "Так. можна замовіць любую тэхніку з японскага рынку. "+
            "Дастаўка займае прыкладна на працягу 70 дзён пасля адгрузкі "+
            "(50 дзён кантэйнер ідзе да порта Клайпеды, цягам тыдня дастаўляецца "+
            "ў Мінск і праходзе мытныя працэдуры, затым адмыслоўцы "+
            "акрэдытаванай арганізаціі аглядаюць і правяраюць транспартныя "+
            "сродкі і выдаюць пасведчанне бяспекі. Пасля гэтага мы аддаем заказніку).",
        "Так, мы можам дапамагчы набыць любыя запасныя "+
            "часткі тэхнікі, якую прадаем, у тым ліку і батарэі "+
            "для электраскутараў; таксама можам замяніць элементы "+
            "у старой, што будзе ўтрая таней, чым набыць новую.",
        "Больш інфармацыі па японскім электраскутарам "+
            "вы можаце знайсці на нашым асобным сайце http://electroskuter.by/",
    )
    return answers

def set_rus_questions():
    questions = (
        '1.  Какие скутеры у вас можно купить?',
        '2.  Какие документы вы даёте?',
        '3.  Где вы находитесь, где посмотреть мототехнику?',
        '4.  Даёте ли вы гарантию на мототехнику, которую продаёте?',
        '5.  Можно ли у вас заказать технику, которой у вас нет на сайте и как долго ждать доставки из Японии?',
        '6.  Можете ли вы помочь купить новую или восстановить старую батарею для электроскутера Yamaha?',
        '7.  Чем японские электроскутеры б/у лучше новых китайских?',
    )
    return questions

def set_rus_answers():
    answers = (
        "Компания ГРАНКОМ продает только качественные "+
            "скутеры и мотоциклы японских брендов, привезенные непосредственно с японского рынка.",
        "При продаже покупатель получает все необходимые "+
            "документы для постановки на учет в ГАИ (если она требуется), "+
            "а именно: договор купли-продажи, оригинальную таможенную декларацию, "+
            "свидетельство безопасности транспортного средства и на мототехнику "+
            "с двигателями более 100 куб. см счет-справку.",
        "На данный момент склады находятся в г. Минске "+
            "на территории базы «Белхозторг» по ул. Платонова, 34.",
        "Да, мы продаем технику в надлежащим состоянии, "+
            "подготовленную к продаже и даем гарантию на скрытые "+
            "дефекты, которые не выявили. В договоре купли-продажи "+
            "прописаны условия гарантии.",
        "Да. Можно заказать любую технику с японского рынка. "+
            "Доставка занимает примерно в течении 70 дней после отгрузки "+
            "(50 дней контейнер идет до порта Клайпеды, в течении недели "+
            "доставляется в Минск и проходит таможенные процедуры, затем "+
            "прибывает на склад компании, проходит проверку, затем специалисты "+
            "аккредитованной организации осматривают и проверяют транспортные "+
            "средства и выдают свидетельства безопасности. После этого мы отдаем заказчику).",
        "Да, мы можем помочь купить любые запасные "+
            "части к технике, которую продаем, в том числе и "+
            "батареи для электроскутеров, также можем заменить "+
            "элементы в старой, что будет втрое дешевле чем купить новую.",
        "Больше информации по японским электроскутерам "+
            "вы можете получить на отдельном нашем сайте http://electroskuter.by/",
    )
    return answers

def set_eng_questions():
    questions = (
        '1. What scooters can I buy?',
        '2. What documents do you give?',
        '3. Where are you at, where to see motorcycles?',
        '4. Do you give a guarantee for the motorcycles that you sell?',
        '5. Can I order equipment that you do not have on the site and how long to wait for delivery from Japan?',
        '6. Can you help buy a new or restore an old battery for a Yamaha electric scooter?',
        '7. Why are used (second hand) Japanese electric scooters bettes than new Chinese ones?',
    )
    return questions

def set_eng_answers():
    answers = (
        "GRANCOM company sells only high-quality "+
            "scooters and motorcycles of Japanese brands brought directly from the Japanese market.",
        "When selling, the buyer receives all the necessary "+
            "documents for registration with the traffic police (if required), "+
            "namely: the purchase agreement, the original customs declaration, "+
            "vehicle safety certificate and invoice statement for motorcycle equipment "+
            "with engines of more than 100 cubic centimeters.",
        "At the moment, the warehouses are located in Minsk "+
            "on the territory of the Belhashand (Belhoztorg) base on Platonov st., 34.",
        "Yes, we sell equipment in good condition, "+
            "prepared for sale and give a guarantee for hidden defects "+
            "that are not revealed. The terms of the guarantee are stated in the sales contract.",
        "Yes. You can order any equipment from the Japanese market. "+
            "Delivery takes approximately 70 days after shipment "+
            "(50 days the container goes to the port of Klaipeda, is delivered to "+
            "Minsk within a week and undergoes customs procedures, then arrives at "+
            "the company's warehouse, is checked, then the experts of the accredited "+
            "organization inspect and check the vehicles and issue safety certificates. "+
            "After that we give it to the customer).",
        "Yes, we can help to buy any spare parts for "+
            "equipment that we sell, including batteries for electric "+
            "scooters, we can also replace elements in the old equipment, "+
            "it will be three times cheaper than buying a new one.",
        "You can get more information about Japanese "+
            "electric scooters on our separate website http://electroskuter.by/",
    )
    return answers

if __name__ == "__main__":

    table = "questions.sqlite"

    bel_table_name = "bel"
    rus_table_name = "rus"
    eng_table_name = "eng"

    table_connect = sqlite3.connect(table)

    table_creation(table_connect, get_creator(bel_table_name))
    table_creation(table_connect, get_creator(rus_table_name))
    table_creation(table_connect, get_creator(eng_table_name))

    bel_greeting = set_bel_greeting()
    rus_greeting = set_rus_greeting()
    eng_greeting = set_eng_greeting()

    bel_helping = set_bel_helping()
    rus_helping = set_rus_helping()
    eng_helping = set_eng_helping()

    bel_error = set_bel_error()
    rus_error = set_rus_error()
    eng_error = set_eng_error()

    bel_questions = set_bel_questions()
    rus_questions = set_rus_questions()
    eng_questions = set_eng_questions()

    bel_answers = set_bel_answers()
    rus_answers = set_rus_answers()
    eng_answers = set_eng_answers()

    for i in range(7):
        adder = get_adder(bel_table_name, i+1, bel_questions[i], bel_answers[i])
        table_adding(table_connect, adder)
    for i in range(7):
        adder = get_adder(rus_table_name, i+1, rus_questions[i], rus_answers[i])
        table_adding(table_connect, adder)
    for i in range(7):
        adder = get_adder(eng_table_name, i+1, eng_questions[i], eng_answers[i])
        table_adding(table_connect, adder)

    table_connect.commit()
    table_connect.close()

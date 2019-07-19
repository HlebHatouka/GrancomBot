import telebot
from telebot import types

bot = telebot.TeleBot('token')
language = str()

@bot.message_handler(commands=['start'])
def start_message(message):
    greeting = "Welcome! I'm GrancomBot!"
    keyboard = types.InlineKeyboardMarkup()

    key_eng = types.InlineKeyboardButton(text='English', callback_data='eng')
    keyboard.add(key_eng)

    key_bel = types.InlineKeyboardButton(text='Беларуская', callback_data='bel')
    keyboard.add(key_bel)

    key_rus = types.InlineKeyboardButton(text='Русский', callback_data='rus')
    keyboard.add(key_rus)
    bot.send_message(chat_id=message.chat.id, text=greeting, reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global language
    if call.data == "eng":
        language = "eng"
        bot.send_message(call.message.chat.id, 'Good :-)\nEnter the command /help to get more information ' +
            'or just ask me.')
    elif call.data == "bel":
        language = "bel"
        bot.send_message(call.message.chat.id, 'Добра :-)\nУвядзіце каманду /help , каб даведацца больш, '+
            'або проста задайце пытанне.')
    elif call.data == "rus":
        language = "rus"
        bot.send_message(call.message.chat.id, 'Хорошо :-)\nВведите команду /help , чтобы узнать больше, '+
            'или просто задайте вопрос.')

@bot.message_handler(commands=['help'])
def help_message(message):
    global language
    helping = Helping(language, message)
    helping.help(message)

@bot.message_handler(content_types=["text"])
def asking_message(message):
    bot.send_message(chat_id=message.chat.id, text = "You entered '"+message.text+"'")

class Helping:
    def __init__(self, lang, message):
        self.__lang = lang
        self.__message = message
    
    def help(self, message):
        self.__set_message(message)
        if self.__lang == "eng":   
            self.__eng_help()
        elif self.__lang == "bel":  
            self.__bel_help()
        elif self.__lang == "rus":
            self.__rus_help()
        self.__get_command()

    def __set_message(self, message):
        self.__message = message
        return self.__message
    
    def __get_command(self):
        bot.register_next_step_handler(self.__message, self.__get_number)

    def __stop_command (self):
        bot.clear_step_handler_by_chat_id(chat_id=self.__message.chat.id)

    @bot.message_handler(content_types=["text"])
    def __get_number(self, message):
        try:
            self.__set_message(message)
            if self.__message.text == "/exit":
                self.__stop_command()
                del self
                return
            if  int(self.__message.text) <= 7:
                number = int(self.__message.text) 
                if number == 1:
                    self.first()
                elif number == 2:
                    self.second()
                elif number == 3:
                    self.third()
                elif number == 4:
                    self.fourth()
                elif number == 5:
                    self.fifth()
                elif number == 6:
                    self.sexth()
                elif number == 7:
                    self.seventh()
            else:
                raise ValueError()
            self.__get_command()
        except ValueError:
            self.__error_occured()
        
    def __error_occured(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "Enter the number of question or /exit to leave!")
        if self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Увядзіце нумар пытання або /exit , каб выйсці!")
        if self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "Введите номер вопроса или /exit , чтобы выйти!")
        self.__get_command()
        
    def __eng_help(self):
        bot.send_message(chat_id=self.__message.chat.id, text = 'I can help you to find the answers to some questions!\n'
        'Enter the number of question that interests you.\n\n'
        '1. What scooters can I buy?\n'
        '2. What documents do you give?\n'
        '3. Where are you at, where to see motorcycles?\n'
        '4. Do you give a guarantee for the motorcycles that you sell?\n'
        '5. Can I order equipment that you do not have on the site and how long to wait for delivery from Japan?\n'
        '6. Can you help buy a new or restore an old battery for a Yamaha electric scooter?\n'
        '7. Than used (second hand) Japanese electric scooters than new Chinese ones?\n\n'
        'Enter the command /exit to leave choice menu and ask your own question.')

    def __bel_help(self):
        bot.send_message(chat_id=self.__message.chat.id, text = 'Я дапамагу Вам знайсці адказы на некаторыя пытанні!\n'
        'Увядзіце нумар пытання, што Вас цікавіць.\n\n'
        '1. Якія скутары ў вас можна набыць?\n'
        '2. Якія дакуманты вы даяце?\n'
        '3. Дзе вы знаходзіцеся, дзе паглядзець мотатэхніку\n'
        '4. Ці даяце вы гарантыю на мотатэніку, якую прадаяце?\n'
        '5. Ці можна ў вас замовіць тэхніку, якой у вас няма на сайце і як доўга чакаць дастаўкі з Японіі\n'
        '6. Ці можаце вы дапамагчы набыць новую або аднавіць старую батарэю для электраскутара Yamaha?\n'
        '7. Чым японскія электраскутары б/у лепшыя за новых кітайскіх?\n\n'
        'Увядзіце каманду /exit , каб пакінуць выбар і задаць ўласнае пытанне.')

    def __rus_help(self):
        bot.send_message(chat_id=self.__message.chat.id, text = 'Я помогу Вам найти ответы на некоторые вопросы!\n'
        'Введите номер интересующего Вас вопроса.\n\n'
        '1.  Какие скутеры у вас можно купить?\n'
        '2.  Какие документы вы даёте?\n'
        '3.  Где вы находитесь, где посмотреть мототехнику?\n'
        '4.  Даёте ли вы гарантию на мототехнику, которую продаёте?\n'
        '5.  Можно ли у вас заказать технику, которой у вас нет на сайте и как долго ждать доставки из Японии?\n'
        '6.  Можете ли вы помочь купить новую или восстановить старую батарею для электроскутера Yamaha?\n'
        '7.  Чем японские электроскутеры б/у лучше новых китайских?\n\n'
        'Введите команду /exit , чтобы оставить выбор и задать собственный вопрос.')

    def first(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "GRANCOM company sells only high-quality "+
            "scooters and motorcycles of Japanese brands brought directly from the Japanese market.")
        elif self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Кампанія ГРАНКАМ прадае толькі якасныя "+
            "скутары і матацыклы японскіх брэндаў, прывезеныя непасрэдна з японскага рынку.")
        elif self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "Компания ГРАНКОМ продает только качественные "+
            "скутеры и мотоциклы японских брендов, привезенные непосредственно с японского рынка.")

    def second(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "When selling, the buyer receives all the necessary "+
            "documents for registration with the traffic police (if required), "+
            "namely: the purchase agreement, the original customs declaration, "+
            "vehicle safety certificate and invoice statement for motorcycle equipment "+
            "with engines of more than 100 cubic centimeters.")
        elif self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Пры продажу пакупнік атрымоўвае ўсе неабходныя "+
            "дакуманты для пастаноўкі на ўлік у ДАІ (калі яна патрабуецца), "+
            "а менавіта: дамова куплі-продажу, арыгінальную мытную дэкларацыю, "+
            "пасведчанне бяспекі транспартнага сродка і на мотатэхніку "+
            "з рухавікамі не больш за 100 куб. см рахунак-даведку.")
        elif self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "При продаже покупатель получает все необходимые "+ 
            "документы для постановки на учет в ГАИ (если она требуется), "+
            "а именно: договор купли-продажи, оригинальную таможенную декларацию, "+
            "свидетельство безопасности транспортного средства и на мототехнику "+
            "с двигателями более 100 куб. см счет-справку.")

    def third(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "At the moment, the warehouses are located in Minsk "+
            "on the territory of the Belhashand (Belhoztorg) base on Platonov st., 34.")
        elif self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "На дадзены момант склады знаходзяцца ў г. Мінску "+
            "на тэрыторыі базы «Белгасганд» па вул. Платонава, 34.")
        elif self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "На данный момент склады находятся в г. Минске "+
            "на территории базы «Белхозторг» по ул. Платонова, 34.")

    def fourth(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "Yes, we sell equipment in good condition, "+
            "prepared for sale and give a guarantee for hidden defects "+
            "that are not revealed. The terms of the guarantee are stated in the sales contract.")
        elif self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Так, мы прадаем тэхніку ў належным стане, "+
            "падрыхтаваную да продажу і даем гарантыю на схаваныя "+
            "дэфекты, якія не выявілі. У дамове куплі-продажу "+
            "прапісаныя ўмовы гарантыі.")
        elif self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "Да, мы продаем технику в надлежащим состоянии, "+
            "подготовленную к продаже и даем гарантию на скрытые "+
            "дефекты, которые не выявили. В договоре купли-продажи "+
            "прописаны условия гарантии.")

    def fifth(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "Yes. You can order any equipment from the Japanese market. "+
            "Delivery takes approximately 70 days after shipment "+
            "(50 days the container goes to the port of Klaipeda, is delivered to "+
            "Minsk within a week and undergoes customs procedures, then arrives at "+
            "the company's warehouse, is checked, then the experts of the accredited "+
            "organization inspect and check the vehicles and issue safety certificates. "+
            "After that we give it to the customer).")
        elif self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Так. можна замовіць любую тэхніку з японскага рынку. "+
            "Дастаўка займае прыкладна на працягу 70 дзён пасля адгрузкі "+
            "(50 дзён кантэйнер ідзе да порта Клайпеды, цягам тыдня дастаўляецца "+
            "ў Мінск і праходзе мытныя працэдуры, затым адмыслоўцы "+
            "акрэдытаванай арганізаціі аглядаюць і правяраюць транспартныя "+
            "сродкі і выдаюць пасведчанне бяспекі. Пасля гэтага мы аддаем заказніку).")
        elif self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "Да. Можно заказать любую технику с японского рынка. "+
            "Доставка занимает примерно в течении 70 дней после отгрузки "+
            "(50 дней контейнер идет до порта Клайпеды, в течении недели "+
            "доставляется в Минск и проходит таможенные процедуры, затем "+
            "прибывает на склад компании, проходит проверку, затем специалисты "+
            "аккредитованной организации осматривают и проверяют транспортные "+
            "средства и выдают свидетельства безопасности. После этого мы отдаем заказчику).")

    def sexth(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "Yes, we can help to buy any spare parts for "+
            "equipment that we sell, including batteries for electric "+
            "scooters, we can also replace elements in the old equipment, "+
            "it will be three times cheaper than buying a new one.")
        elif self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Так, мы можам дапамагчы набыць любыя запасныя "+
            "часткі тэхнікі, якую прадаем, у тым ліку і батарэі "+
            "для электраскутараў; таксама можам замяніць элементы "+
            "у старой, што будзе ўтрая таней, чым набыць новую.")
        elif self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "Да, мы можем помочь купить любые запасные "+
            "части к технике, которую продаем, в том числе и "+
            "батареи для электроскутеров, также можем заменить "+
            "элементы в старой, что будет втрое дешевле чем купить новую.")

    def seventh(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "You can get more information about Japanese "+
            "electric scooters on our separate website http://electroskuter.by/")
        elif self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Больш інфармацыі па японскім электраскутарам "+
            "вы можаце знайсці на нашым асобным сайце http://electroskuter.by/")
        elif self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "Больше информации по японским электроскутерам "+
            "вы можете получить на отдельном нашем сайте http://electroskuter.by/")
            
bot.polling(none_stop=True)

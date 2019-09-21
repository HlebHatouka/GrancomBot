import telebot
from telebot import types
import sqlite3
#import mysql.connector

bot = telebot.TeleBot('942160466:AAF2PUbUMAvlWpODUw9qdinDlG9NMChC09M')
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
        self.__table = "questions.sqlite"

    def help(self, message):
        self.__set_message(message)
        connection = self.__create_connection(self.__table)
        if self.__lang == "eng":
            self.__eng_help(connection)
        elif self.__lang == "bel":
            self.__bel_help(connection)
        elif self.__lang == "rus":
            self.__rus_help(connection)
        self.__dissable_connection(connection)
        self.__get_command()

    def __set_message(self, message):
        self.__message = message
        return self.__message

    def __get_command(self):
        bot.register_next_step_handler(self.__message, self.__get_number)

    def __stop_command (self):
        bot.clear_step_handler_by_chat_id(chat_id=self.__message.chat.id)

    def __create_connection(self, path):
        return sqlite3.connect(path)

    def __get_questions(self, connection, name):
        table_cursor = connection.cursor()
        table_cursor.execute("SELECT question FROM {0}".format(name))
        results = table_cursor.fetchall()
        return results

    def __get_answer(self, connection, name, number):
        table_cursor = connection.cursor()
        table_cursor.execute("SELECT answer FROM {0} WHERE id = {1}".format(name, number))
        results = table_cursor.fetchall()
        return results

    def __dissable_connection(self, connection):
        connection.close()

    @bot.message_handler(content_types=["text"])
    def __get_number(self, message):
        try:
            self.__set_message(message)
            if self.__message.text == "/exit":
                self.__stop_command()
                del self
                return
            if 0 < int(self.__message.text) <= 7:
                number = int(self.__message.text)
                self.__answer(number)
            else:
                raise ValueError()
            self.__get_command()
        except ValueError:
            self.__error_occurred()

    def __error_occurred(self):
        if self.__lang == "eng":
            bot.send_message(chat_id=self.__message.chat.id, text = "Enter the number of question or /exit to leave "+
            "and ask your own question!")
        if self.__lang == "bel":
            bot.send_message(chat_id=self.__message.chat.id, text = "Увядзіце нумар пытання або /exit , каб выйсці "+
            "і задаць сваё ўласнае пытанне!")
        if self.__lang == "rus":
            bot.send_message(chat_id=self.__message.chat.id, text = "Введите номер вопроса или /exit , чтобы выйти "+
            "и задать свой собственный вопрос!")
        self.__get_command()

    def __eng_help(self, connection):
        questions = self.__get_questions(connection, self.__lang)
        bot.send_message(chat_id=self.__message.chat.id, text = 'I can help you to find the answers to some questions!\n'
        'Enter the number of question that interests you.\n\n')
        for question in questions:
            bot.send_message(chat_id=self.__message.chat.id, text = question)
        bot.send_message(chat_id=self.__message.chat.id, text = 'Enter the command /exit to leave choice menu and ask your own question.')

    def __bel_help(self, connection):
        questions = self.__get_questions(connection, self.__lang)
        bot.send_message(chat_id=self.__message.chat.id, text = 'Я дапамагу Вам знайсці адказы на некаторыя пытанні!\n'
        'Увядзіце нумар пытання, што Вас цікавіць.\n\n')
        for question in questions:
            bot.send_message(chat_id=self.__message.chat.id, text = question)
        bot.send_message(chat_id=self.__message.chat.id, text = 'Увядзіце каманду /exit , каб пакінуць выбар і задаць ўласнае пытанне.')

    def __rus_help(self, connection):
        questions = self.__get_questions(connection, self.__lang)
        bot.send_message(chat_id=self.__message.chat.id, text = 'Я помогу Вам найти ответы на некоторые вопросы!\n'
        'Введите номер интересующего Вас вопроса.\n\n')
        for question in questions:
            bot.send_message(chat_id=self.__message.chat.id, text = question)
        bot.send_message(chat_id=self.__message.chat.id, text = 'Введите команду /exit , чтобы оставить выбор и задать собственный вопрос.')

    def __answer(self, number):
        connection = self.__create_connection(self.__table)
        answer = self.__get_answer(connection, self.__lang, number)
        bot.send_message(chat_id=self.__message.chat.id, text = answer)
        self.__dissable_connection(connection)

bot.polling(none_stop=True)

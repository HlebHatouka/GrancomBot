import telebot
from telebot import types
import sqlite3

#set your bot token here
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
        self.__question_table = "questions.sqlite"
        self.__help_table = "help.sqlite"

    def help(self, message):
        self.__set_message(message)
        question_connection = self.__create_connection(self.__question_table)
        help_connection = self.__create_connection(self.__help_table)
        self.__get_help(question_connection, help_connection)
        self.__dissable_connection(question_connection)
        self.__dissable_connection(help_connection)
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

    def __get_from_question_table(self, what, name, number):
        connection = self.__create_connection(self.__question_table)
        table_cursor = connection.cursor()
        table_cursor.execute("SELECT {0} FROM {1} WHERE id = {2}".format(what, name, number))
        result = table_cursor.fetchall()
        self.__dissable_connection(connection)
        return result

    def __get_from_help_table(self, what, name):
        connection = self.__create_connection(self.__help_table)
        table_cursor = connection.cursor()
        table_cursor.execute("SELECT {0} FROM {1}".format(what, name))
        results = table_cursor.fetchall()
        self.__dissable_connection(connection)
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
        error = self.__get_from_help_table("error", self.__lang)
        bot.send_message(chat_id=self.__message.chat.id, text = error)
        self.__get_command()

    def __get_help(self, questions_connection, help_connection):
        questions = []
        helping = []
        for i in range(7):
            questions.append(self.__get_from_question_table("question", self.__lang, i+1))
        for i in range(2):
            helping.append(self.__get_from_help_table("helping", self.__lang))
        bot.send_message(chat_id=self.__message.chat.id, text = helping[0])
        for question in questions:
            bot.send_message(chat_id=self.__message.chat.id, text = question)
        bot.send_message(chat_id=self.__message.chat.id, text = helping[1]) 

    def __answer(self, number):
        connection = self.__create_connection(self.__question_table)
        answer = self.__get_from_question_table("answer", self.__lang, number)
        bot.send_message(chat_id=self.__message.chat.id, text = answer)
        self.__dissable_connection(connection)

bot.polling(none_stop=True)

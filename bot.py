# -*- coding: utf-8 -*-
import telebot
from telebot import types

API_TOKEN = '888229933:AAE2BRkblZM95jmLYeJQRxlqc9pQvHHwYms'

bot = telebot.TeleBot(API_TOKEN)

team_dict = {}


class Team:
	def __init__(self, name, id):
		self.name = name
		self.step = 0


#download from db
db = open("db.txt", "r")
for line in db:
	team_dict[line.split()[0]].step = line.split()[2]
db.close()


@bot.message_handler(commands=['admingetinfo'])
def send_info(message):
	db = open("db.txt", "r")
	for line in db:
		bot.send_message(message.chat_id, line)
	db.close()


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.send_message(message.chat_id, """\
Приветули, как называется твоя команда?
""")
	bot.register_next_step_handler(message, register_name_step)


def register_name_step(message):
	try:
		team = Team(message.text)
		team_dict[message.chat_id] = team
		bot.send_message(message.chat_id, "Готовы начать?")

		db = open("db.txt", "w")
		for key in dict.keys():
			db.write(key + str(team_dict[key].name) + str(team_dict[key].step) + "\n")
		db.close()

		bot.register_next_step_handler(message, questions_before_step)
	except Exception as e:
		bot.send_message(message.chat_id, "Я не понял, напиши название еще раз.")


def questions_before_step(message):
	if not message.text in {"Да"}:
		bot.send_message(message.chat_id, "Нет так нет... Но не откладывайте в долгий ящик!")
		bot.register_next_step_handler(message, questions_before_step)
		return
	team_dict[message.chat_id].step += 1

	db = open("db.txt", "w")
	for key in dict.keys():
		db.write(key + str(team_dict[key].name) + str(team_dict[key].step) + "\n")
	db.close()

	bot.send_message(message.chat_id, "Отлично, вот первое задание:")
	bot.send_document(message.chat_id, "BQADAgADFQMAAhn98UhgQ6aV6mCxdwI")
	bot.register_next_step_handler(message, questions_first_step)


def questions_first_step(message):
	if not message.text in {"space bottle", "spacebottle", "SPACE BOTTLE", "SPACEBOTTLE", "Spacebottle", "Space bottle"}:
		bot.send_message(message.chat_id, "Неверно, подумайте еще.")
		bot.register_next_step_handler(message, questions_first_step)
		return
	team_dict[message.chat_id].step += 1

	db = open("db.txt", "w")
	for key in dict.keys():
		db.write(key + str(team_dict[key].name) + str(team_dict[key].step) + "\n")
	db.close()

	bot.send_message(message.chat_id, "Браво! Пора приступать к следующему заданию:")
	bot.send_message(message.chat_id, """\
Японское поле 20x20

1
1 2
6 1
2 8
14
14 1
3 8 1
1 4 2
3 3 2
4 5
4 4
4 3 1
1 2 7
3 1 1 4 1
8 1
11 1
10 2
8
6
10

1 1 2
1 3 4
5 6
4 7
1 2 7
6 7
4 6
1 4 4 1
1 14 1
5 4 3 1
4 5 1 1
5 5 1 1
6 1
13
9
5
2 2
2 1
2 1
3 3
""")
	bot.register_next_step_handler(message, questions_second_step)



def questions_second_step(message):
        if not message.text in {"петух", "Петух"}:
                bot.send_message(message.chat_id, "Нет. Попробуйте еще.")
                bot.register_next_step_handler(message, questions_second_step)
                return
        team_dict[message.chat_id].step += 1

	db = open("db.txt", "w")
        for key in dict.keys():
                db.write(key + str(team_dict[key].name) + str(team_dict[key].step) + "\n")
        db.close()

	bot.send_message(message.chat_id, "Верно!")
	bot.message(message.chat_id, """\
На месте происшествия была найдена следующая записка. Что кроется в этом сообщении?

something sTrAnge is happening…
this mysteriOuS place,
 these incomprehEnSible things
  around mE aNd as A wHole…
i hope i“ll fix the sitUaTion.
have i timE yEt?
""")
        bot.register_next_step_handler(message, questions_third_step)


def questions_third_step(message):
        if not message.text in {"runaway", "RUNAWAY", "run away", "RUN AWAY", "Runaway", "Run away"}:
                bot.send_message(message.chat_id, "Нет, неизвестный хотел передать другое сообщение.")
                bot.register_next_step_handler(message, questions_third_step)
                return
        team_dict[message.chat_id].step += 1
        bot.send_message(message.chat_id, "Верно! После таких записок становится страшновато, правда? Но не волнуйтесь, лучше решите новое задание:")
        bot.send_document(message.chat_id, """\
Катя и Юра пытаются попасть на планету ВМК.
Для этого им необходимо пройти ворота с электронным замком.
В замке хранится таблица размером 3х8, заполненная целыми числами от 1 до 8.
В каждой строке встречаются все цифры от 1 до 8, а в столбце цифры не повторяются.
Будем называть такие таблицы Космическими прямоугольниками.
У Кати и Юры есть свои ключи в виде таблиц 4х8.
Замок откроется только в том случае, если замок и ключ можно дополнить одной строкой единственным образом так, чтобы дополненные прямоугольники так же являлись космическими.
Кто из ребят попадёт на планету ВМК?
Напишите чей ключ правильный и приведите строку, которой надо будет дополнить таблицы, чтобы пройти ворота.

Замок
6 5 8 3 1 2 7 4
1 7 5 2 4 6 8 3
2 6 1 4 8 3 5 7

Ключ Кати
8 6 3 5 1 4 7 2
1 3 7 8 2 6 4 5
4 7 1 2 5 3 8 6
5 8 4 6 7 2 1 3

Ключ Юры
2 4 3 7 8 5 6 1
1 2 7 6 4 3 5 8
4 1 6 2 7 8 3 5
5 8 2 1 3 4 7 6
""")
        bot.register_next_step_handler(message, questions_fourth_step)


def questions_fourth_step(message):
        if not message.text in {"Юра 8 3 4 5 6 7 1 2", "ключ Юры 8 3 4 5 6 7 1 2", "Ключ Юры 8 3 4 5 6 7 1 2"}:
                bot.send_message(message.chat_id, "Неверно, подумайте еще.")
                bot.register_next_step_handler(message, questions_third_step)
                return
        team_dict[message.chat_id].step += 1

	db = open("db.txt", "w")
        for key in dict.keys():
                db.write(key + str(team_dict[key].name) + str(team_dict[key].step) + "\n")
        db.close()

	bot.send_message(message.chat_id, "Да, Кате прийдется найти себе другой ключ, а Юра пройдет. Вот последнее задание:")
        bot.send_document(message.chat_id, """\
Find Honorificabilitudinitatibus in the biggest internet number
Открой на русском
Найди ответ на 1.1.4
Представь каждый символ цифрой

0000000010..010000
0..01000
00000010..0
000000010..01000000
010..010000
00000010010..0
0..
..
..0
""")
        bot.register_next_step_handler(message, questions_fifth_step)


def questions_fifth_step(message):
        if not message.text in {"вычисления", "Вычисления"}:
                bot.send_message(message.chat_id, "Нет, ПОИЩИТЕ получше.")
                bot.register_next_step_handler(message, questions_fifth_step)
                return
        team_dict[message.chat_id].step += 1

	db = open("db.txt", "w")
        for key in dict.keys():
                db.write(key + str(team_dict[key].name) + str(team_dict[key].step) + "\n")
        db.close()

        bot.send_message(message.chat_id, "Верно! Поздравляю, вы прошли все задания! Увидимся на квесте.")


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()

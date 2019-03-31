# -*- coding: utf-8 -*-
import telebot
from telebot import types

API_TOKEN = '888229933:AAE2BRkblZM95jmLYeJQRxlqc9pQvHHwYms'

bot = telebot.TeleBot(API_TOKEN)

team_dict = {}


class Team:
  def __init__(self, name):
    self.name = name
    self.step = int(0)


def send_info(message, info):
  bot.send_message("-396237929", str(info) + str(" : ") + str(message.chat.username) + str(" , ") + str(message.text))


"""#download from db
db = open("db.txt", "r")
for line in db:
  team_dict[line.split()[0]].step = line.split()[2]
db.close()"""


"""@bot.message_handler(commands=['admingetinfo'])
def send_info(message):
  db = open("db.txt", "r")
  for line in db:
    bot.send_message(message.chat.id, line)
  db.close()"""


@bot.message_handler(commands=['start'])
def send_welcome(message):
  msg = bot.send_message(message.chat.id, """\
Приветули, как мне вас называть?
""")
  bot.register_next_step_handler(msg, register_name_step)


def register_name_step(message):
  send_info(message, "name")
  team = Team(message.text)
  team_dict[message.chat.id] = team
  msg = bot.send_message(message.chat.id, """\
Я слышал, вы хотите узнать что-то о пропавших студентах?
Я расскажу вам всё, что знаю, но я должен быть уверен в том, что могу вам доверять.
Чтобы понять, почему пропали студенты, вы должны подготовиться, решив эти задания.
""")
  team_dict[message.chat.id].step += 1
  db = open("db.txt", "w")
  for key in team_dict:
    s = str(key) + str(team_dict[key].name) + str(team_dict[key].step) + str("\n")
    db.write(s)
  db.close()
  msg = bot.send_message(message.chat.id, "Начнем с чего-то совсем простого:")
  bot.send_message(message.chat.id, """\
На месте происшествия была найдена следующая записка. Что кроется в этом сообщении?

something sTrAnge is happening…
this mysteriOuS place,
 these incomprehEnSible things
  around mE aNd as A wHole…
i hope i'll fix the sitUaTion.
have i timE yEt?
""")
  bot.register_next_step_handler(msg, questions_first_step)


def questions_first_step(message):
  send_info(message, "one")
  if not message.text in {"runaway", "RUNAWAY", "run away", "RUN AWAY", "Runaway", "Run away"}:
    msg = bot.send_message(message.chat.id, "Неверно, подумайте еще.")
    bot.register_next_step_handler(msg, questions_first_step)
    return
  team_dict[message.chat.id].step += 1
  db = open("db.txt", "w")
  for key in team_dict:
    s = str(key) + str(team_dict[key].name) + str(team_dict[key].step) + str("\n")
    db.write(s)
  db.close()
  msg = bot.send_message(message.chat.id, "Отлично, а знаете про шифр Виженера?")
  bot.send_document(message.chat.id, "BQADAgADFQMAAhn98UhgQ6aV6mCxdwI")
  bot.register_next_step_handler(msg, questions_second_step)



def questions_second_step(message):
  send_info(message, "two")
  if not message.text in {"space bottle", "spacebottle", "SPACE BOTTLE", "SPACEBOTTLE", "Spacebottle", "Space bottle")
    msg = bot.send_message(message.chat.id, "Нет. Помните, важно подобрать верный ключ.")
    bot.register_next_step_handler(msg, questions_second_step)
    return
  team_dict[message.chat.id].step += 1
  db = open("db.txt", "w")
  for key in team_dict:
    s = str(key) + str(team_dict[key].name) + str(team_dict[key].step) + str("\n")
    db.write(s)
  db.close()
  msg = bot.send_message(message.chat.id, "Отлично, посмотрим, как вы справитесь с кроссвордом:")
  bot.send_message(message.chat.id, """\
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
  bot.register_next_step_handler(msg, questions_third_step)


def questions_third_step(message):
  send_info(message, "three")
  if not message.text in {"петух", "Петух"}:
    msg = bot.send_message(message.chat.id, "Неа, но вот посказка: сначала описаны столбцы.")
    bot.register_next_step_handler(msg, questions_third_step)
    return
  team_dict[message.chat.id].step += 1
  db = open("db.txt", "w")
  for key in team_dict:
    s = str(key) + str(team_dict[key].name) + str(team_dict[key].step) + str("\n")
    db.write(s)
  db.close()
  msg = bot.send_message(message.chat.id, "Ага, ку-ка-ре-ку! Ну ладно, перейдем к более серьезным заданиям:")
  bot.send_message(message.chat.id, """\
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
  bot.register_next_step_handler(msg, questions_fourth_step)


def questions_fourth_step(message):
  send_info(message, "four")
  if not message.text in {"Юра 8 3 4 5 6 7 1 2", "ключ Юры 8 3 4 5 6 7 1 2", "Ключ Юры 8 3 4 5 6 7 1 2"}:
    msg = bot.send_message(message.chat.id, "Джоан Роулинг сказала мне, что вы ошиблись.")
    bot.register_next_step_handler(msg, questions_fourth_step)
    return
  team_dict[message.chat.id].step += 1
  db = open("db.txt", "w")
  for key in team_dict:
    s = str(key) + str(team_dict[key].name) + str(team_dict[key].step) + str("\n")
    db.write(s)
  db.close()
  msg = bot.send_message(message.chat.id, "Правильно! А теперь финальное задание:")
  bot.send_message(message.chat.id, """\
1) Find 'Honorificabilitudinitatibus' in the biggest internet number
2) Wiki
3) Открой книгу на русском на предпросмотр
4) Найди ответ на 1.1.4
5) Представь каждый символ цифрой:

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
  bot.register_next_step_handler(msg, questions_fifth_step)


def questions_fifth_step(message):
  send_info(message, "five")
  if not message.text in {"вычисления", "Вычисления"}:
    msg = bot.send_message(message.chat.id, "Нет, ПОИЩИТЕ получше.")
    bot.register_next_step_handler(msg, questions_fifth_step)
    return
  team_dict[message.chat.id].step += 1
  db = open("db.txt", "w")
  for key in team_dict:
    s = str(key) + str(team_dict[key].name) + str(team_dict[key].step) + str("\n")
  db.close()
  bot.send_message(message.chat.id, """\
Отлично!
Теперь я вижу, что вы можете спасти пропавших ребят.
Приходите 06.04.19 во второй ГУМ к библиотеке к 13:00.
""")


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()

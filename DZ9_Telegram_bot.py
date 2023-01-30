# 39(1). Создайте программу для игры с конфетами человек против человека. 
# Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. 
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# В качестве дополнительного усложнения можно:
# a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
# b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, 
# позволяющий выяснить какое количесвто конфет необходимо брать, 
# чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
import telebot
from telebot import types
import datetime

bot = telebot.TeleBot("5983003991:AAGRDIe83UeLj7ID6hYAVA3Dm_vmqMtjU68")

global user_sweet

@bot.message_handler(commands = ["start"])

@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Правила")
    markup.add(but1)
    but2 = types.KeyboardButton("Начать игру")
    markup.add(but2)
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)

@bot.message_handler(content_types= ["text"])
def controller(message):
    global user_sweet
    print(message.text)
    if message.text == "Начать игру":
        bot.send_message(message.chat.id,"Введи количество конфет от 1 до 28")
        bot.register_next_step_handler(message,user_turn)
    elif message.text == "Правила":
        bot.send_message(message.chat.id,"На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход")
        button(message)
        
def user_turn(message):
    global user_sweet
    user_sweet = int(message.text)
    if user_sweet < 1 or user_sweet > 28:
            bot.send_message(message.chat.id,"Вы ввели неправильное число, введите число от 1 до 28")
            controller(message)
    elif user_sweet >= 1 and user_sweet <= 28:
        # bot.register_next_step_handler(message,user_turn)
        turn = user_sweet
        sweets -= turn

bot.infinity_polling()


# count = 221
# while count > 28:
#     print("Игрок1 введите количество конфет от 1 до 28: ")
#     p1 = int(input())
#     if p1 > 28:
#         print("Вы ввели число больше 28, введите число от 1 до 28")
#         continue
#     elif p1 < 1:
#         print("Вы ввели число меньше 1, введите число от 1 до 28")
#         continue
#     else:
#         count = count - p1
#         print(count)
#         if count < 28:
#           print("Игрок2 победил")
#         else:
#           while count > 28:    
#             print("Игрок2 введите количество конфет от 1 до 28: ")
#             p2 = int(input())
#             if p2 > 28:
#                 print("Вы ввели число больше 28, введите число от 1 до 28")
#                 continue
#             elif p2 < 1:
#                 print("Вы ввели число меньше 1, введите число от 1 до 28")
#                 continue
#             else:
#                 count = count - p2
#                 print(count)
#                 if count > 28:
#                   break
#                 else:
#                   print("Игрок 1 победил")

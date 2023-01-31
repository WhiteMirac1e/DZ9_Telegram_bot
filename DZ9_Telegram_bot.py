#на столе лежат конфеты
import telebot
import random
bot = telebot.TeleBot("6161821924:AAGRyYfSsJWvWbS8GdDlmbbDBEmqtcrzUdY")

sweets = 55
max_sweet = 28
user_turn = 0
bot_turn = 0
flag = ""

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id,f"Приветстую вас в игре!")
    bot.send_message(message.chat.id,f"Всего в игре {sweets} конфет")
    flag = random.choice(["user","bot"])
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы")
        controller(message)
    else:
        bot.send_message(message.chat.id,f"Первым ходит бот")
        controller(message)

def controller(message):
    global flag
    if sweets > 0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход, введите кол-во конфет от 0 до {max_sweet}")
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")

def user_input(message):
    global flag, user_turn, sweets
    user_turn = int(message.text)
    sweets -= user_turn
    flag = "user" if flag == "bot" else "bot"
    bot.send_message(message.chat.id, f"Осталось {sweets}")
    controller(message)

def bot_input(message):
    global sweets,bot_turn,flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"Осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

bot.infinity_polling()

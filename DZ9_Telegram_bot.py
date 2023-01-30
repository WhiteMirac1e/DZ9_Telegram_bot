#на столе лежат конфеты
import telebot
import random
bot = telebot.Telebot("5983003991:AAGRDIe83UeLj7ID6hYAVA3Dm_vmqMtjU68")

sweets = 55
max_sweet = 28
user_turn = 0
bot_turn = 0
flag = ""

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"Приветстую вас в игре!")
    bot.send_message(message.chat.id,f"Всего в игре {sweets} конфет")
    flag = random.choice(["user","bot"])
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы")
        controller(message,flag)
    else:
        bot.send_message(message.chat.id,f"Первым ходит бот")
        controller(message,flag)

def controller(message,flag):
    if sweets>0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход, введите кол-во конфет от 0 до {max_sweet}")
            bot.register_next_step_handler(message, user_input)
        else:
            bot.send_message(message.chat.id, f"Теперь ходит бот")
            bot_input(message)
    else:
        bot.send_message(message.chat.id, f"Победил {flag}!")


def bot_input(id):
    global sweets,bot_turn,flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"Осталось {sweets}")
    flag = "user" if flag

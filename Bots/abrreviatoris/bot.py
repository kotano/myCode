import telebot
import json

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message.chat.id)
    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('enter abbreviation', 'choose abbreviation')
    return bot.send_message(
        message.chat.id, "let's start", reply_markup=keyboard1)


def keyboard_abbreviations(start, end):
    keyboard_base = telebot.types.ReplyKeyboardMarkup(True)

    with open('abb.json', 'r', encoding='utf-8') as keyboard:
        keyboards = json.load(keyboard)

    for key in list(keyboards)[start:end]:
        keyboard_base.add(key)

    return keyboard_base


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == 'enter abbreviation':
        bot.send_message(message.chat.id, 'enter abbreviation without spaces')
    if message.text == 'choose abbreviation':
        bot.send_message(message.chat.id, 'which one?',
                         reply_markup=keyboard_abbreviations(0, 23))

    with open('abb.json', 'r', encoding='utf-8') as abb:
        abb = json.load(abb)

    try:
        return bot.send_message(message.chat.id, abb['{}'.format(message.text)])
    except KeyError:
        return bot.send_message(message.chat.id, 'try different one')


if __name__ == "__main__":
    bot.polling(none_stop=True)

from telebot import types
import telebot
import config
import requests
import json


# random joke
def get_random_joke(private=False):

    if private:
        r = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=11')
    else:
        r = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
    # r2 = r.text.replace('{"content":"', '')
    # content = r2.replace('"}', '')
    content = r.json(strict=False)['content']  # .replace('\\r', '')
    print(content)
    return content


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    print(message.chat.id)
    sti = open('stick/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Приличный анекдот')
    item2 = types.KeyboardButton("18+ 🔞")

    markup.add(item1, item2)

    r = bot.send_message(
        message.chat.id,
        "Всем работягам хай, остальным соболезную. Выбирай анекдот :)".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    return r


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':

        if message.text == "18+ 🔞":
            joke = get_random_joke(private=True)
            r = bot.send_message(message.chat.id, joke)

        elif message.text == 'Приличный анекдот':
            joke = get_random_joke(private=False)

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(
                'Неплохо, давай еще', callback_data='joke')
            markup.add(item1)

            r = bot.send_message(message.chat.id, joke, reply_markup=markup)
        else:
            r = bot.send_message(message.chat.id, 'А? ШО?')
        return r


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    r = None
    try:
        if call.message:
            if call.data == 'joke':
                joke = get_random_joke()
                r = bot.send_message(call.message.chat.id, joke)

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text='👌🏻😂🤙🏿', reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text="хех, посмеялся")

    except Exception as e:
        print(repr(e))

    finally:
        return r


if __name__ == "__main__":
    bot.polling(none_stop=True)

from unittest.mock import Mock

import pytest

import bot

test_id = 732101811  # Some message.chat.id


@pytest.fixture
def get_message():
    message = Mock()
    message.chat.id = test_id
    message.from_user.id = test_id
    message.text = 'Test'
    return message


def test_on_command(get_message):
    r = bot.on_command(get_message)
    expected = 'Напиши "Привет"'
    assert r.text == expected


def test_get_text_messages(get_message):
    message = get_message
    message.text = "Привет"
    answers = bot.get_text_messages(message)  # Returns list
    values = [message.text for message in answers]
    expected1 = 'Привет, давай я расскажу тебе гороскоп на сегодня.'
    expected2 = 'Выбери свой знак Зодиака'
    assert expected1 in values and expected2 in values

    # expected = 'Не понимаю. Напиши /help.'
    # assert expected in values


def test_callback_worker(monkeypatch, get_message):
    call = get_message
    call.data = 'zodiac'
    call.message.chat.id = call.chat.id

    expected = '{} {} {} {}'.format(
        bot.one[0],
        bot.two[0],
        bot.two_add[0],
        bot.three[0],
    )

    monkeypatch.setattr(bot, 'one', [bot.one[0]])
    monkeypatch.setattr(bot, 'two', [bot.two[0]])
    monkeypatch.setattr(bot, 'two_add', [bot.two_add[0]])
    monkeypatch.setattr(bot, 'three', [bot.three[0]])

    r = bot.callback_worker(call)

    assert expected == r.text

import pytest
from unittest.mock import Mock

import bot


# Вписываете сюда свой message.chat.id
# Чтобы его узнать запустите бота с коммандой /start
# и найдите chat id в консоли

test_id = 11111111


@pytest.fixture
def get_message():
    msg = Mock()
    msg.chat.id = test_id
    msg.text = 'test'
    return msg


static_joke = '''-Ты не одолжишь мне простой карандаш?
- На возьми.
-Это же красный.
-А что, красный для тебя уже слишком сложно?'''


def get_static_joke(*args, **kwargs): return static_joke


def test_get_random_joke(monkeypatch):

    def fakejoke(*args):
        def fakejson(**kwrags): return {'content': static_joke}
        r = Mock()
        r.json = fakejson
        return r

    monkeypatch.setattr(bot.requests, 'get', fakejoke)

    r = bot.get_random_joke()
    assert r == static_joke


def test_welcome(get_message):
    r = bot.welcome(get_message)
    exp = "Всем работягам хай, остальным соболезную. Выбирай анекдот :)"
    assert exp == r.text


def test_lalala(monkeypatch, get_message):
    monkeypatch.setattr(bot, 'get_random_joke', get_static_joke)

    message = get_message
    message.chat.type = 'private'
    message.text = 'Приличный анекдот'
    r = bot.lalala(message)
    assert r.text == static_joke


def test_callback_inline(monkeypatch, get_message):
    monkeypatch.setattr(bot, 'get_random_joke', get_static_joke)

    call = get_message
    call.message = Mock()
    call.message.chat.id = get_message.chat.id
    call.data = 'joke'

    r = bot.callback_inline(call)
    assert r.text == static_joke

import json
from unittest.mock import Mock

import pytest

import bot


test_id = 732101811


@pytest.fixture
def provide_message():
    message = Mock()
    message.chat.id = test_id
    message.text = 'Test'
    return message


def test_start_message(provide_message):
    r = bot.start_message(provide_message)
    assert r.text == "let's start"


def test_keyboard_abbreviations():
    r = bot.keyboard_abbreviations(0, 2)
    exp = [
        [{'text': 'asap'}],
        [{'text': 'idk'}],
    ]
    assert r.keyboard == exp


def test_menu(provide_message):
    with open('abb.json', 'r', encoding='utf-8') as abb:
        abb = json.load(abb)
    message = provide_message

    message.text = 'asap'
    r = bot.menu(message)
    assert r.text == abb['asap']

    message.text = 'idk'
    r = bot.menu(message)
    assert r.text == abb['idk']

    message.text = 'some wrong key'
    r = bot.menu(message)
    assert r.text == 'try different one'

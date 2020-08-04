import pytest
from bs4 import BeautifulSoup

import main

mainpage = open('HLTV_site.html', encoding='utf-8', newline='').read()
rankings = open('topigrokov.html', encoding='utf-8', newline='').read()
matches = open('matchi.html', encoding='utf-8', newline='').read()


#
class Site(object):
    pass
site = Site()
# site.mainpage = open('HLTV_site.html', encoding='utf-8', newline='').read()
# site.rankings = open('topigrokov.html', encoding='utf-8', newline='').read()
# site.matches = open('matchi.html', encoding='utf-8', newline='').read()


def f_get_parsed_page(arg):
    return BeautifulSoup(site.page, 'lxml')


def test_top5teams(monkeypatch):
    site.page = mainpage
    monkeypatch.setattr(main, 'get_parsed_page', f_get_parsed_page)
    assert main.top5teams() == ['Astralis',
                                'Natus Vincere', 'fnatic', 'mousesports', 'G2']


def test_top30teams(monkeypatch):
    site.page = rankings
    monkeypatch.setattr(main, 'get_parsed_page', f_get_parsed_page)
    # main.page = BeautifulSoup(page2, 'lxml')
    assert main.top30teams() == ['Astralis',
                                 'Natus Vincere',
                                 'fnatic',
                                 'mousesports',
                                 'G2',
                                 'Liquid',
                                 'FaZe',
                                 'Evil Geniuses',
                                 'FURIA',
                                 'Vitality',
                                 '100 Thieves',
                                 'NiP',
                                 'MAD Lions',
                                 'Gen.G',
                                 'MIBR',
                                 'OG',
                                 'Spirit',
                                 'GODSENT',
                                 'Cloud9',
                                 'ENCE',
                                 'Heretics',
                                 'Virtus.pro',
                                 'Complexity',
                                 'Winstrike',
                                 'North',
                                 'forZe',
                                 'Hard Legion',
                                 'Movistar Riders',
                                 'HAVU',
                                 'BIG']


def test_get_matches(monkeypatch):
    # main.matches = BeautifulSoup(page3, 'lxml')
    site.page = matches
    monkeypatch.setattr(main, 'get_parsed_page', f_get_parsed_page)
    assert main.get_matches() == [{'1': b'Sprout', '2': b'ALTERNATE aTTaX', 'time': b'16:00'},
                                  {'1': b'SMASH', '2': b'Nordavind',
                                      'time': b'16:50'},
                                  {'1': b'MAD Lions', '2': b'Complexity',
                                      'time': b'17:30'},
                                  {'1': b'sAw', '2': b'Real Betis',
                                      'time': b'18:00'},
                                  {'1': b'TheDice', '2': b'Heretics',
                                      'time': b'19:30'},
                                  {'1': b'Spirit', '2': b'forZe', 'time': b'19:50'},
                                  {'1': b'BIG', '2': b'Unicorns of Love',
                                      'time': b'20:00'},
                                  {'1': b'Liquid', '2': b'MIBR', 'time': b'21:10'}]


pytest.main()

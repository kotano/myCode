#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import sys
import urllib

""" Logpuzzle
На сервере лежит 9 изображений, являющихся частями одного изображения 
(фото дикой природы).

Дан лог файл веб-сервера, в котором среди прочих запросов содеражатся запросы
к этим изображениям. Нужно вытащить из файла url всех изображений и скачать их.
Затем создать файл index.html и собрать с его помощью все изображения в одну
картинку.

Вот что из себя представляет строка лога:
101.237.66.11 - - [05/Jun/2013:10:44:02 +0400] "GET /images/animals_07.jpg HTTP/1.1" 200 13632 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

Замечание: для создания html файла можно использовать самую простую разметку:
<html>
<body>
<img src="img0.jpg"><img src="img1.jpg">...
</body>
</html>

Подсказка: скачать файлы можно двумя способами:

1. Воспользоваться функцией, сохраняющей url по заданному пути file_name:
urllib.request.urlretrieve(url, file_name)

2. Скачать url и сохранить в файле:
import urllib.request
import shutil
...
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

"""


def read_urls(filename):
    """ 
    Возвращает список url изображений из данного лог файла,
    извлекая имя хоста из имени файла (apple-cat.ru_access.log). Вычищает
    дубликаты и возвращает список url, отсортированный по названию изображения.
    """

    f = open(filename, 'r')
    s = f.read()
    groups = re.findall(r'GET\s+(/images/animals_\d+.jpg)', s)

    host = re.search(r'(.*)_access\.log', filename).group(1)


    return sorted(['http://' + host + x for x in set(groups)])
  

def download_images(img_urls, dest_dir):
    """
    Получает уже отсортированный спискок url, скачивает каждое изображение
    в директорию dest_dir. Переименовывает изображения в img0.jpg, img1.jpg и тд.
    Создает файл index.html в заданной директории с тегами img, чтобы 
    отобразить картинку в сборе. Создает директорию, если это необходимо.
    """
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    if not os.path.exists(os.path.join(dest_dir, 'img')):
        os.makedirs(os.path.join(dest_dir, 'img'))

    html = ['<html><body>']
    for i, url in enumerate(img_urls):
        filename = os.path.join('img', 'img{}.jpg'.format(i))
        urllib.urlretrieve(url, os.path.join(dest_dir, filename))
        html.append('<img src="{}">\n'.format(filename))
    html.append('</body></html>')

    f = open(os.path.join(dest_dir, 'index.html'), 'w')
    f.write(''.join(html))
    f.close()

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])
    print img_urls


    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()

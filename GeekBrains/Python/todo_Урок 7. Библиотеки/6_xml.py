from xml.etree import ElementTree as ET

# парсим документ
with open('simple.xml', 'r', encoding='utf-8') as f:
    tree = ET.parse(f)
print (tree)

# гуляем по дереву
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

# доступ к элементу по индексу
print (root[0][1].text)

# поиск элементов
for node in tree.iter('neighbor'):
    print (node.attrib)

# поиск только внутри элемента
# find() - находит первого ребенка элемента
# elem.text — возвращает контент
# elem.get() - дает доступ к атрибуту элемента
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print (name, rank)


# Изменение документа
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes') # устанавливает и изменяет атрибуты

tree.write('simple2.xml')


# Удаление элементов
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('simple2.xml')


# Построение XML документов
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a) # <a><b /><c><d /></c></a>











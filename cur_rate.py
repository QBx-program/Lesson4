import requests
import re
from datetime import datetime


def currency_rates(get_cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code == 200:
        print('Соединение установлено с http://www.cbr.ru/scripts/XML_daily.asp')
    else:
        print(f'Ошибка соединения: {response.status_code}')
    date_server = datetime.strptime(response.headers['Date'], '%a, %d %B %Y %H:%M:%S %Z')
    print(f'Дата в ответе сервера: {date_server.date()}')
    text = response.text
    xml_list = []
    currency_list = {}
    _tag_check = False
    tag = ''
    param = ''
    for i, w in enumerate(text):
        if w == '<':
            _tag_check = True
            if i != 0:
                if text[i-1] != '>':
                    xml_list.append(param)
                param = ''
        if w == '>':
            tag = tag + w
            _tag_check = False
            xml_list.append(tag)
            tag = ''
        if _tag_check == True:
            tag = tag + w
        if _tag_check == False and w != '>' and w != '<':
            param = param + w
    date_rate = datetime.strptime(re.findall(r'(\d{2}\.\d{2}\.\d{4})', xml_list[1])[0], '%d.%m.%Y')
    for i, v in enumerate(xml_list):
        if v == '<CharCode>':
            currency_list[xml_list[i+1]] = []
            _currency = xml_list[i+1]
        if v == '<Nominal>':
            currency_list[_currency].append(xml_list[i + 1])
        if v == '<Value>':
            currency_list[_currency].append(float(xml_list[i+1].replace(',', '.')))
            currency_list[_currency].append(date_rate.date())
    return currency_list
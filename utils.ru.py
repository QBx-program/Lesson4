import cur_rate

get_cur = (input('Введите банковское наименование валюты ')).upper()
ans_cur = cur_rate.currency_rates(get_cur)
if ans_cur.get(get_cur):
    print(f'{get_cur}/RUB = {ans_cur[get_cur][1]} за {ans_cur[get_cur][0]} рубль(-ей) на {ans_cur[get_cur][2]}')
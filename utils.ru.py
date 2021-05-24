import cur_rate

def all_currency():
    a_cur = cur_rate.currency_rates()
    for i, v in enumerate(a_cur.items()):
        print(f'{v[0]} = {a_cur[v[0]][1]} рублей за {a_cur[v[0]][0]} {v[0]} на {a_cur[v[0]][2]}')

def answer_rate(g_cur):
    a_cur = cur_rate.currency_rates()
    if a_cur.get(g_cur):
        print(f'{g_cur}/RUB = {a_cur[g_cur][1]} рублей за {a_cur[g_cur][0]} {g_cur} на {a_cur[g_cur][2]}')
    else:
        print('Такой валюты не существует')

def file_run():
    get_cur = (input('Введите банковское наименование валюты (введите "all", чтобы показать все) ')).upper()
    if get_cur == 'ALL':
        all_currency()
    else:
        answer_rate(get_cur)

def main(argv):
    cur = str(argv[1]).upper()
    if cur == "ALL":
        all_currency()
    else:
        answer_rate(cur)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        exit(main(sys.argv))
    else:
        file_run()
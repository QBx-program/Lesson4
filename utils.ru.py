import cur_rate

def answer_rate(a_cur, g_cur):
    if a_cur.get(g_cur):
        print(f'{g_cur}/RUB = {a_cur[g_cur][1]} рублей за {a_cur[g_cur][0]} {g_cur} на {a_cur[g_cur][2]}')
    else:
        print('Такой валюты не существует')

def file_run():
    get_cur = (input('Введите банковское наименование валюты ')).upper()
    ans_cur = cur_rate.currency_rates(get_cur)
    answer_rate(ans_cur, get_cur)

def main(argv):
    ans_cur = cur_rate.currency_rates(str(argv[1]))
    cur = argv[1].upper()
    answer_rate(ans_cur, cur)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        exit(main(sys.argv))
    else:
        file_run()
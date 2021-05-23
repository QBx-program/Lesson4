import cur_rate

get_cur = (input('Введите банковское наименование валюты ')).upper()
ans_cur = cur_rate.currency_rates(get_cur)
if ans_cur.get(get_cur):
    print(f'{get_cur}/RUB = {ans_cur[get_cur][1]} за {ans_cur[get_cur][0]} рубль(-ей) на {ans_cur[get_cur][2]}')

def main(argv):
    if len(argv) > 0:
        print('Ответ из консоли:')
        ans_cur = cur_rate.currency_rates(str(argv[1]))
        cur = argv[1].upper()
        if ans_cur.get(cur):
            print(f'{cur}/RUB = {ans_cur[cur][1]} за {ans_cur[cur][0]} рубль(-ей) на {ans_cur[cur][2]}')
        else:
            print('Такой валюты не существует')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        exit(main(sys.argv))
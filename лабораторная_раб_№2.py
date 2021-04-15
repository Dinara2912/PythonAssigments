def task91():
    print("< Книги на лето >")


def task92():
    print("< Посещаемость >")
    b = set()
    a = int(input())
    w = int(input())
    for f in range(w):
        b.add(input())
    for f in range(a - 1):
        n = set()
        for i in range(int(input())):
            n.add(input())
        b = b & n
    for i in b:
        print(i)


def task93():
    print("< Однофамильцы >")
    men = int(input())
    men_works = [input() for _ in range(men)]
    result = 0
    for example in set(men_works):
        cout = 0
        for name in men_works:
            if example == name:
                cout += 1
        if cout > 1:
            result += cout
    print(result)


def task94():
    print("< Рецепты >")
    ingredient_hold_mn = set()
    ingredient_eat = set()
    ingredient_hold = int(input())
    for i in range(ingredient_hold):
        ingredient_hold_mn.add(input())
    name_recept_N = int(input())
    for i in range(name_recept_N):
        name_recept = input()
        ingredient_eat_M = int(input())
        flag = True
        for j in range(ingredient_eat_M):
            ingredient_eat.add(input())
        for i in ingredient_eat:
            if not i in ingredient_hold_mn:
                flag = False
        if flag:
            print(name_recept)
        ingredient_eat = set()


def task95():
    print("< Новые блюда >")
    menu = set()
    use_menu = set()
    menu_not_use = set()
    menu_N = int(input())
    for i in range(menu_N):
        menu.add(input())
    day_menu_true = int(input())
    for i in range(day_menu_true):
        menu_in_day_N = int(input())
        for j in range(menu_in_day_N):
            use_menu.add(input())
    menu_not_use = menu - use_menu
    print(*menu_not_use, sep='\n')


def task101():
    print("< Какая-то там буква >")
    s = input('Введите слово: ')
    n = int(input('Введите натуральное число: '))
    if (0 < n <= len(s)):
        print(s[n - 1])
    else:
        print('ОШИБКА')


def task102():
    print("< Цезарь его знает >")

    def cesar_code(letter, shift):
        if letter.isalpha():
            number = ord(letter) + shift % 32
            if number > 1103:
                number -= 32
            return chr(number)
        return letter

    shift = int(input())
    for l in input():
        print(cesar_code(l, shift), end='')


def task103():
    print("< Скажите а (заглавное) >")
    s = input()
    if s[0].lower() == 'а':
        print('ДА')
    else:
        print('НЕТ')


def task104():
    print("< Последняя буква 2 >")
    ch = input()
    print(ch[-1])


def task105():
    print("< Продолжайте говорить А >")
    while True:
        word = input('Слово: ')
        if word[0].lower() != 'а':
            break


def task106():
    print("< Ползем вниз >")


def task111():
    print("< Розенкранц и Гильденстерн меняют профессию >")
    n = input()
    print(len(max(n.split('р'), key=len)))


def task112():
    print("< Фильтр >")
    N = int(input('N = '))
    text = [input() for _ in range(N)]

    for t in text:
        if t[:4] == '####':
            continue

        if t[:2] == '%%':
            print(t[2:])
        else:
            print(t)


def task113():
    print("< Именно та буква >")
    a = input()
    b = int(input())
    c = input()
    if len(a) < b or len(c) != 1 or str(b).find('-') != -1 or b < 1:
        print('ОШИБКА')
    elif a[b - 1] == c:
        print('ДА')
    else:
        print('НЕТ')


def task114():
    print("< Минификатор >")


def task115():
    print("< Буквоедство >")
    s = input()
    while len(s):
        print(s)
        s = s[1: -1]


def task121():
    print("< Белый список >")
    white_list = []
    for i in range(int(input())):
        white_list.append(input())
    search = []
    for j in range(int(input())):
        search.append(input())
    for k in search:
        if k in white_list:
            print(k)


def task122():
    print("< Проверка чека >")
    n = input()
    s = []
    s1 = []
    b = 0
    lot, itogo = int(n[:4]), int(n[4:])
    for i in range(lot):
        a = input()
        price, kolvo, summ = int(a[0:7]), int(a[8:12]), int(a[13:18])
        if price * kolvo != summ:
            s.append(i + 1)
        summ1 = kolvo * price
        s1.append(summ1)
    for i in s1:
        b += i
    print(itogo - b)
    for i in s:
        print(i, end=' ')


def task123():
    print("<  Подробный список покупок >")
    print(*reversed([' '.join((input(), input())) for _ in range(int(input()))]), sep='\n')


def task124():
    print("< RLE >")



def task125():
    print("< Периодическая десятичная дробь >")
    n = int(input())
    r = 1
    rr = []
    dd = []
    while r not in rr:
        rr.append(r)
        dd.append(10 * r // n)
        r = 10 * r % n
    print(*dd[rr.index(r):])



def task126():
    print("<  Крупные буквы >")
    f = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '], 'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
         'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   '], 'D': ['**   ', '* *  ', '* *  ', '* *  ', '**   '],
         'E': ['***  ', '*    ', '**   ', '*    ', '***  '], 'F': ['***  ', '*    ', '**   ', '*    ', '*    '],
         'G': [' **  ', '*    ', '* *  ', '* *  ', ' **  '], 'H': ['* *  ', '* *  ', '***  ', '* *  ', '* *  '],
         'I': ['***  ', ' *   ', ' *   ', ' *   ', '***  '], 'J': [' **  ', '  *  ', '  *  ', '* *  ', ' *   '],
         'K': ['* *  ', '**   ', '*    ', '**   ', '* *  '], 'L': ['*    ', '*    ', '*    ', '*    ', '***  '],
         'M': ['* *  ', '***  ', '***  ', '***  ', '* *  '], 'N': ['* *  ', '***  ', '***  ', '* *  ', '* *  '],
         'O': ['***  ', '* *  ', '* *  ', '* *  ', '***  '], 'P': ['***  ', '* *  ', '***  ', '*    ', '*    '],
         'Q': ['***  ', '* *  ', '* *  ', '***  ', '***  '], 'R': ['**   ', '* *  ', '**   ', '* *  ', '* *  '],
         'S': [' **  ', '*    ', ' *   ', '  *  ', '**   '], 'T': ['***  ', ' *   ', ' *   ', ' *   ', ' *   '],
         'U': ['* *  ', '* *  ', '* *  ', '* *  ', '***  '], 'V': ['* *  ', '* *  ', '* *  ', '* *  ', ' *   '],
         'W': ['* *  ', '* *  ', '* *  ', '***  ', '* *  '], 'X': ['* *  ', '* *  ', ' *   ', '* *  ', '* *  '],
         'Y': ['* *  ', '* *  ', '* *  ', ' *   ', ' *   '], 'Z': ['***  ', '  *  ', ' *   ', '*    ', '***  ']}
    s = input()
    for i in range(5):
        for k in s:
            print(f.get(k)[i], end='')
        print()

def task127():
    print("< Масштабирование >")
    lenght = int(input())  # длина
    width = int(input())  # ширина
    list_ = []
    for i in range(lenght):
        list_.append(input())
    list2 = []
    for i in list_[::2]:
        list2.append(i[::2])
    lenght = lenght // 2
    width = width // 2
    print(lenght, width)
    for i in list2:
        print(i)

def task131():
    print("< Наперстки >")
    n = int(input())
    li = [''] * n
    for i in range(n):
        li[i] = input()
    k = int(input())
    for i in range(k):
        x = int(input())
        tmp = [''] * x
        for j in range(x):
            tmp[j] = li[int(input()) - 1]
        li = tmp
    for i in range(len(li)):
        print(li[i])

def task132():
    print("< Сорт. в обр. порядке >")


def task133():
    print("< А272727 >")
    res = []
    for _ in range(int(input())):
        res.append(sum((x == y for x, y in zip(res, reversed(res)))))
    print(*res, sep='\n')

def task134():
    print("< Два Пути >")
    num = int(input())
    first = [int(input()) for i in range(num)]
    second = first[:]
    training = int(input())
    for i in range(training):
        brother = int(input())
        if brother == 1:
            first[int(input())] += int(input())
        elif brother == 2:
            second[int(input())] += int(input())
    print(*first)
    print(*second)
    dd = 0
    for i in range(len(first)):
        if first[i] == second[i]:
            dd = dd + 1
    print(dd)

def task135():
    print("< Финал и не финал >")

def task136():
    print("< Крупные буквы - 2 >")
    f = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '], 'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
         'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   '], 'D': ['**   ', '* *  ', '* *  ', '* *  ', '**   '],
         'E': ['***  ', '*    ', '**   ', '*    ', '***  '], 'F': ['***  ', '*    ', '**   ', '*    ', '*    '],
         'G': [' **  ', '*    ', '* *  ', '* *  ', ' **  '], 'H': ['* *  ', '* *  ', '***  ', '* *  ', '* *  '],
         'I': ['***  ', ' *   ', ' *   ', ' *   ', '***  '], 'J': [' **  ', '  *  ', '  *  ', '* *  ', ' *   '],
         'K': ['* *  ', '**   ', '*    ', '**   ', '* *  '], 'L': ['*    ', '*    ', '*    ', '*    ', '***  '],
         'M': ['* *  ', '***  ', '***  ', '***  ', '* *  '], 'N': ['* *  ', '***  ', '***  ', '* *  ', '* *  '],
         'O': ['***  ', '* *  ', '* *  ', '* *  ', '***  '], 'P': ['***  ', '* *  ', '***  ', '*    ', '*    '],
         'Q': ['***  ', '* *  ', '* *  ', '***  ', '***  '], 'R': ['**   ', '* *  ', '**   ', '* *  ', '* *  '],
         'S': [' **  ', '*    ', ' *   ', '  *  ', '**   '], 'T': ['***  ', ' *   ', ' *   ', ' *   ', ' *   '],
         'U': ['* *  ', '* *  ', '* *  ', '* *  ', '***  '], 'V': ['* *  ', '* *  ', '* *  ', '* *  ', ' *   '],
         'W': ['* *  ', '* *  ', '* *  ', '***  ', '* *  '], 'X': ['* *  ', '* *  ', ' *   ', '* *  ', '* *  '],
         'Y': ['* *  ', '* *  ', '* *  ', ' *   ', ' *   '], 'Z': ['***  ', '  *  ', ' *   ', '*    ', '***  ']}
    s = input()
    for i in range(5):
        for k in s:
            print(f.get(k)[i], end='')
        print()

def task137():
    print("< Тотальная децимация >")
    n = int(input())
    names = [input() for i in range(n)]
    step = int(input())
    rounds = int(input())
    for j in range(rounds):
        del names[step - 1::step]
    print('\n'.join(names))

def task141():
    print("< Только без лука >")
    q = int(input())
    a = []
    for i in range(q):
        s = input()
        if 'лук' not in s:
            a.append(s)
    print(', '.join(a))

def task142():
    print("< Маяковский >")


def task143():
    print("< Маяковский >")
    print('\n'.join(input().split()))


def task144():
    print("< Вертикальная диаграмма >")
    n = list(map(int, input().split()))

    xmax = len(n)
    ymax = max(n)

    print('*' * (xmax + 2))
    print('*' + ' ' * xmax + '*')
    for y in range(1, ymax + 1):
        print(end='*')
        for nk in n:
            if nk >= ymax - y + 1:
                print(end='*')
            else:
                print(end=' ')
        print('*')


def task145():
    print("< GET >")
    a = input()
    s = input()
    a = a[a.find(s) + len(s) + 1:]
    q = [a.find('?'), a.find('&')]
    for i in range(q.count(-1)):
        q.remove(-1)
    if q == []:
        print(a)
    else:
        print(a[:min(q)])

def task151():
    print("<  >")
    a = input()
    print(*[i for i in input().split() if a.upper() in i.upper()], sep='\n')


def task152():
    print("< Знаков без пробелов >")
    s = input()
    c = 0
    for a in s:
        if a != ' ' and a != '\t':
            c += 1
    print(c)

def task153():
    print("< Длинношееед >")
    s = input().lower()
    n = 0
    for i in range(len(s)):
        if s.count(s[i]) > n:
            n = s.count(s[i])
    print(n)

def task154():
    print("<  >")

def task155():
    print("<  >")

def task161():
    print("<  >")

def task162():
    print("<  >")

def task163():
    print("<  >")

def task164():
    print("<  >")

def task171():
    print("<  >")

def task172():
    print("<  >")

def task173():
    print("<  >")

def task174():
    print("<  >")

def task175():
    print("<  >")

if __name__ == '__main__':
    task153()

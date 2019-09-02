import requests
word = input('Введите слово для флекса в начальной форме: ')
if len(word) > 0:
    page = requests.get('http://wikislovo.ru/morphemic/' + word)
    if page.status_code != 200:
        print('Слово не найдено. Попробуйте ещё раз.')
    else:
        page = page.content.decode("utf-8")
        page = page.splitlines()
        line = [s for s in page if "корень:" in s][0]
        morph = line.strip(' ').strip('<li>').strip('</li>').replace('корень: ', '').replace(',', '').split(' ')
        for i in morph:
            word = word.replace(i, 'флекс')
        print(word)
else:
    print('Вы ввели пустое слово.')
